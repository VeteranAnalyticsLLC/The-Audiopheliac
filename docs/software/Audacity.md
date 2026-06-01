# Software Package Configuration Profile - Audacity

**Package:** Audacity 3.7.7
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Profile version:** 2026.05.1
**Last reviewed:** 2026-05-31
**Status:** Active

> Per-package configuration, settings, and troubleshooting profile for The Audiopheliac. Audacity is the primary capture-and-edit utility for the vinyl-to-FLAC archive pipeline.

---

## 1. Overview

Audacity is the primary capture surface for the vinyl-to-FLAC archive workflow. It hosts the recording session for vinyl rips (AT-LP120XUSB > Schiit Mani II > MOTU M4 LINE IN 3-4), the per-side edit pass (silence trim, click removal, loudness normalization), and the FLAC export to the canonical archive path. It also serves as Ableton Live's configured Sample Editor (right-click a sample in Live > opens it in Audacity for destructive editing). Open source, free, cross-platform. Cross-reference: `docs/vinyl_capture_reference.md` (canonical capture workflow), `docs/software/AbletonLive12.md` (Live ↔ Audacity integration), `docs/Audiopheliac_Music_Library_Inventory_v2026_05.md` (vinyl rip inventory), `skills/the-mentor/SKILL.md` (Lesson 1 vinyl rip in Audacity).

---

## 2. Installation

