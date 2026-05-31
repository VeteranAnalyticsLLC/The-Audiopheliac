"""Local audio playback engine for the Audiopheliac Cockpit.

Plays files from the GDMARCHE filesystem (typically M:\\ for the music library,
D:\\ for Creative Studio output) through the Windows default audio device, which
is normally the M-Audio AIR Hub feeding the Yamaha HS7 + JBL LSR310S monitor
chain. This is the "Studio" destination — sound at the desk, on monitors,
without waking the rest of the house through the Yamaha.

Engine selection (first available wins):
    1. VLC                (C:\\Program Files\\VideoLAN\\VLC\\vlc.exe)
       - best transport control, gapless, handles FLAC/MP3/WAV/AAC/OGG/M4A
       - launched with --intf dummy so it stays headless; logs to stderr
       - we kill the process to stop
    2. Windows Media Player    (wmplayer.exe in PATH)
       - always present on Windows; basic playback only
    3. os.startfile            (shell association)
       - last-ditch; whatever the user has set for .flac opens
       - we can't stop or query this; it's "open and forget"

Threading: a single _ActivePlayback object holds the current Popen handle and
the file/queue metadata. start() kills any prior process before launching.
This is single-zone by design — one local player, one destination.

Audio device routing: the engine inherits Windows' default playback device.
To target the AIR Hub specifically, set Windows default to "Speakers (AIR Hub)"
in Settings > System > Sound. The Cockpit does NOT switch Windows defaults at
runtime; that's a permanent OS-level decision the user already made.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# Filename extensions the Cockpit treats as playable audio. Anything else
# is hidden from the Local browser to keep the list short.
AUDIO_EXTS: tuple[str, ...] = (
    ".flac", ".mp3", ".wav", ".aac", ".aiff", ".aif", ".ogg", ".opus",
    ".m4a", ".alac", ".wma", ".dsf", ".dff", ".ape",
)

_NO_WINDOW = 0x08000000  # subprocess.CREATE_NO_WINDOW on Windows

# Standard install locations for the engines, in preference order.
_VLC_CANDIDATES: tuple[str, ...] = (
    r"C:\Program Files\VideoLAN\VLC\vlc.exe",
    r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
)
_WMP_CANDIDATES: tuple[str, ...] = (
    r"C:\Program Files\Windows Media Player\wmplayer.exe",
    r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe",
)


class LocalPlayerError(RuntimeError):
    pass


@dataclass
class EngineInfo:
    name: str           # "vlc" | "wmp" | "shell"
    path: str           # executable path, or "" for shell
    label: str          # human label for the UI


def detect_engine() -> EngineInfo:
    """Pick the best available engine on this machine.

    Order: VLC, Windows Media Player, shell. The first match wins. We cache
    nothing — detection is two stat() calls; the cost is negligible and the
    cache invalidation is more trouble than it's worth.
    """
    for p in _VLC_CANDIDATES:
        if os.path.isfile(p):
            return EngineInfo(name="vlc", path=p, label="VLC")
    vlc_in_path = shutil.which("vlc")
    if vlc_in_path:
        return EngineInfo(name="vlc", path=vlc_in_path, label="VLC")
    for p in _WMP_CANDIDATES:
        if os.path.isfile(p):
            return EngineInfo(name="wmp", path=p, label="Windows Media Player")
    wmp_in_path = shutil.which("wmplayer")
    if wmp_in_path:
        return EngineInfo(name="wmp", path=wmp_in_path, label="Windows Media Player")
    return EngineInfo(name="shell", path="", label="Default file association")


@dataclass
class _ActivePlayback:
    proc: Optional[subprocess.Popen] = None
    engine: str = ""
    files: list[str] = field(default_factory=list)   # absolute paths in queue order
    started_at: float = 0.0
    folder: str = ""                                  # source folder if folder-play
    title: str = ""                                   # display label


class LocalPlayer:
    """Single-zone local audio player. One queue, one process, one destination."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._engine = detect_engine()
        self._active = _ActivePlayback()

    # ----- introspection -----

    def engine(self) -> EngineInfo:
        return self._engine

    def is_playing(self) -> bool:
        with self._lock:
            p = self._active.proc
            if p is None:
                return False
            return p.poll() is None

    def status(self) -> dict[str, Any]:
        with self._lock:
            playing = bool(self._active.proc and self._active.proc.poll() is None)
            return {
                "engine": self._engine.name,
                "engine_label": self._engine.label,
                "engine_path": self._engine.path,
                "playing": playing,
                "title": self._active.title,
                "folder": self._active.folder,
                "queue_len": len(self._active.files),
                "queue": [Path(p).name for p in self._active.files[:20]],
                "started_at": self._active.started_at,
            }

    # ----- control -----

    def stop(self) -> None:
        with self._lock:
            p = self._active.proc
            self._active = _ActivePlayback()
        if p is not None and p.poll() is None:
            try:
                p.terminate()
                # Give VLC/WMP a beat to flush; if it doesn't exit, force-kill.
                for _ in range(15):
                    if p.poll() is not None:
                        break
                    time.sleep(0.1)
                if p.poll() is None:
                    p.kill()
            except OSError:
                pass

    def play_url(self, url: str, *, title: str = "") -> dict[str, Any]:
        """Play a network URL (http/https) through the local engine.

        Used for MinimServer DLNA URLs, Net Radio HTTP streams, and any other
        source whose content is fetchable via a URL. VLC handles this natively;
        WMP and shell are not viable for arbitrary network URLs and will raise.
        """
        if not url.lower().startswith(("http://", "https://")):
            raise LocalPlayerError(f"play_url expects http(s)://, got: {url}")
        self.stop()
        engine = self._engine
        if engine.name != "vlc":
            raise LocalPlayerError(
                f"Network URL playback requires VLC; current engine is {engine.label}. "
                f"Install VLC to enable streaming MinimServer / Net Radio / etc. to Studio."
            )
        args = [
            engine.path,
            "--intf", "dummy",
            "--play-and-exit",
            "--no-video",
            "--quiet",
            "--network-caching=1500",   # 1.5s cache: balance latency vs. dropouts
            url,
        ]
        proc = subprocess.Popen(
            args,
            creationflags=_NO_WINDOW,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            close_fds=True,
        )
        with self._lock:
            self._active = _ActivePlayback(
                proc=proc,
                engine=engine.name,
                files=[url],
                started_at=time.time(),
                folder="",
                title=title or url,
            )
        return self.status()

    def play_files(self, files: list[str], *, title: str = "",
                   folder: str = "") -> dict[str, Any]:
        """Play one or more files. If multiple, VLC handles the queue natively;
        WMP/shell will only play the first reliably.

        Returns the new status snapshot.
        """
        if not files:
            raise LocalPlayerError("no files supplied")
        abspaths: list[str] = []
        for f in files:
            ap = os.path.abspath(f)
            if not os.path.isfile(ap):
                raise LocalPlayerError(f"not a file: {ap}")
            if Path(ap).suffix.lower() not in AUDIO_EXTS:
                raise LocalPlayerError(f"unsupported audio extension: {ap}")
            abspaths.append(ap)

        # Tear down any current playback first; we are single-zone.
        self.stop()

        engine = self._engine
        proc: Optional[subprocess.Popen] = None
        if engine.name == "vlc":
            # --intf dummy: no UI window
            # --play-and-exit: VLC exits after the queue completes (so is_playing flips false)
            # --no-video: never open a video window (album-art images don't pop up)
            # --quiet: less noise in stderr
            args = [
                engine.path,
                "--intf", "dummy",
                "--play-and-exit",
                "--no-video",
                "--quiet",
                *abspaths,
            ]
            proc = subprocess.Popen(
                args,
                creationflags=_NO_WINDOW,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                close_fds=True,
            )
        elif engine.name == "wmp":
            # WMP only takes a single path on the command line for headless
            # behavior. If multiple files are passed, we play the first; the
            # client should call back to advance.
            args = [engine.path, abspaths[0]]
            proc = subprocess.Popen(
                args,
                creationflags=_NO_WINDOW,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                close_fds=True,
            )
        else:
            # Shell association. We can't track this process (os.startfile
            # returns no handle), but launching is fire-and-forget. status()
            # will report not-playing because proc is None, which is honest.
            try:
                os.startfile(abspaths[0])  # type: ignore[attr-defined]
            except AttributeError as e:  # non-Windows
                raise LocalPlayerError(
                    "os.startfile is only available on Windows"
                ) from e
            except OSError as e:
                raise LocalPlayerError(f"shell launch failed: {e}") from e

        with self._lock:
            self._active = _ActivePlayback(
                proc=proc,
                engine=engine.name,
                files=abspaths,
                started_at=time.time(),
                folder=folder or str(Path(abspaths[0]).parent),
                title=title or Path(abspaths[0]).name,
            )
        return self.status()

    def play_folder(self, folder: str, *, recursive: bool = False,
                    title: str = "") -> dict[str, Any]:
        """Enumerate audio files in `folder` (optionally recursively) and play."""
        base = Path(folder)
        if not base.is_dir():
            raise LocalPlayerError(f"not a directory: {folder}")
        if recursive:
            iterator = base.rglob("*")
        else:
            iterator = base.iterdir()
        files = sorted(
            str(p) for p in iterator
            if p.is_file() and p.suffix.lower() in AUDIO_EXTS
        )
        if not files:
            raise LocalPlayerError(f"no playable audio files in {folder}")
        label = title or base.name or folder
        return self.play_files(files, title=label, folder=str(base))


