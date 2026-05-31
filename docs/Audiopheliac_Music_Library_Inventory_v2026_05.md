# Audiopheliac Music Library Inventory

**Version:** 2026.05.1
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Purpose:** Canonical inventory of the FLAC and MP3 music library at `M:\\`. Tracks album-level provenance (source format), rip / import dates, and integration with downstream listening surfaces (Plex Media Server, vehicle streaming via Tailscale Option 2 node-share).

This doc complements `docs/vinyl\_capture\_reference.md` (vinyl rip workflow, naming conventions, archive discipline) and serves as the running record of what lives in the library and how it got there.

\---

## Library Root

`M:\\` is the primary FLAC + MP3 music library. Monitored by Plex Media Server for streaming to in-vehicle and remote playback (per memory: vehicle Plex streaming is a durable use case, off-LAN reachability via Tailscale Option 2 node-share).

\---

## Folder and File Naming Conventions

### Album folder pattern

```
M:\\<Artist>\\<Album Title> (<Release Year>) - <Source Tag> (<DDMMMYY>)\\
```

Where `<Source Tag>` is one of:

|Source Tag|Meaning|
|-|-|
|`Vinyl Rip`|Captured from vinyl via the AT-LP120XUSB to Mani II to MOTU M4 to Audacity chain. Full workflow in `docs/vinyl\_capture\_reference.md`.|
|`CD Backup`|Ripped from a physical CD as lossless FLAC (EAC, dBpoweramp, or equivalent).|
|`Digital Purchase`|Downloaded as lossless from Bandcamp, HDtracks, Qobuz, or similar.|
|`Streaming Capture`|Captured from a streaming source. (Rare and not the primary library workflow.)|

The source tag plus date pattern is intentional: it allows multiple captures of the same album to coexist under one artist folder with clear provenance. Example: a vinyl rip of Tom Petty's *Wildflowers* could sit beside a CD backup of the same album, distinguished by source tag in the folder name.

### Track file pattern

* FLAC: `NN-Track Title.flac` (two-digit track number, dash separator, song title, `.flac` extension)
* MP3: `NN-Track Title.mp3` (same pattern, `.mp3` extension)

### Artist folder

* `<Artist Name>` as published, no leading "The".

### Date format

`DDMMMYY` (day, three-letter month uppercase, two-digit year). Example: `30MAY26`.

Trade-off acknowledged: this format is human-readable and unambiguous across US / EU date conventions, but does not sort chronologically when listed alphabetically. If chronological sortability ever becomes the higher priority, switch to ISO 8601 (`YYYY-MM-DD`).

\---

## Inventory: Vinyl Rips

|#|Artist|Album|Release Year|Rip Date|Path|Notes|
|-|-|-|-|-|-|-|
|1|David Bowie|Let's Dance|1983|2026-05-30|`M:\\David Bowie\\Let's Dance (1983) - Vinyl Rip (30MAY26)\\`|First vinyl rip in the archive. Inaugural end-to-end use of the rip workflow: AT-LP120XUSB (PHONO mode, AT-VM95SH Shibata cart at 2.0 g VTF), Schiit Mani II (MM mode, gain calibrated on Modern Love test cut to peaks at -12 dBFS), MOTU M4 (line in 3/4, WASAPI host, 48 kHz / 24-bit), Audacity 3.7.7 (Click Removal at 250/30, Loudness Normalization to -14 LUFS, no bass EQ applied per archive-neutrality discipline). 8 tracks, \~250 MB FLAC archive.|

\---

## Inventory: CD Backups

(none yet)

\---

## Inventory: Digital Purchases

(none yet)

\---

## Inventory: MP3 Quick-Reference Listening Copies

Listening copies (VBR \~190 kbps or CBR 256 kbps MP3) typically generated during the vinyl rip workflow for car-listening evaluation pre-mastering. Stored at `M:\\<Artist>\\` alongside the FLAC archive when retained.

|Artist|Album|Source|Bitrate|Date|
|-|-|-|-|-|
|David Bowie|Let's Dance|Vinyl Rip 30MAY26|VBR Standard \~190 kbps and CBR 256 kbps|2026-05-30|

\---

## When to Update This Doc

Update this doc when any of the following happen:

* A new vinyl rip is finalized into the library.
* A new CD backup is ripped and added.
* A new digital purchase is added.
* The library root path changes.
* The folder or track naming conventions change.
* A second-source capture of an existing album is added (e.g., a vinyl rip of an album already present as a CD backup).

Source documents to keep in sync:

* `CLAUDE.md` (HARDWARE, SIGNAL CHAIN MAP, INFRASTRUCTURE AND SYNC sections).
* `docs/vinyl\_capture\_reference.md` (rip workflow + naming convention authority for the vinyl source path).
* `docs/Audiopheliac\_Audio\_Source\_Inventory\_v2026\_05.md` (parent source inventory).

\---

*The library is where every cable, waveform, and decibel ends up. This is the record of what's there.*

