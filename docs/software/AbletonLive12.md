# Software Package Configuration Profile - Ableton Live 12

**Package:** Ableton Live 12 Suite (Upgrade) + Live 12 Lite + Beat Tools
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Profile version:** 2026.05.1
**Last reviewed:** 2026-05-31
**Status:** Active

> Per-package configuration, settings, and troubleshooting profile for The Audiopheliac. Companion to `docs/Ableton_Live_12_Specs.md` (high-level spec) and `docs/Ableton_Live_12_Settings_Setup/` (settings snapshot with screenshots + YAML). This file is the day-to-day operations source of truth for Live 12 on GDMARCHE.

---

## 1. Overview

Ableton Live 12 is the primary DAW for The Audiopheliac. It serves three roles: (1) the destination DAW for vinyl-rip workflow (capture in Audacity, finalize in Live; or capture directly in Live once the input chain is wired); (2) the production environment for Suno-staged song builds, vocal recording, and final mix/master; (3) the lesson surface for the Mentor mode "vinyl capture in Ableton Live" lesson currently in progress. Cross-reference: `docs/av_master_inventory_2026.md` (workstation + MOTU M4), `config/audiopheliac_signal_map_v_2026_05.md` (Office Studio chain), `docs/vinyl_capture_reference.md` (Audacity-first vinyl workflow), `skills/the-mentor/SKILL.md` (lesson plan).

---

## 2. Installation

| Field | Value |
|---|---|
| Install source | Ableton account download (vendor MSI) |
| Install path | `C:\ProgramData\Ableton\Live 12 Suite\` (per Live 12 Demo Set KB article; verify with Live > Help > About) |
| Vendor version (last verified) | 12.4.1 on 2026-05-31 (auto-updated from 12.3.4 during Mentor Lesson 2 mid-session) |
| Installer size | 4.4 GB (Windows 64-bit) |
| Auto-update | On (Settings > Licenses & Updates > Get Automatic Updates = Always) |
| License / subscription | Perpetual licenses: Live 12 Suite (Upgrade), Live 12 Lite, Beat Tools |
| Auth email | gillon.marchetti@gmail.com |
| Hardware code (GDMARCHE) | `2104-13A8-C8CB-0228-57C1-E13B` |
| Last online authorization | 2026-05-31, 5:02 a.m. (Windows device) |
| Offline authorization file (cold copy) | `E:\Authorize_2104-13A8-C8CB-0228-57C1-E13B.auz` |

---

## 3. Account / Credentials

| Field | Value |
|---|---|
| Account email | gillon.marchetti@gmail.com |
| Account URL | https://www.ableton.com/en/account/ |
| MFA enabled | Verify in Ableton account settings (unconfirmed in this profile) |
| Support contact | https://help.ableton.com (Knowledge Base) / Ableton account messaging |

**Serial numbers (Live 12 Suite Upgrade, Live 12 Lite, Beat Tools) are NOT stored in this repo.** They live at `C:\Users\gillo\Keys\Audiopheliac_Software_Licenses.md` per the `.gitignore` rules in `docs/Ableton_Live_12_Specs.md` Section 6. Re-download installers from the Ableton account page if a fresh install is needed; serials can be retrieved from the same Licenses & Packs page or the local Keys file.

Knowledge connector at the claude.ai account level: "Ableton Live Knowledge" (covers manual + Learn Live tutorial library; connected 2026-05-05). See `docs/Ableton_Live_12_Specs.md` Section 5.

---

## 4. Configuration

Full settings snapshot lives at `docs/Ableton_Live_12_Settings_Setup/` (human-readable Reference markdown + machine-readable YAML + 9 PNG screenshots of each Settings tab). That folder is the canonical settings record. The summary below highlights only the settings that matter operationally; defer to the reference doc for the full inventory.

| Setting path | Value | Why this value |
|---|---|---|
| Settings > Audio > Driver Type | MME/DirectX (Lesson 2 target: switch to ASIO) | ASIO required for bit-perfect low-latency tracking; current MME/DirectX gives 256 ms overall latency, fine for playback but high for tracking. Switching to ASIO and selecting MOTU M Series ASIO 4.5.0.551 is the active configuration step in Mentor Lesson 2. |
| Settings > Audio > In/Out Sample Rate | 48000 Hz | Project standard per `CLAUDE.md` SOFTWARE AND DAW. Archive-grade album captures step up to 96 kHz / 24-bit per session. |
| Settings > Record, Warp & Launch > File Type | WAV | Lossless capture default. |
| Settings > Record, Warp & Launch > Bit Depth | 24 | Project standard. |
| Settings > File & Folder > Sample Editor | `C:/Program Files/Audacity/Audacity.exe` | Right-click a sample in Live > "Manage Sample File" path opens it in Audacity. Tightens the Live ↔ Audacity workflow for vinyl-rip cleanup. See `docs/software/Audacity.md`. |
| Settings > File & Folder > Temporary Folder | `C:/Users/gillo/OneDrive/Documents/Ableton/Live Recordings` | Cloud-synced path. **Flag:** sync churn and lock contention risk during active recording. Relocate to a local non-synced path before heavy recording sessions. |
| Settings > File & Folder > Cache Folder | `D:\Ableton Cache` | On D: drive per `CLAUDE.md` Workspace Bindings (DAW data lives on D:). |
| Settings > Library > Location of User Library | `M:\The Audiopheliac\User Library` | NAS path. Available only when M: is mapped at Live launch. Verify mapping (`net use`) before treating as broken. |
| Settings > Plug-Ins > VST2 Custom Folder | `D:\VSTs\VST2` (not available in snapshot) | Folder does not exist; create if/when third-party VST2 plugins are installed. |
| Settings > Plug-Ins > VST3 Custom Folder | `D:\VSTs\VST3` (not available in snapshot) | Same as above; VST3 system folders are On so factory VST3s still load. |
| Settings > Plug-Ins > Use VST3 Plug-In System Folders | On | Factory-path VST3s load regardless of custom-folder state. |
| Settings > Theme & Colors > Theme | Immaterial | Live 12's clean low-contrast dark theme. |
| Settings > Display & Input > Allow Sleep Mode | Off | Prevents Windows from sleeping during open sessions. |

---

## 5. Signal Chain / Integration Points

Active Office Studio chain (post-MOTU-M4 install 2026-05-28):

```
AT-LP120XUSB (phono RCA out)
  > Schiit Mani II (phono preamp, MM mode)
  > MOTU M4 LINE IN 3-4 (USB-C to GDMARCHE; MOTU M Series ASIO)
  > Ableton Live 12

