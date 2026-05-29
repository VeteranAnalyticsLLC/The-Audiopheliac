# Audiopheliac Audio Source Inventory v2026.05

**Version:** 2026.05.28.3 (M4 swap — MOTU M4 installed and verified as active primary 2026-05-28; AIR Hub demoted to 30-day cold-spare evaluation through 2026-06-27)
**Owner:** Gillon "Gill" Marchetti
**Purpose:** Canonical inventory of every audio source available to the Cockpit, what zone each can play to, and integration status. This document drives the Cockpit's source-selection UI and the per-zone routing matrix. Failure modes (§11) are the acceptance bar for any source integration.

**Sources used to compile this draft:**
- Direct enumeration of GDMARCHE user-scope filesystem (Start Menu, AppData/Local, AppData/Roaming, AppData/Local/Packages) via Cowork mounts.
- Direct enumeration of NAS qpkg list and `/share/Music` top-level via QNAP File Station + qpkg.conf parse.
- `console/config.json` for currently-wired Cockpit sources.
- `CLAUDE.md` HARDWARE + SIGNAL CHAIN MAP for analog/external inputs per zone.
- Gill's verbal scope statement (this session): MinimServer is being retired; comprehensive source inventory and Cockpit integration is the new focus.

**What Cowork can't reach** (Rafa-lane queries in §12): Windows registry installed-programs list, Windows default audio device + endpoint inventory, running media process state, M-Audio AIR Hub ASIO sample rate / buffer / device-routing state, subscription tier confirmations for Tidal/Apple Music/Plex Pass.

---

## 1. Methodology and Conventions

- **Source** = anything that can produce a stream of audio bits ultimately destined for a zone's speakers.
- **Zone** = listening location with its own endpoint chain. Four active zones today: Office Studio, Family Room, Lanai, Garage (per CLAUDE.md SIGNAL CHAIN MAP).
- **Destination** = the Cockpit's selectable output target. Two today in `config.json`: `studio` (GDMARCHE → AIR Hub → HS7) and `yamaha` (Family Room R-N800A).
- **Integration status:**
  - **Wired** — the Cockpit already routes this source.
  - **Available, not wired** — installed/subscribed but not selectable from Cockpit yet.
  - **Available, retired** — present but slated for removal (MinimServer, Roon footprint).
  - **Confirmation needed** — installed/visible but subscription/active state not verified.

---

## 2. GDMARCHE — Desktop Audio Applications

### 2a. Streaming Clients (desktop apps)

