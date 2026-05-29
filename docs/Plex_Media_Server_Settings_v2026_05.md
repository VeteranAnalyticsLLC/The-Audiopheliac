# Plex Media Server Settings — Audiopheliac NAS

**Version:** 2026.05.28.1 (initial seed — General + Remote Access + Library locked)
**Owner:** Gillon "Gill" Marchetti
**Server:** The Audiopheliac NAS (qpkg on NAS87828E, `192.168.1.230:32400`)
**machineIdentifier:** `12d7637652860683ab0a2359b39833633a6ce425`
**Plex version at lock:** 1.42.2.10156 (pending qpkg update to latest as of 2026-05-28)
**Data directory:** `/share/Plex/Library/` (Phase 4 persistence fix landed 2026-05-27; env var set in `/share/CACHEDEV1_DATA/.qpkg/PlexMediaServer/plex.sh`)

## Purpose

Locked baseline for Plex settings. Quick reference for realignment if any setting drifts (after qpkg updates, after major Plex application updates, after accidental UI changes). YAML blocks are the authoritative spec; prose paragraphs explain the why.

## How to use this doc

- The YAML block in each section names the locked value for every setting on that Plex settings page.
- Prose below each YAML block explains the rationale and ties to Gill's objectives.
- **[CRITICAL]** tags mark settings that materially affect Gill's stated objectives. Drift on these matters.
- **[ROUTINE]** tags mark settings where Plex defaults are accepted as-is. Drift unlikely to matter.
- **[USER]** tags mark settings whose value depends on a runtime measurement Gill should provide (e.g., upload speed).

## Objective mapping (referenced throughout)