Ableton playback:
  Ableton Live 12
    > MOTU M4 MONITOR Outs 1-2 (TRS balanced)
    > Rolls MX28 Mini-Mix VI (LEVEL 3 BAL)
    > Yamaha HS7 + JBL LSR310S
```

Live monitoring uses MOTU M4 front-panel INPUT MONITOR MIX knob: toward PLAYBACK for daily listening, blend or INPUT for live zero-latency tracking. Full signal map in `config/audiopheliac_signal_map_v_2026_05.md` and `CLAUDE.md` SIGNAL CHAIN MAP > Office Studio.

Data-pipeline integrations:
- **Audacity** as Sample Editor (right-click sample > opens in Audacity). See `docs/software/Audacity.md`.
- **Suno** as upstream songwriting/arrangement source. Suno-generated stems land in `M:\The Audiopheliac\` and `D:\The Audiopheliac\Creative Studio\01_Songs\`. Ableton imports for final mix/master. See `CLAUDE.md` SUNO PRODUCTION ENVIRONMENT.
- **MinimServer** (NAS UPnP/DLNA) for browse-and-play reference listening of library FLAC during arrangement decisions.

---

## 6. Related Automation

| Artifact | Path | Purpose |
|---|---|---|
| Mentor lesson skill | `skills/the-mentor/SKILL.md` | Lesson 2 (vinyl capture in Ableton Live) authority. KISS-aligned step delivery. |
| Vinyl capture reference | `docs/vinyl_capture_reference.md` | Gear-specific reference for the canonical capture chain (AT-VM95SH spec, Mani II config, M4 input map, adapter requirements, default rates, canonical Audacity Manual links). |
| Settings snapshot | `docs/Ableton_Live_12_Settings_Setup/` | Full settings reference (markdown + YAML + 9 PNG screenshots). Maintained as a captured baseline; recapture when meaningful settings change. |
| Spec doc | `docs/Ableton_Live_12_Specs.md` | DAW spec doc (editions, install paths, default session settings, Ableton Live Knowledge connector pointer). |

No project automation scripts target Live directly. Live is interactive; the upstream `automation/spotify_*` scripts feed library data that informs production decisions but do not script Live itself.

---

## 7. Troubleshooting Runbook

### Issue: "Visual C++ Redistributable must be updated before Live can continue auto-updating"
- **Symptom:** Banner at the bottom of Live's main window with `Update Now` / `Remind me later` buttons. Live runs normally but auto-update is paused until resolved.
- **Cause:** Live's auto-updater requires a newer Microsoft Visual C++ Redistributable (Windows shared runtime library) than what's currently installed on GDMARCHE.
- **Fix:**
  1. Save any open Live Set work first.
  2. Click `Update Now`. Windows runs the VC++ installer.
  3. Restart Live when prompted.
- **Verification:** The banner is gone; Live > Help > Check for Updates (or auto-update) runs without complaint.
- **References:** https://help.ableton.com/hc/en-us/articles/209775785-Troubleshooting-Live-Installer-Issues-Windows

### Issue: "There is an automatic update of Live currently in progress" dialog on launch
- **Symptom:** Modal dialog when launching Live, blocking session start.
- **Cause:** Live's auto-updater is still downloading or installing a newer version in the background.
- **Fix:**
  1. Click `OK` to dismiss the dialog.
  2. Wait 30 seconds to a few minutes.
  3. Re-launch Live.
- **Verification:** Live opens cleanly into a session.

### Issue: Driver Type stuck on MME/DirectX after MOTU M4 install
- **Symptom:** High overall latency (256 ms in snapshot), live monitoring through Live feels delayed.
- **Cause:** Live defaults to MME/DirectX driver type; switching to ASIO requires manual change after installing a new interface driver.
- **Fix:**
  1. Open Settings > Audio.
  2. Change Driver Type from MME/DirectX to ASIO.
  3. Set Audio Device to MOTU M Series ASIO (4.5.0.551).
  4. Set Buffer Size to 256 or 512 samples (per project standard).
- **Verification:** Overall latency drops to a single-digit or low-double-digit ms reading. Audio device shows "MOTU M Series ASIO" only (no separate input/output device dropdowns).

### Issue: User Library path shows "not available"
- **Symptom:** Settings > Library > Location of User Library = `M:\The Audiopheliac\User Library` shows greyed/not-available.
- **Cause:** M: drive (NAS share `\\NAS87828E\Music`) is not mapped at Live launch.
- **Fix:**
  1. Open File Explorer.
  2. Verify M: is mapped (right-click > "This PC" should show M: under Network Locations).
  3. If absent, re-map with `net use M: "\\NAS87828E\Music" /persistent:yes` (per `CLAUDE.md` Default scripting language: PowerShell).
  4. Restart Live or click Browse and re-point to the User Library path.
- **Verification:** User Library content appears under the Library section in Live's browser sidebar.

---

## 8. Known Limitations

- **No native demo set browser.** Per Ableton KB ([Location of the default Demo Set](https://help.ableton.com/hc/en-us/articles/209774005-Location-of-the-default-Demo-Set)), the Demo Set is the Live Set Live opens on first launch. It lives at `C:\ProgramData\Ableton\Live 12 Suite\Resources\Core Library\Lessons\Demo Songs` on Windows. Not exposed as a discrete "Open Demo Set" menu item; access by browsing to the path or via the Live > Help View interactive lessons.
- **MIDI Tools (Philip Meyer) and similar third-party Max for Live packs** require Live 12 Suite (Max for Live) to function. Live 12 Lite or Live 12 Standard cannot load them.
- **Splice integration** requires an active Splice account beyond what comes bundled with the Live license.
- **Cloud-synced Temporary Folder** (current default: OneDrive) introduces sync-churn risk during active recording. Plan a move to a local non-synced path before heavy recording.

---

## 9. Change Log

| Date | Profile version | Change |
|---|---|---|
| 2026-05-31 | 2026.05.1 | Initial profile. Captures Live 12 Suite (Upgrade) + Lite + Beat Tools licensure on GDMARCHE, version 12.4.1 (auto-updated from 12.3.4 during Mentor Lesson 2), settings cross-references to `docs/Ableton_Live_12_Settings_Setup/`, signal chain, troubleshooting runbook for VC++ Redistributable + auto-update-in-progress + driver-type-mismatch + User Library NAS dependency, available Pack catalog (Section 10). Hardware code recorded; serial numbers held at `C:\Users\gillo\Keys\Audiopheliac_Software_Licenses.md` per repo gitignore rules. |

---

## 10. Available Packs (Live 12 Suite license)

Packs available to redownload via Live's browser ("Packs" label) or the Ableton account Licenses & Packs page. Pack files (when downloaded) install to `D:\Ableton Packs\` per Settings > Library > Installation Folder for Packs (currently marked "not available" because the folder does not yet exist on D:; create it before bulk downloading).

**Inventory captured 2026-05-31. Re-verify against the Ableton account when adding to this list.**

### Ableton-authored packs

| Pack | Size | URL |
|---|---|---|
| Building Max Devices | 43.6 MB | https://www.ableton.com/en/packs/building-max-devices/ |
| CV Tools | 15.5 MB | https://www.ableton.com/en/packs/cv-tools/ |
| Chop and Swing | 587.3 MB | https://www.ableton.com/en/packs/chop-and-swing/ |
| Convolution Reverb | 301.1 MB | https://www.ableton.com/en/packs/convolution-reverb/ |
| Creative Extensions | 14.0 MB | https://www.ableton.com/en/packs/creative-extensions/ |
| Drive and Glow | 625.0 MB | https://www.ableton.com/en/packs/drive-and-glow/ |
| Drone Lab | 4,717.6 MB | https://www.ableton.com/en/packs/drone-lab/ |
| Drum Booth | 1,106.7 MB | https://www.ableton.com/en/packs/drum-booth/ |
| Drum Essentials | 203.4 MB | https://www.ableton.com/en/packs/drum-essentials/ |
| Electric Keyboards | 3,085.1 MB | https://www.ableton.com/en/packs/electric-keyboards/ |
| Expressive Chords | 3.2 MB | https://www.ableton.com/en/packs/expressive-chords/ |
| Glitch and Wash | 883.3 MB | https://www.ableton.com/en/packs/glitch-and-wash/ |
| Granulator III | 127.6 MB | https://www.ableton.com/en/packs/granulator-iii/ |
| Lost and Found | 1,379.4 MB | https://www.ableton.com/en/packs/lost-and-found/ |
| Microtuner | 5.7 MB | https://www.ableton.com/en/packs/microtuner/ |
| Mood Reel | 2,544.1 MB | https://www.ableton.com/en/packs/mood-reel/ |
| Orchestral Brass | 1,490.7 MB | https://www.ableton.com/en/packs/orchestral-brass/ |
| Orchestral Mallets | 1,285.6 MB | https://www.ableton.com/en/packs/orchestral-percussion/ |
| Orchestral Strings | 2,796.9 MB | https://www.ableton.com/en/packs/orchestral-strings/ |
| Orchestral Woodwinds | 4,676.0 MB | https://www.ableton.com/en/packs/orchestral-woodwinds/ |
| Punch and Tilt | 397.4 MB | https://www.ableton.com/en/packs/punch-and-tilt/ |
| Sequencers | 30.0 MB | https://www.ableton.com/en/packs/sequencers/ |
| Session Drums Club | 2,277.1 MB | https://www.ableton.com/en/packs/session-drums-club/ |
| Session Drums Studio | 3,102.3 MB | https://www.ableton.com/en/packs/session-drums-studio/ |
| Skitter and Step | 575.4 MB | https://www.ableton.com/en/packs/skitter-and-step/ |
| Surround Panner | 0.54 MB | https://www.ableton.com/en/packs/surround-panner/ |
| Synth Essentials | 445.3 MB | https://www.ableton.com/en/packs/synth-essentials/ |
| Voice Box | 278.8 MB | https://www.ableton.com/en/packs/voice-box/ |

### Third-party packs (bundled in license)

| Pack | Author | Size | URL |
|---|---|---|---|
| Brass Quartet | Spitfire Audio | 256.6 MB | https://www.ableton.com/en/packs/brass-quartet/ |
| Generators by Iftah | Iftah | 1.4 MB | https://www.ableton.com/en/packs/generators-by-iftah/ |
| Grand Piano | e-instruments | 705.6 MB | https://www.ableton.com/en/packs/grand-piano/ |
| Guitar and Bass | e-instruments | 495.7 MB | https://www.ableton.com/en/packs/guitar-and-bass/ |
| Inspired by Nature | Dillon Bastan | 60.2 MB | https://www.ableton.com/en/packs/inspired-nature/ |
| MIDI Tools | Philip Meyer | 2.4 MB | https://www.ableton.com/en/packs/midi-tools/ |
| Performance Pack | Iftah | 10.0 MB | https://www.ableton.com/en/packs/performance-pack/ |
| PitchLoop89 | Robert Henke (Monolake) | 1.6 MB | https://www.ableton.com/en/packs/pitchloop89/ |
| String Quartet | Spitfire Audio | 481.8 MB | https://www.ableton.com/en/packs/string-quartet/ |
| Trap Drums | Sound Oracle | 65.1 MB | https://www.ableton.com/en/packs/trap-drums/ |
| Upright Piano | Spitfire Audio | 427.7 MB | https://www.ableton.com/en/packs/upright-piano/ |

**Total catalog: 39 packs.** Approximate total size (Ableton-authored + third-party): ~33 GB. Download selectively; not all packs are relevant to The Audiopheliac's listening / production profile (country, classic rock, blues-rock, selective hip-hop and pop).

### Priority recommendations for The Audiopheliac's production profile

Aligned to the Listening Profile (CLAUDE.md): bass-conscious, classic / blues / country spine, vocal-foreground, home hi-fi reward.

| Priority | Pack | Reason |
|---|---|---|
| High | Convolution Reverb | Foundational reverb for any mix work. Audiophile-grade impulse responses. |
| High | Session Drums Studio | Real-recorded drum samples (rock / pop production foundation). |
| High | Grand Piano (e-instruments) | Quality acoustic piano for any song with keys. |
| High | Guitar and Bass (e-instruments) | DI alternatives for the rhythm spine when recording the Epiphone or Seagull is overkill. |
| Medium | Electric Keyboards | Vintage keys palette (Rhodes, Wurlitzer, etc.) for soul / country crossover. |
| Medium | Drum Booth | Additional drum kit variety. |
| Medium | Upright Piano (Spitfire) | Alternative piano character (more intimate than the Grand). |
| Low | Synth Essentials | Foundational synth library; useful for production breadth but not core to the listening spine. |
| Low | Orchestral Strings | Reserved for the rare cinematic moment in a country / rock production. |
| Skip (for now) | Drone Lab, Glitch and Wash, Orchestral Woodwinds, Mood Reel | Out of genre spine; large downloads with low return. |

Total "High" downloads: ~4.6 GB. Total "Medium" additions: ~3.9 GB. Both fit comfortably on D: drive.

---

*Profile companion files:*
- *`docs/Ableton_Live_12_Specs.md` — DAW spec doc (editions, install paths, knowledge connector).*
- *`docs/Ableton_Live_12_Settings_Setup/` — full settings snapshot (markdown + YAML + 9 PNG screenshots).*
- *`docs/vinyl_capture_reference.md` — vinyl rip workflow reference.*
- *`docs/documentation/live12-manual-en.pdf` / `.txt` — official Ableton Live 12 manual.*