| App | Install Path | Confirmed Subscription | Bit-Perfect Path | Cockpit Integration |
|---|---|---|---|---|
| **Spotify** | MS Store: `SpotifyAB.SpotifyMusic_zpdnekdrzrea0` | Premier (CLAUDE.md) | Custom `Spotify_Bit_Perfect.lnk` shortcut in Start Menu | Wired (Spotify Web API + Spotify Connect to Yamaha) |
| **Plexamp** | `AppData\Local\Plexamp` + `AppData\Roaming\Plexamp` + auto-updater | **Plex Pass status needs Gill confirm** | Native bit-perfect via AIR Hub | Not wired |
| **Plex (desktop player)** | `AppData\Local\Plex` | Plex Pass per Plexamp | Plex client | Not wired |
| **Plex HTPC** | `AppData\Local\Plex HTPC` | (subset of above) | mpv-based | Not wired |
| **Yamaha MusicCast 10** | MS Store: `63231GhostInTheMachine.Musiccast10_4sn0e1cqmjmmy` | n/a (controller, not source) | n/a | Not wired (Cockpit duplicates much of its function) |
| **Amazon Music** | Web/PWA only; not installed as native app | Active free tier (commercial-supported); no Unlimited subscription | Yamaha has built-in Amazon Music source | Not wired (route via Yamaha's Amazon Music input or via browser to AIR Hub) |
| **Pandora** | Web/PWA only; not installed as native app | Active free tier (commercial-supported) | Yamaha has built-in Pandora source | Not wired (route via Yamaha's Pandora input or via browser to AIR Hub) |
| **Suno** | Browser-only via https://suno.com | Premier Annual confirmed (CLAUDE.md) | n/a (creative tool, not playback) | Wired (Library → Suno tab) |

### 2b. Local Playback Engines

| App | Install Path | Role | Cockpit Integration |
|---|---|---|---|
| **VLC** | `AppData\Roaming\vlc` + `C:\Program Files\VideoLAN\VLC\vlc.exe` (per `localplayer.py`) | Primary local-FLAC playback engine for Studio destination | Wired (`localplayer.py` uses VLC for Studio play) |
| **Windows Media Player** | System app | Fallback engine in `localplayer.py` | Wired (fallback if VLC absent) |
| **Audacity** | `AppData\Local\audacity` + `AppData\Roaming\audacity` | Audio editor (with playback) | Not wired — not a streaming target |
| **Ableton Live 12 Lite** | `AppData\Local\Ableton` + `AppData\Roaming\Ableton` | DAW (Suite per CLAUDE.md; could be Lite per file present) | Not wired — DAW, not a Cockpit source |
| **EZ CD Audio Converter** | MS Store: `Poikosoft.EZCDAudioConverterFree_mf0mhss1hhy7w` | CD ripping | Not a source — CD-rip pipeline tool |

### 2c. Multi-instrument / DAW-adjacent

| App | Install Path | Role |
|---|---|---|
| **Native Access** (Native Instruments) | Start Menu shortcut | Plugin / sample library management |
| **inMusic Software Center** | `AppData\Local\inMusicBrands` | Akai / M-Audio driver and software updates |
| **Arobas Music** | `AppData\Local\Arobas Music` + `AppData\Roaming\Arobas Music` | Guitar Pro or similar |

### 2d. Audio Drivers / Interfaces

| Driver | Status | Note |
|---|---|---|
| **MOTU M Series ASIO** | **Active primary as of 2026-05-28** | Driver 4.5.0.551, firmware 2.07, device serial m4ma0243as. 4-channel USB-C 24-bit/192kHz; 2× combo XLR/TRS inputs (mic preamp + 48V phantom), 2× dedicated TRS line inputs, 2× balanced TRS monitor outs, 2× headphone outs. M Series Console: 48 kHz / buffer 256 / lowest-latency-safety-offsets ON / sync-Windows-sample-rate-to-device ON. Detailed per-package profile at `docs/software/Motu-M4.md`. |
| **M-Audio AIR Hub ASIO** | **Cold spare** (30-day evaluation through 2026-06-27) | Output-only, no ADC. Retained on system as known-good fallback while M4 is verified rock-solid. Post-2026-06-27 decision: retire entirely, OR keep as USB-A passthrough hub (its non-audio utility). |
| **ASIO4ALL v2** | Installed | Generic ASIO wrapper for non-ASIO-native apps. Not in primary audio path. |
| **Waves MaxxAudio Pro for Dell** | MS Store: 2 packages installed | DSP layer that may apply EQ/effects on Realtek-bound consumer endpoints. **Does NOT affect MOTU M4 audio path** (USB Audio Class pro interfaces do not surface a Windows Enhancements tab; Waves binds to Realtek endpoints only). Still worth disabling for any system-default-routed audio scenarios. |

### 2e. Residual / Pending Decisions

| Item | Path | Status |
|---|---|---|
| **Plex Media Server (local GDMARCHE install)** | `AppData\Local\Plex Media Server` | Redundant with NAS PMS. NAS PMS has a persistence issue (per Gill). Consolidation decision pending — see §13. |

---

## 3. NAS (QNAP TS-473A, NAS87828E) — Audio-Relevant Apps

Gill's canonical list of NAS audio-related apps (this session):

| App | Version | Status | Purpose | Cockpit Integration |
|---|---|---|---|---|
| **Music Station** (CAYIN) | 5.4.7 | Installed, enabled | QNAP's first-party music app; web UI + UPnP capability | Not wired |
| **CAYIN MediaSign Player** | 3.2.25318 | Installed, enabled | Digital signage player; included by Gill in audio-app set | Not wired |
| **Plex Media Server (NAS)** | 1.42.2 | Installed, enabled, **persistence fix landed 2026-05-27** | Full media server (audio + video). Data relocated to `/share/Plex/Library/` via `PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR` in qpkg start script; survives qpkg restarts and in-place updates. Verified ~12h uptime as of 2026-05-28. | Pending Plexamp + Plex catalog browse wiring per Pass A integration pattern. |
| **Multimedia Console + Media Streaming Add-on (QDMS)** | MMC 2.10.2 / QDMS 500.1.1.11 | Installed, enabled | QNAP's media-stack hub plus the DLNA streaming server (QDMS) | **Not wired — QDMS is the candidate DLNA replacement for MinimServer** |
| **Kazoo Server** (Linn) | n/a | **Available in App Center, NOT installed** | Audiophile UPnP server (Linn). Listed for awareness; install decision pending. | n/a |

### 3b. NAS Music Library (`/share/Music` top-level)

147 folders total. Top-level inventory shows a healthy classic-rock / alt-rock / country / pop catalog plus production artifacts:

- **The Audiopheliac** — Suno output archive (current; modified 2026-05-24)
- **_Archive** — indexer-excluded per `config/music_sources.json`
- **Spotify Downloads** — local-cached Spotify content
- **User Library** — Ableton User Library copy
- A stale top-level folder from a deprecated server remains on disk under `/share/Music/` (admin-owned, not in the active app set). NAS-side housekeeping item — flag for a cleanup pass when convenient; not an Audiopheliac scope item.
- **Various Artists / Compilation / Album Artist** — admin-owned organizational folders
- **Artist folders** (selected examples from top 50): Metallica, Amy Winehouse, Willie Nelson (×2), Chicago, Madonna, Steppenwolf, Allman Brothers (×2), Queen, U2, Alanis Morissette, Phish, Pearl Jam, Weezer, Whitney Houston, Tori Amos, Tom Petty, Smashing Pumpkins, Cure (×2), Beatles, System of a Down, Beach Boys, Stone Temple Pilots, Taylor Swift, Talking Heads, Andrea Bocelli, Rage Against the Machine, R.E.M., Stevie Ray Vaughn, Shania Twain (×2), Savage Garden, Pink Floyd, Pennywise, Parliament, Girls Against Boys, Led Zeppelin, Nirvana, Nine Inch Nails, and more.
- **Folder hygiene note:** several artists have both a clean folder (MarcArmy2003-owned) and a torrent-style admin-owned folder (e.g., `Steppenwolf - Discography 1968-2005 (FLAC) 88`). The indexer treats both as siblings. Worth a curation pass — out of scope today, flagging for follow-up.

### 3c. Out-of-Scope NAS Apps (not audio sources)

Cinema28, QuMagie, VideoStation, and similar QNAP apps are video / photo focused. Out of scope for this inventory; revisited in Pass B (video consumption).

---

## 4. Streaming Subscriptions and Account Status

| Service | Status | Tier | Confirmed By |
|---|---|---|---|
| **Spotify** | Active | Premium, **Lossless enabled, Family plan** | Gill confirmed this session |
| **Suno** | Active | Premier Annual (10K credits/mo, commercial use) | CLAUDE.md PLATFORM CREDENTIALS |
| **Amazon Music** | Active | Free tier (commercial-supported); no Unlimited subscription | Gill confirmed this session |
| **Pandora** | Active | Free tier (commercial-supported) | Gill confirmed this session |
| **Plex Pass** | Active | **Annual subscription** | Gill confirmed this session |
| **Apple TV+** | Active | Subscription | Gill confirmed this session — TV+ (video), not Apple Music. Out of scope for audio inventory. |
| **Discogs** | Active (library/wantlist token, not streaming) | n/a | CLAUDE.md |

---

## 5. Yamaha R-N800A Built-in Streaming Services

The receiver has its own catalog of network sources accessible via YXC and via the front panel / MusicCast app. From CLAUDE.md and `console/config.json`'s `enabled_sources` array, plus the receiver's native firmware:

| Service | Built-In | Subscription Required | Cockpit Integration |
|---|---|---|---|
| **Spotify Connect** | Yes (Yamaha is a Spotify Connect endpoint) | Spotify Premium | Wired (Cockpit's Spotify tab → Connect to R-N800A) |
| **AirPlay 2** | Yes | n/a (Apple device required as source) | Not wired (Cockpit doesn't initiate AirPlay) |
| **Amazon Music** | Yes (native source) | Free tier (Gill's account) | Listed in `enabled_sources` (`amazon_music`) but not yet wired with an Amazon catalog browser. Free tier has commercials. |
| **Pandora** | Yes (native source) | Free tier (Gill's account) | **Not in `enabled_sources` yet — add when wiring.** Free tier has commercials. |
| **Net Radio (vTuner)** | Yes | n/a | Wired (Cockpit Net Radio tab + `net_radio_suggestions` in config.json) |
| **Bluetooth** | Yes | n/a | Listed in `enabled_sources`; selectable as input |
| **MusicCast (multi-zone)** | Yes | n/a | **Not wired** — MusicCast grouping is per System Design but not implemented yet |
| **DLNA/UPnP (Server input)** | Yes | n/a | Migrating to QDMS as the DLNA source (replacement for the deprecated UPnP server) |
| **USB DAC** | Yes | n/a | Listed in `enabled_sources` |
| **Tuner (FM/AM)** | Yes | n/a | Listed in `enabled_sources` |

The R-N800A also exposes Tidal, Deezer, and Qobuz sources in firmware. None of these are active subscriptions; omitted from this inventory.

---

## 6. Per-Zone Analog and External Inputs

From CLAUDE.md SIGNAL CHAIN MAP.

### 6a. Family Room (Yamaha R-N800A as receiver)

| Input | Source |
|---|---|
| Optical In 2 | Samsung TV (Family Room) |
| Line In 1 (Phono) | Pro-Ject Phono Box S2 Ultra ← Technics SL-1200MK2 (Ortofon Blue) |
| Line In 2 | (open / available) |
| Audio 1 | (open / available) |
| Audio 2 | (open / available) |
| PRE OUT | → Rolls MB15b booster → 1Mii TX → wireless to Office Studio RX + Lanai RX |

### 6b. Office Studio (Rolls MX28 Mini-Mix VI as analog mixer)

| Input | Source |
|---|---|
| Input A | GDMARCHE → M-Audio AIR Hub → balanced TRS L/R |
| Input B | AT-LP120XUSB → Schiit Mani II phono preamp |
| Input C | 1Mii RX #1 (wireless from Family Room PRE OUT path) |
| MX28 Master Out | → JBL LSR310S sub → Yamaha HS7 monitors |

### 6c. Lanai (Schiit SYS passive switcher + Bose 3-2-1)

| Input | Source |
|---|---|
| Schiit SYS Input 1 | 1Mii RX #2 (wireless from Family Room) |
| Schiit SYS Input 2 | Singing Machine ISM9033 (karaoke) |
| Bose AUX IN | ← Schiit SYS Output |
| Bose TV 1 In | ← J-Tech JTECH-AE4KA (HDMI eARC from Samsung UN65U7900F) |

### 6d. Garage (Bose SoundTouch Genius + Amazon Echo)

| Input | Source |
|---|---|
| Bose Bluetooth | Phone / device pairing |
| Bose 3.5mm | Phone / device wired |
| Bose Wi-Fi | Yamaha R-N800A Bluetooth (sporadic due to distance) |
| Amazon Echo | Independent BT/Wi-Fi (parallel to Bose) |

---

## 7. Per-Zone Playable Source Matrix (Current and Target)

| Source | Office Studio | Family Room | Lanai | Garage |
|---|---|---|---|---|
| **Local FLAC (NAS via DLNA)** | Yes (via QDMS + Studio destination; or VLC playback on GDMARCHE) | Yes (DLNA to Yamaha Server input) | Indirect (via Family Room → 1Mii wireless) | No (Bluetooth source only) |
| **Spotify Connect (Premium Lossless)** | Yes (Spotify desktop → AIR Hub) | Yes (Spotify Connect to R-N800A) | Indirect (via Family Room → 1Mii) | No |
| **Amazon Music (free tier)** | Yes (browser/app → AIR Hub) | Yes (R-N800A built-in Amazon Music source) | Indirect | Echo (independent path) |
| **Pandora (free tier)** | Yes (browser → AIR Hub) | Yes (R-N800A built-in Pandora source) | Indirect | Echo (independent path) |
| **Plexamp (Plex Pass)** | Yes (Plexamp → AIR Hub) | DLNA out from Plex possible but Plex's NAS persistence issue blocks reliable use today | Indirect | No |
| **Suno** | Yes (browser → AIR Hub) | Yes (browser → AirPlay 2 / Spotify Connect / DLNA from M: drive after publish) | Indirect | No |
| **Net Radio** | Yes (browser stream → AIR Hub) | Yes (R-N800A vTuner) | Indirect | Echo |
| **Vinyl (Technics SL-1200MK2)** | Indirect (Family Room → 1Mii wireless to MX28) | Yes (native; turntable → Phono Box → Yamaha) | Indirect (via 1Mii) | No |
| **Vinyl (AT-LP120XUSB)** | Yes (LP120 → Schiit Mani II → MX28) | No | No | No |
| **TV / video audio (Family Room)** | Indirect (via 1Mii) | Yes (TV Optical → Yamaha) | No | No |
| **TV / video audio (Lanai)** | No | No | Yes (TV eARC → J-Tech → Bose TV 1) | No |
| **Singing Machine (karaoke)** | No | No | Yes (Schiit SYS Input 2 → Bose AUX) | No |
| **MusicCast multi-zone group** | (Future) | (Future) | (Future) | No |
| **Bluetooth from phone** | No (would need bridge) | Yes (Yamaha Bluetooth input) | Yes (Bose Bluetooth) | Yes (Bose Bluetooth) |

---

## 8. Cockpit Currently-Wired Sources (`console/config.json`)

The `enabled_sources` array in `config.json` lists 14 Yamaha-side physical inputs the Cockpit exposes as selectable inputs on the Family Room destination:

```
spotify, amazon_music, airplay, server, bluetooth, tuner,
optical1, optical2, line1, line2, audio1, audio2, usb_dac, phono
```

This is the **Yamaha input selector**, not the broader source catalog. The Cockpit's Library tab separately exposes: Spotify (Web API), Local Files (M: drive browser), MinimServer (retiring), Net Radio, Suno (launcher tab).

**Gap:** the Library tabs don't include Tidal, Apple Music, Amazon Music browse, Plexamp, or QDMS yet. These are the integrations Pass A's source-integration-pattern doc was designed to enable.

---

## 9. Cockpit Destinations (`config.json`)

Currently two:

| ID | Label | Sub | Kind | Engine |
|---|---|---|---|---|
| `studio` | Studio | GDMARCHE → AIR Hub → HS7 | local | VLC (per `localplayer.py`) |
| `yamaha` | Family Room | Yamaha R-N800A | yamaha | YXC + DLNA push |

**Missing for the four-zone model:** Lanai and Garage destinations. These currently route via Family Room (1Mii TX from Yamaha PRE OUT → wireless RX in Lanai and previously Office; Garage is Bluetooth-only). To make them independently selectable, the Cockpit needs explicit destination entries with their own routing logic (likely: Lanai = Family Room with a Lanai-only flag for the wireless tap, Garage = Bluetooth pair handoff). Out of scope for inventory but flagged.

---

## 10. Music Library Locations (Cockpit `local_player.music_roots`)

| Label | Path | Notes |
|---|---|---|
| M: Music Library | `M:\` | UNC: `\\NAS87828E\Music\` (per CLAUDE.md MUSIC LIBRARY section) |
| The Audiopheliac (NAS) | `M:\The Audiopheliac` | Suno output archive |
| Creative Studio | `D:\The Audiopheliac\Creative Studio` | Active production folder |
| Published Masters | `D:\The Audiopheliac\Creative Studio\01_Songs\Published Masters` | Final WAV archives |

---

## 11. Failure Modes (Acceptance Criteria — Gill, this session)

The Cockpit will be considered functionally complete on each integrated source when none of these failure modes occur:

1. **Zone selection fails to play** — A zone is selected but no audio reaches its speakers.
2. **Source selection fails to play** — A streaming, local-library, or analog input is selected but no audio plays from it.
3. **Audio quality loss unrelated to inherent device/app limits** — Bit-depth/sample-rate downsampling, unintended DSP, transcoding to lossy, ground hum, dropouts.
4. **Search broken** — Cannot search by artist, album, or track for any selected source, OR the searched-for track doesn't load and play to the selected zone(s).
5. **Source overlap without mutex** — A newly selected source starts playing without stopping the prior source (two streams playing simultaneously into the same zone).
6. **Any other Cockpit-caused defect** — Code, operations, or design bug not attributable to mechanical or external software issues.

**Architectural note on failure mode #5:** Within the Yamaha (Family Room), only one input is active at a time at the hardware level — selecting a new source automatically displaces the prior. Within the Studio destination, `localplayer.py` stops any prior process before starting a new one. **Gap:** if Spotify Connect is paused (not stopped) at the Yamaha and a local FLAC is then started via DLNA, the Yamaha will switch inputs but Spotify Connect's session remains held open on the receiver. The Cockpit should explicitly issue a Spotify stop/disconnect when switching sources within the same zone. Not blocking but worth fixing.

**Cross-zone failure mode #5:** Two zones playing different things simultaneously is the desired behavior, not a failure. The mutex applies per-zone, not globally.

---

## 12. Rafa-Lane Queries (Windows-side coverage gaps)

Run these on GDMARCHE to fill what Cowork can't reach:

```powershell
# 1. Full installed-programs registry enumeration (machine + user scope)
Get-ItemProperty 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
                  'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
                  'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*' `
  | Where-Object { $_.DisplayName -match 'audio|music|spotify|plex|amazon|pandora|vlc|foobar|ableton|audacity|airfoil|sonarworks|waves|maxx|m-audio|asio|motu|kazoo|minim' } `
  | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate `
  | Sort-Object DisplayName | Format-Table -AutoSize

# 2. Default Windows audio output device + all output endpoints
# Requires AudioDeviceCmdlets module (Install-Module -Name AudioDeviceCmdlets -Force)
# Or via .NET MMDeviceEnumerator:
Add-Type -AssemblyName PresentationCore
$enum = New-Object -ComObject MMDeviceAPI.MMDeviceEnumerator   # may need different approach
# Simpler: use Get-PnpDevice for the sound-device class
Get-PnpDevice -Class 'AudioEndpoint' | Where-Object Status -eq 'OK' |
  Select-Object FriendlyName, Status, Class | Sort-Object FriendlyName | Format-Table -AutoSize
Get-PnpDevice -Class 'MEDIA' | Where-Object Status -eq 'OK' |
  Select-Object FriendlyName, Status, InstanceId | Format-Table -AutoSize

# 3. Running media processes
Get-Process | Where-Object { $_.ProcessName -match 'spotify|plex|amp|amazon|pandora|vlc|foobar|ableton|audacity|wmplayer|firefox|chrome|edge|brave|launch|cockpit|python|musiccast' } |
  Select-Object ProcessName, Id, MainWindowTitle, Path, StartTime |
  Sort-Object ProcessName | Format-Table -AutoSize

# 4. Confirm M-Audio AIR Hub state (device + ASIO sample rate if accessible)
Get-PnpDevice -FriendlyName '*AIR*' | Select-Object FriendlyName, Status, InstanceId | Format-Table -AutoSize
# Sample rate is usually visible in the AIR Hub control panel, not registry; flag if needed.

# 5. Waves MaxxAudio Pro state — is the DSP layer active on the default device?
Get-PnpDevice -FriendlyName '*Waves*' | Select-Object FriendlyName, Status | Format-Table -AutoSize
# Manual: check Settings > System > Sound > Sound Control Panel > Playback > [device] > Properties > Enhancements tab. If MaxxAudio is enabled, disable for bit-perfect monitoring.

# 6. UPnP/DLNA discovery test from GDMARCHE's network segment
# Quick sanity check that QDMS (and other UPnP servers) are visible from where the Cockpit runs.
# PowerShell SSDP M-SEARCH:
$socket = New-Object Net.Sockets.UdpClient
$socket.Client.SetSocketOption([Net.Sockets.SocketOptionLevel]::IP, [Net.Sockets.SocketOptionName]::ReuseAddress, $true)
$ep = New-Object Net.IPEndPoint([Net.IPAddress]::Parse('239.255.255.250'), 1900)
$msg = "M-SEARCH * HTTP/1.1`r`nHOST: 239.255.255.250:1900`r`nMAN: `"ssdp:discover`"`r`nMX: 3`r`nST: urn:schemas-upnp-org:device:MediaServer:1`r`n`r`n"
$bytes = [Text.Encoding]::ASCII.GetBytes($msg)
$socket.Send($bytes, $bytes.Length, $ep) | Out-Null
$socket.Client.ReceiveTimeout = 4000
try {
  while ($true) {
    $remote = New-Object Net.IPEndPoint([Net.IPAddress]::Any, 0)
    $reply = $socket.Receive([ref]$remote)
    Write-Host "FROM $($remote.Address): $([Text.Encoding]::ASCII.GetString($reply))" -ForegroundColor Cyan
    Write-Host '---'
  }
} catch { Write-Host 'SSDP scan window closed' }
$socket.Close()
```

**Expected outputs to capture and paste back:**
- Installed-programs table (filtered).
- Audio endpoint list (so we know what "Studio" output is actually using).
- Running media process list (so we know what's contending for the default output right now).
- UPnP M-SEARCH replies — confirms whether QDMS, Plex, etc. are visible from GDMARCHE's network segment (MinimServer's discovery failure may or may not be specific to it).

---

## 13. Confirmations Needed from Gill

Resolved this session: Tidal (out), iTunes/Apple Music (out), Apple TV+ (video subscription, out of audio scope), Amazon Music (free tier, in), Pandora (free tier, in), Plex Pass (annual, active), Spotify (Premium Lossless, Family).

| Question | Why it matters |
|---|---|
| **Plex on NAS persistence issue** — what's the symptom (settings reset, library scan resets, auth drops, container restarts)? | Decide whether to consolidate to GDMARCHE Plex, fix NAS Plex, or replace with another server for that lane |
| **Plex Media Server consolidation** — keep both NAS and GDMARCHE instances, or pick one? | Reduces redundancy; tied to persistence-issue resolution |
| **Waves MaxxAudio Pro for Dell** — DSP active on default output, or already disabled? | Bit-perfect quality gate; verify before any audio quality complaint surfaces |
| **MusicCast multi-zone grouping** — desired for Cockpit selection, or front-panel-only for now? | Scope for §9 destinations expansion |
| **Lanai destination** — make selectable in Cockpit independently, or keep as tap from Family Room? | Architecture decision for the four-zone Cockpit |
| **Garage destination** — Cockpit-selectable via Yamaha Bluetooth out, or hands-off (phone Bluetooth only)? | Same |
| **Kazoo Server** — install and evaluate, or skip? | Optional audiophile UPnP alternative; QDMS is the default candidate |

---

## 14. Open Decisions Awaiting Inventory Closure

Once §12 (Rafa) and §13 (Gill) are answered:

1. **Pick the DLNA server.** Recommended: QDMS (free, already running). Decision-blocker: UPnP discovery test in §12 #6 confirms QDMS is reachable from GDMARCHE.
2. **Set integration priority.** Likely order based on usage: Spotify (already wired) → Local FLAC via QDMS (replace MinimServer) → Tidal → Net Radio (already wired) → Apple Music → Amazon Music → Plexamp.
3. **Resolve `console/` prototype vs canonical Cockpit migration timing.** Continue patching the Flask prototype, or accelerate the Cloudflare Worker + Astro + MCP-registry build per ADRs.

---

## 15. Document Maintenance

- Append additions / corrections as new subsections rather than rewriting in place.
- Bump version (`v2026.05.x`) on each substantive update.
- Mark retirements with **Retired YYYY-MM-DD** rather than deleting.
- When a source is wired in the Cockpit, update its row in §7 and §8.

---

*Inventory pass 1 complete. Awaiting subscription confirmations from Gill and Rafa-lane Windows queries before moving to integration.*