- **O1** — Audiophile listening via Plexamp/Plex desktop (bit-perfect, lossless integrity)
- **O2** — Plex Pass features pay off (sonic analysis, loudness, smart radio, advanced metadata)
- **O3** — Music library auto-updates (Suno tracks landing in `M:\The Audiopheliac\`, new vinyl rips on `/share/Music/`)
- **O4** — Source-of-truth integrity (curated FLAC tags respected, deliberate library curation)
- **O5** — CarPlay / mobile remote listening (Plex CarPlay app from outside the home)
- **O6** — Cockpit integration (Plexamp launcher + catalog browse as additive sources per `Cockpit_Source_Integration_Pattern_v2026_05.md`)
- **O7** — Data persistence (Phase 4 fix; data at `/share/Plex/Library/` survives qpkg restarts and in-place updates)
- **O8** — Bandwidth discipline (don't saturate Spectrum upload during remote streams)

---

## Server: General

```yaml
friendly_name: "The Audiopheliac NAS"
server_claim_status: claimed
claimed_by: gillon.marchetti@gmail.com
server_update_channel: Public
send_crash_reports: ON
push_notifications: ON
debug_logging: OFF
verbose_logging: OFF
```

**Rationale:**

- `friendly_name: "The Audiopheliac NAS"` — **[CRITICAL]** identifiable across multiple Plex servers visible from a single account. Was set to NAS hostname (`NAS87828E`) by the wizard; renamed 2026-05-28.
- `claim status` — **[CRITICAL — O7]** persistent claim is what survives the Phase 4 data relocation. If this ever shows `unclaimed`, something has gone wrong with the env-var-in-init-script persistence; re-claim is recoverable but means the data directory or init script edit got reset.
- `server_update_channel: Public` — **[ROUTINE]** stable release channel. Beta gets newer features faster but introduces stability risk. Public is the right call for a daily-driver.
- `send_crash_reports: ON` — **[ROUTINE]** helps Plex improve. Low privacy concern.
- `push_notifications: ON` — **[CRITICAL — O5, O6]** required for Plexamp mobile features (CarPlay especially) and for future Cockpit integration if it ever uses Plex push events.
- `debug_logging: OFF` — **[ROUTINE]** produces more log volume than necessary for a healthy server. Turn ON temporarily only if actively troubleshooting.
- `verbose_logging: OFF` — **[ROUTINE]** per Plex's own setting description: "only useful to debug specific issues and should only be enabled if requested by support staff." Fills logs fast.

---

## Server: Remote Access

```yaml
remote_access_enabled: ON
manually_specify_public_port: OFF   # Plex auto-assigns; 18033 currently
public_port: 18033                  # captured for reference; Plex picks this, not a setting per se
internet_upload_speed_mbps: <SET BY GILL>   # [USER] enter actual Spectrum upload Mbps
remote_stream_bitrate_limit: "Original (No limit)"
```

**Rationale:**

- `remote_access_enabled: ON` — **[CRITICAL — O5]** required for Plex CarPlay app to reach the home server when Gill is driving. Trade-off: public exposure of `67.8.208.251:18033` adds attack surface (port scans, auth brute force attempts) but Plex auth + Plex Pass account requirement gates actual access. Acceptable given the use case.
- `internet_upload_speed_mbps` — **[CRITICAL — O8]** MUST be set. Without this, Plex assumes unlimited and a CarPlay session can saturate the Spectrum uplink, degrading every other home internet use simultaneously (Zoom, Cockpit if remote, NAS sync, etc.). Spectrum residential typically reports 35-50 Mbps upload; check `speedtest.net` and enter the actual value.
- `remote_stream_bitrate_limit: Original` — **[ROUTINE]** fine for Plexamp/CarPlay since Plexamp streams compressed audio (~320 kbps AAC) regardless of source bitrate. If Gill ever decides to remote-stream video (Plex movies), cap this below upload speed.

---

## Server: Library

```yaml
scan_library_automatically: ON
run_partial_scan_when_changes_detected: ON
include_music_libraries_in_automatic_updates: ON
scan_library_periodically: ON
library_scan_interval: "every 3 hours"   # was "hourly"; reduced to avoid over-scanning
empty_trash_automatically_after_every_scan: ON
allow_media_deletion: OFF
weeks_to_consider_for_continue_watching: 16   # video-only; no music impact
maximum_continue_watching_items: 40            # video-only; no music impact
```

**Rationale:**

- `scan_library_automatically: ON` + `run_partial_scan_when_changes_detected: ON` — **[CRITICAL — O3]** the primary mechanism for picking up new Suno tracks, vinyl rips, and any other files dropped on `/share/Music/` or `M:\The Audiopheliac\`. Partial scan keeps it efficient (only touches changed folders).
- `include_music_libraries_in_automatic_updates: ON` — **[CRITICAL — O3]** Plex defaults this OFF because of a Linux inotify watch-limit concern on resource-constrained installs. QNAP qpkg has the default 65,536 watch limit, far exceeding the 147-album-folder library size. Without this ON, music library does NOT auto-update — Gill would have to trigger manual scans.
- `scan_library_periodically: ON + every 3 hours` — **[ROUTINE]** safety net for any filesystem events that the watch system might miss (NFS shares, edge cases). Was set to hourly which combined with auto-on-change is over-scanning; every 3 hours is the right balance.
- `empty_trash_automatically_after_every_scan: ON` — **[ROUTINE]** keeps the library clean of references to deleted files.
- `allow_media_deletion: OFF` — **[CRITICAL — O4]** Plex's UI delete is a one-click destroy operation against curated 24-bit FLAC vinyl rips and original Suno tracks. Defense in depth: delete via File Station or source, never via Plex client. If a track needs to be removed from the library view without deleting the file, use Plex's "Remove from library" (different from "Delete").
- `weeks_to_consider_for_continue_watching` / `maximum_continue_watching_items` — **[ROUTINE]** video-library settings, no practical effect on music.

---

## Server: Quality

*[Pending review when Gill provides the Quality settings page screenshot.]*

```yaml
# placeholder
local_quality: <TBD>
remote_quality: <TBD>
# etc.
```

---

## Server: Network

*[Pending review when Gill provides the Network settings page screenshot.]*

```yaml
# placeholder
secure_connections: <TBD>
allowed_lan_networks: <TBD>
# etc.
```

---

## Server: Transcoder

*[Pending review when Gill provides the Transcoder settings page screenshot.]*

```yaml
# placeholder
transcoder_quality: <TBD>
transcoder_temporary_directory: <TBD>
# etc.
```

---

## Server: DLNA

*[Pending review when Gill provides the DLNA settings page screenshot. Important for Cockpit integration — DLNA is the path for Plex → Yamaha R-N800A Family Room destination.]*

```yaml
# placeholder
enable_dlna_server: <TBD>
# etc.
```

---

## Server: Languages

*[Pending review when Gill provides the Languages settings page screenshot.]*

---

## Server: Scheduled Tasks

*[Pending review when Gill provides the Scheduled Tasks settings page screenshot. Important — sets the off-peak window for sonic analysis, deep library refresh, etc.]*

```yaml
# placeholder
nightly_task_window_start: <TBD>
nightly_task_window_end: <TBD>
sonic_analysis_in_off_peak_only: <TBD>
# etc.
```

---

## Server: Extras

*[Pending review when Gill provides the Extras settings page screenshot.]*

---

## Manage: Libraries

*[Pending review of the Music library's Advanced settings — see `Phase 5` reminder in Inventory doc §3a. Locked Advanced settings preflight for the Music library:]*

```yaml
music_library:
  name: <TBD>             # Gill decides: "Music" or "The Audiopheliac Library"
  scanner: "Plex Music"
  agent: "Plex Music"
  visibility: "Include in home screen and global search"
  album_sorting: "Newest first"   # or "By name" per Gill preference
  sonic_analysis: ON              # [CRITICAL — O2] core Plex Pass feature; Plexamp depends on this
  prefer_local_metadata: ON       # [CRITICAL — O4] respects curated FLAC tags
  store_track_progress: OFF       # default for music; ON is for audiobooks/long-form
  include_related_content_from_shared_libraries: ON
  artist_bios: ON                 # Plex Pass
  album_reviews_and_critic_ratings: ON   # Plex Pass
  popular_tracks: ON              # Plex Pass; powers radio stations
  find_lyrics: ON                 # Plex Pass
  concerts: ON                    # Plex Pass; rarely useful but low cost
  genres_source: "Embedded Tags"  # [CRITICAL — O4] respects genre-spine curation per Listening Profile
  album_art_source: "Both Plex Music and Local Files"
  album_loudness_analysis: ON     # [CRITICAL — O1, O2] Plex Pass; consistent perceived volume across tracks
  folder_paths:
    - "/share/Music/"   # or "/share/Multimedia/Music/" — same files; Gill picks based on convention
```

---

## Online Media Sources

*[Pending review when Gill provides the page.]*

---

## Authorized Devices

*[Pending review. Note: any device that's been signed into Plex with Gill's account appears here. Periodic cleanup is good hygiene if old devices accumulate.]*

---

## Webhooks

*[Pending review. Could be relevant for Cockpit integration — if Plex events should trigger Cockpit state updates, webhooks are the mechanism.]*

---

## Settings drift / realignment process

When the Plex web UI shows a setting value that doesn't match this doc:

1. Check the doc's locked value and rationale.
2. If the doc is right and Plex has drifted (qpkg update reset something, accidental change), reset the Plex value to match this doc.
3. If Plex is right and the doc is stale (a deliberate change happened in a session that didn't get logged here), update this doc and bump the version number at the top.
4. Either way, note the drift in `docs/daily_log.md` at the next session-close — drift is information worth keeping.

## Revision history

- **2026.05.28.1** — Initial seed. Locked: General page (7 settings), Remote Access page (3 settings), Library page (9 settings). Music library Advanced settings preflight captured as TBD pending Gill's Phase 5 add-library action. Other settings pages (Quality, Network, Transcoder, DLNA, Languages, Scheduled Tasks, Extras, Online Media Sources, Authorized Devices, Webhooks) flagged as pending review.