| Field | Value |
|---|---|
| Install source | https://www.audacityteam.org/ (vendor Windows installer) |
| Install path | `C:\Program Files\Audacity\Audacity.exe` (verified via Ableton Settings > File & Folder > Sample Editor field) |
| Vendor version (last verified) | 3.7.7 on 2026-05-30 (Mentor Lesson 1 Bowie *Let's Dance* vinyl rip) |
| Auto-update | In-app: Help > Check for Updates (manual). No background auto-update. |
| License / subscription | Free / open source (GPLv3) |
| Auth email | N/A (no account required) |

---

## 3. Account / Credentials

| Field | Value |
|---|---|
| Username / handle | N/A |
| Account email | N/A (no account required for use) |
| Support contact | Audacity Forum: https://forum.audacityteam.org/ |
| Knowledge base | https://manual.audacityteam.org/ (canonical Audacity Manual) |

---

## 4. Configuration

Audacity settings live at Edit > Preferences (or Audacity menu > Preferences on macOS).

| Setting path (App > Menu) | Value | Why this value |
|---|---|---|
| Audio Settings > Host | Windows WASAPI | Audacity ships **no native ASIO support** (Steinberg SDK licensing prohibits redistribution in open-source binaries). WASAPI is the lowest-latency Windows host Audacity can use out of the box. ASIO4ALL does not help; the host dropdown never shows ASIO regardless of installed drivers. See Section 8. |
| Audio Settings > Recording Device | In 3-4 (MOTU M Series) | The dedicated 1/4" TRS line inputs on the M4 reserved for the Schiit Mani II vinyl path. **Important:** "Loopback (MOTU M Series)" captures system playback, NOT physical inputs; use "In 3-4 (MOTU M Series)" for vinyl capture. |
| Audio Settings > Playback Device | Out 1-2 (MOTU M Series) | M4 MONITOR outs feeding Rolls MX28 LEVEL 3 BAL > HS7 + LSR310S. |
| Audio Settings > Project Sample Rate | 48000 Hz | Project standard per `CLAUDE.md` SOFTWARE AND DAW. Archive-grade album captures step up to 96 kHz per session. |
| Audio Settings > Default Sample Format | 32-bit float (working) | Working depth for capture and editing; FLAC export drops to 24-bit per project standard. |
| Tracks Behaviors > Solo button | "Multi-track" | Allows multiple tracks soloed simultaneously (useful for A/B comparison during edit pass). |

Companion utility: none. Audacity is self-contained.

---

## 5. Signal Chain / Integration Points

Vinyl-to-FLAC capture chain (active 2026-05-30 onward; AT-VM95SH cartridge installed 2026-02-09):

```
AT-LP120XUSB (PHONO out, AT-VM95SH Shibata cart at 2.0 g VTF)
  > Schiit Mani II (phono preamp, MM mode)
  > MOTU M4 LINE IN 3-4 (USB-C to GDMARCHE; Windows WASAPI host)
  > Audacity 3.7.7 (capture, edit, FLAC export)
```

Output destinations (two-tier archive model locked 2026-05-30):

```
Audacity working files (.aup3 + RAW WAV)
  > D:\The Audiopheliac\Creative Studio\07_Exports\Vinyl Rips\<Artist>\<Album>\_working\
                  Side <A|B> - <RAW|EDIT>.wav

Audacity FLAC export (deliverable)
  > M:\<Artist>\<Album Title> (<Release Year>) - Vinyl Rip (<DDMMMYY>)\
                  NN-Track Title.flac
```

Live ↔ Audacity integration: Ableton Live 12 Settings > File & Folder > Sample Editor = `C:/Program Files/Audacity/Audacity.exe`. Right-click any sample clip in Live > "Manage Sample File" > opens Audacity with that file loaded. After edit + save in Audacity, Live re-reads the file (may require manual reload via "Replace" depending on Live's cache state).

Cross-reference: `config/audiopheliac_signal_map_v_2026_05.md` (Office Studio chain), `CLAUDE.md` SIGNAL CHAIN MAP > Office Studio, `docs/vinyl_capture_reference.md` (full vinyl capture procedure).

---

## 6. Related Automation

| Artifact | Path | Purpose |
|---|---|---|
| Vinyl capture reference | `docs/vinyl_capture_reference.md` | Canonical capture workflow (host, device, levels, edit procedure, export). |
| Vinyl archive metadata pipeline | `docs/vinyl_archive_metadata_pipeline.md` | Metadata-tooling survey (Kid3, Mp3tag, discogstagger, vinyl-recorder, vinylflow). Audacity is the capture stage; metadata tools are downstream of FLAC export. |
| Mentor Lesson 1 (vinyl capture) | `skills/the-mentor/SKILL.md` § Audacity mode | KISS-aligned step-by-step vinyl rip procedure using Audacity. Active scope: Lesson 1. |
| Music library inventory | `docs/Audiopheliac_Music_Library_Inventory_v2026_05.md` | Album-level provenance ledger; vinyl rips logged here on finalization. |

No headless scripts target Audacity; the workflow is interactive. Macro / Nyquist scripting for batch operations is possible but not currently in use.

---

## 7. Troubleshooting Runbook

### Issue: Driver dropdown does not show ASIO option
- **Symptom:** Audio Settings > Host dropdown contains only "MME," "Windows DirectSound," and "Windows WASAPI." No "ASIO" entry, even with MOTU M Series ASIO 4.5.0.551 installed and working in Ableton.
- **Cause:** Stock Audacity has no native ASIO support. Steinberg's ASIO SDK licensing prohibits redistribution of ASIO code in open-source binaries. ASIO4ALL is a virtual driver that wraps WDM, not Audacity-side ASIO.
- **Fix:** Use Windows WASAPI host. WASAPI gives the lowest stock-Audacity latency on Windows.
- **Verification:** Audio meters move when input arrives at the M4. Recorded levels match expectations from the Mani II output gain stage.

### Issue: Captured audio shows only system playback, not the turntable
- **Symptom:** Recorded waveform contains music currently playing through Windows audio (Spotify, browser tabs) instead of vinyl signal.
- **Cause:** Audio Settings > Recording Device is set to "Loopback (MOTU M Series)" instead of a physical input device. Loopback captures system playback by design.
- **Fix:**
  1. Stop the current recording.
  2. Open Edit > Preferences > Audio Settings.
  3. Set Recording Device to "In 3-4 (MOTU M Series)" (physical line inputs).
  4. Apply, close, restart the recording.
- **Verification:** Recorded waveform shows the vinyl signal only; pressing Pause on Spotify mid-test does not stop the captured audio.

### Issue: Recording starts but levels stay at -∞ dBFS
- **Symptom:** Recording is active and clock advances, but the meter shows no signal even though Mani II output should be present.
- **Cause:** Several possible:
  1. M4 LINE IN 3-4 cabling not connected, or RCA-to-TRS adapters absent/faulty.
  2. AT-LP120XUSB PHONO/LINE switch is on LINE (built-in preamp) while Mani II is also amplifying. Double-amplification causes clip or, paradoxically, mute if the path is broken.
  3. Mani II not powered or wrong gain setting for cart (AT-VM95SH is MM; switch on Mani II must be MM, not MC).
  4. Audacity Recording Device pointing to wrong input.
- **Fix (physical layer first per CLAUDE.md Reasoning Protocol):**
  1. Verify AT-LP120XUSB rear switch = PHONO (not LINE). PHONO sends raw cart signal to Mani II.
  2. Verify Mani II power LED is on. Verify gain switch = MM (low gain).
  3. Verify RCA cables Mani II OUT > M4 LINE IN 3-4 are seated.
  4. Verify Audacity Audio Settings > Recording Device = "In 3-4 (MOTU M Series)" and Channels = 2 (stereo).
  5. Play vinyl; meter should show signal.
- **Verification:** Peaks reach approximately -12 dBFS during loud passages (calibration target from the Bowie session).

### Issue: Project file (.aup3) corrupted or fails to open
- **Symptom:** Audacity reports "Could not open project file" or similar on launch.
- **Cause:** Unclean shutdown during active recording, OneDrive sync collision on cloud-synced paths, or disk full.
- **Fix:**
  1. Check for `<projectname>.aup3-shm` and `<projectname>.aup3-wal` files alongside the .aup3. These are SQLite write-ahead-log artifacts; if Audacity crashed mid-write, they hold the last-known state.
  2. Try opening the .aup3 directly; Audacity may recover.
  3. If that fails, restore from D: working-stage backup or restart capture (vinyl rips are reproducible; this is why the Side A / Side B RAW WAVs exist as an independent layer).
- **Verification:** Project opens with tracks intact; waveform displays correctly.

---

## 8. Known Limitations

- **No native ASIO support.** Stock Audacity cannot use ASIO drivers. Use Windows WASAPI for lowest stock-Audacity latency. To get ASIO in Audacity, you would need to build from source with the Steinberg SDK (not legally redistributable; build-yourself only) or use a different DAW for that capture (Ableton, Reaper, etc.). For The Audiopheliac, Ableton handles ASIO-required workflows; Audacity stays on WASAPI for vinyl capture and editing.
- **Single-DAW workflow per session.** Audacity will hold an exclusive WASAPI lock on the M4 while a recording session is open; Ableton cannot share the device until Audacity releases it (or unless Audacity is set to WASAPI shared mode, which raises latency).
- **No multi-track session model like a DAW.** Audacity treats every "track" as a single audio clip; no clip launcher, no automation lanes, no session view. Linear edit only. This is by design (Audacity is an editor, not a DAW).
- **OneDrive sync interactions.** If a project is saved to a cloud-synced path (current Ableton Temporary Folder default puts Live recordings on OneDrive; Audacity should NOT save vinyl-rip projects there), sync churn can lock files mid-write and cause project corruption. Save to local non-synced paths (D: drive) only.

---

## 9. Change Log

| Date | Profile version | Change |
|---|---|---|
| 2026-05-31 | 2026.05.1 | Initial profile. Audacity 3.7.7 captured as the canonical vinyl-to-FLAC capture surface, configured as Ableton Live 12's Sample Editor. WASAPI host (no ASIO; verified via Audacity docs and Mentor obs #11). MOTU M4 In 3-4 as recording device. Two-tier archive model: working WAVs to D: Creative Studio, FLAC deliverables to M:. Troubleshooting runbook covers ASIO absence, loopback-vs-physical-input confusion, silent-recording diagnostic flow (physical layer first), .aup3 recovery. Cross-references to `docs/vinyl_capture_reference.md`, `docs/Audiopheliac_Music_Library_Inventory_v2026_05.md`, and the Mentor skill. |

---

*Profile companion files:*
- *`docs/vinyl_capture_reference.md` — canonical vinyl capture workflow (gear-specific reference).*
- *`docs/vinyl_archive_metadata_pipeline.md` — downstream metadata tooling survey.*
- *`docs/Audiopheliac_Music_Library_Inventory_v2026_05.md` — vinyl rip provenance ledger.*
- *`skills/the-mentor/SKILL.md` § Audacity mode — Mentor Lesson 1 step-by-step procedure.*
- *`docs/software/AbletonLive12.md` — Live profile (covers Sample Editor integration from the Live side).*