# ---------------- directory browsing ----------------

def list_dir(path: str) -> dict[str, Any]:
    """Return a Cockpit-friendly directory listing.

    Hides hidden files and non-audio non-folders. Each entry is
    {kind, name, path, ext, is_audio}.
    """
    p = Path(path)
    if not p.is_dir():
        raise LocalPlayerError(f"not a directory: {path}")
    folders: list[dict[str, Any]] = []
    audio: list[dict[str, Any]] = []
    for entry in sorted(p.iterdir(), key=lambda e: (e.is_file(), e.name.lower())):
        name = entry.name
        if name.startswith(".") or name.startswith("$"):
            continue
        if entry.is_dir():
            folders.append({
                "kind": "folder",
                "name": name,
                "path": str(entry),
            })
        elif entry.is_file():
            ext = entry.suffix.lower()
            if ext in AUDIO_EXTS:
                audio.append({
                    "kind": "audio",
                    "name": name,
                    "path": str(entry),
                    "ext": ext.lstrip("."),
                })
    parent = str(p.parent) if p.parent != p else ""
    return {
        "path": str(p),
        "parent": parent,
        "folders": folders,
        "files": audio,
        "total": len(folders) + len(audio),
    }


def validate_root(path: str, allowed_roots: list[str]) -> str:
    """Reject path-traversal: confirm `path` lives under one of `allowed_roots`.

    Returns the resolved absolute path on success. Raises LocalPlayerError
    on rejection. Used by every HTTP-facing endpoint that takes a path.
    """
    p = Path(path).resolve()
    for root in allowed_roots:
        try:
            root_resolved = Path(root).resolve()
        except OSError:
            continue
        try:
            p.relative_to(root_resolved)
            return str(p)
        except ValueError:
            continue
    raise LocalPlayerError(
        f"path is not under an allowed root: {path} "
        f"(allowed: {', '.join(allowed_roots)})"
    )
