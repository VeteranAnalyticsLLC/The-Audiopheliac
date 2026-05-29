# Software Package Configuration Profile — MOTU M4

**Package:** MOTU M4 (USB audio interface) + MOTU M Series driver
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Profile version:** 2026.05.1
**Last reviewed:** 2026-05-28
**Status:** Active

> Per-package configuration, settings, and troubleshooting profile for The Audiopheliac. Installed and verified 2026-05-28 as the active primary audio interface, replacing the M-Audio AIR Hub (now in 30-day cold-spare evaluation through 2026-06-27).

---

## 1. Overview

The MOTU M4 is the GDMARCHE Office Studio audio interface. It bridges the Windows audio subsystem to the analog monitoring chain (Rolls MX28 → JBL LSR310S → Yamaha HS7) and provides 2 channels of low-noise mic/instrument input for tracking through Ableton Live 12. Replaces the AIR Hub (output-only, 24-bit/96kHz) with full I/O at 24-bit/192kHz plus mic preamps with 48V phantom on inputs 1-2. Driver: MOTU M Series ASIO + Windows class-compliant. Cross-reference: `docs/av_master_inventory_2026.md`, `config/audiopheliac_signal_map_v_2026_05.md`.

---

## 2. Installation

| Field | Value |
|---|---|
| Install source | https://motu.com/en-us/products/m-series/m4/getting-started/ (Windows installer) |
| Install path | `C:\Program Files\MOTU\M Series\` (default; not changed) |
| Vendor version (last verified) | Driver 4.5.0.551 on 2026-05-28 |
| Firmware (last verified) | 2.07 on 2026-05-28 |
| Auto-update | Off — manual via motu.com installer when needed |
| License / subscription | One-time hardware purchase (Guitar Center, 2026-05-21; arrived 2026-05-28); receipt at `P:\Finances\Purchases_and_Receipts\Audio Equipment\MOTU_M4_GuitarCenter.pdf` |
| Auth email | N/A (driver does not require account) |

### Hardware identifiers

| Field | Value |
|---|---|
| Device model | MOTU M4 |
| Device serial | m4ma0243as |
| UPC | 839128 006126 |
| USB connection | USB-C bus-powered; connected to GDMARCHE chassis-direct USB-A port via included USB-C-to-USB-A cable (not through WD19DCS dock — chassis-direct for lowest-jitter primary path) |

---

## 3. Account / Credentials

N/A. The M4 + M Series driver do not require an account. Vendor account at motu.com is optional (used for software downloads and warranty registration); not required for daily operation.

---

## 4. Configuration

### MOTU M Series control panel (auto-opens on hardware connect by default)

| Setting | Value | Why |
|---|---|---|
| Open this window when hardware is connected | ON | Convenience; surfaces config on each cold-boot |
| Sample Rate (Hz) | 48000 | Audiopheliac project default per CLAUDE.md SOFTWARE; ASIO/WASAPI Exclusive apps (Ableton, Plexamp) switch to source-native rates as needed |
| Buffer Size (Samples) | 256 | ~5.3 ms one-way at 48 kHz. Balanced default for playback + light tracking. Bump to 512+ for plugin-heavy Ableton; drop to 128 only for tight tracking-monitoring needs |
| Use lowest latency safety offsets | ON | Enabled 2026-05-28 — Xeon E-2286M + 112 GB ECC has the headroom to run without safety margin. Revert to OFF if audible artifacts (clicks, pops, glitches) appear during heavy Ableton plugin loads |
| Sync Windows sample rate to device | ON | Critical for bit-perfect — when Plexamp engages WASAPI Exclusive at 44.1, Windows follows the M4 instead of forcing a mismatch |

### Windows Sound Control Panel — Out 1-2 (MOTU M Series) Properties

| Tab > Setting | Value | Why |
|---|---|---|
| Levels > Volume | 100 | Full digital; M4 MONITOR knob handles analog attenuation, no double-attenuation |
| Levels > Mute | OFF | — |
| Advanced > Default Format | 2 channel, 24 bit, 48000 Hz (Studio Quality) | Shared-mode format; ASIO/WASAPI Exclusive apps bypass this |
| Advanced > Allow applications to take exclusive control | ON | Required for Plexamp WASAPI Exclusive bit-perfect playback |
| Advanced > Give exclusive mode applications priority | ON | Required so Plexamp/Ableton sessions aren't interrupted by system sounds |
| Spatial sound > Format | Off | Stereo bit-perfect; no surround virtualization |
| Enhancements tab | N/A | The M4 is a USB Audio Class pro interface; Windows does not surface an Enhancements tab for this device class. Waves MaxxAudio Pro for Dell binds to Realtek-class endpoints, not to third-party USB audio paths — the M4 output is unaffected by Waves regardless of system-wide Waves state |

### Front-panel hardware controls (default daily-driver positions)

| Control | Position | Why |
|---|---|---|
| MONITOR knob (large) | Set per listening level; daily 11-1 o'clock typical | Master analog attenuation to monitor outs + headphones |
| INPUT/PLAYBACK MIX knob | Full PLAYBACK | Daily listening — only hear DAW playback through monitors. Blend toward INPUT for live tracking-monitoring |
| 3-4 button (monitoring) | OFF | Don't include inputs 3-4 in front-panel monitor mix unless actively using them |
| MON button (Input 1) | OFF | Let DAW route input monitoring; only ON for zero-latency hardware monitoring without a DAW |
| MON button (Input 2) | OFF | Same |
| 48V phantom (Input 1) | OFF | Only ON when condenser mic is plugged in; phantom into ribbon mics can damage them |
| 48V phantom (Input 2) | OFF | Same |
| Input source selector (MIC/LINE/GUITAR) | Set per source | MIC for XLR condenser/dynamic; LINE for keyboards, synths, line-level gear; GUITAR for instrument-level DI |

### Default Windows audio device assignments

- **Default Playback Device:** Out 1-2 (MOTU M Series) — verified 2026-05-28
- **Default Recording Device:** In 1-2 (MOTU M Series) — verified 2026-05-28

### Other MOTU outputs/inputs visible in Windows

| Endpoint | Status | Purpose |
|---|---|---|
| Out 1-2 | Default Device | Main monitor path → MX28 LEVEL 3 BAL |
| Out 3-4 | Ready | Hardware-routed to front-panel headphone jacks. Used for separate headphone cue mix when needed |
| In 1-2 | Default Recording Device | Mic preamp + 48V XLR inputs (combo XLR/TRS jacks) |
| In 3-4 | Ready | Dedicated line inputs (no preamp). Reserved for Schiit Mani II vinyl rip path once RCA-M → TRS-M adapter pair arrives |
| Loopback | Ready | MOTU loopback captures Out 1-2 as a recording source; useful for streaming/recording desktop audio. Not in active use |

---

## 5. Signal Chain / Integration Points

```
GDMARCHE (Spotify / Plexamp / streaming / DAW)
  > MOTU M4 (USB-C bus-powered; 24-bit/192kHz)
  > MONITOR Outs 1-2 (1/4" TRS balanced)
  > Rolls MX28 Mini-Mix VI (LEVEL 3 BAL)
  > MX28 Master Out (1/4" TRS balanced)
  > JBL LSR310S subwoofer + Yamaha HS7 monitors (parallel)
```

Cross-reference: full Office Studio signal chain in `CLAUDE.md §SIGNAL CHAIN MAP` and `config/audiopheliac_signal_map_v_2026_05.md`. Hardware inventory in `docs/av_master_inventory_2026.md`. Cockpit "Studio" destination references this chain in `console/config.json`.

### Future pending integrations (open action items in CLAUDE.md)

- **Vinyl rip path:** AT-LP120XUSB → Schiit Mani II → RCA-M → TRS-M adapter pair → M4 LINE IN 3-4 → Ableton Live 12 → published WAV at `D:\The Audiopheliac\Creative Studio\01_Songs\Published Masters\`. Blocked on adapter purchase.
- **Ableton Audio Preferences reconfig:** ASIO driver MOTU M Series, audio device MOTU M4, sample rate 48 kHz, buffer 256, input channels 1-4 enabled, output channels 1-4 enabled.
- **Plexamp Audio settings reconfig:** Output device MOTU M Series, WASAPI Exclusive ON, Resample OFF / Match Source, Bit Depth Match Source, Gapless ON.

---

## 6. Related Automation

| Artifact | Path | Purpose |
|---|---|---|
| `console/localplayer.py` | `C:\Users\gillo\6. The-Audiopheliac\console\localplayer.py` | Cockpit's Studio-destination playback engine (VLC); inherits Windows default audio device, which routes to the M4 |
| `console/config.json` Studio destination | `C:\Users\gillo\6. The-Audiopheliac\console\config.json` | `"sub": "GDMARCHE → MOTU M4 → HS7"` (updated 2026-05-28) |

---

## 7. Troubleshooting Runbook

### Issue: M4 not appearing in Device Manager after USB connection

- **Symptom:** Connected M4 via USB; no MOTU M Series entry in Device Manager → Sound, video and game controllers; no MOTU device in Windows Sound Settings dropdown.
- **Cause:** Either (a) MOTU driver not installed before first connection (Windows enumerated as generic USB Audio Class device and bound to the wrong driver), or (b) USB port unstable / dock-mediated connection failing.
- **Fix:**
  1. Disconnect M4
  2. Device Manager → uninstall any "USB Audio Device" or partially-bound MOTU entry
  3. Ensure MOTU M Series driver is installed (Settings → Apps → Installed apps → search for "MOTU")
  4. If absent, reinstall driver from `https://motu.com/en-us/products/m-series/m4/getting-started/`
  5. Reboot
  6. Reconnect M4 to chassis-direct USB-A port (avoid the WD19DCS dock for the first connection)
- **Verification:** Device Manager → Sound, video and game controllers shows "MOTU M Series" with no warning icon; MOTU M Series control panel auto-opens; Windows Sound Settings dropdown lists Out 1-2 and In 1-2 (MOTU M Series).

### Issue: Audio plays but no sound at HS7 monitors

- **Symptom:** Windows reports audio playing to MOTU M Series; M4 front-panel OUT meters (1, 2) show signal; HS7 monitors silent.
- **Cause:** Downstream wiring or gain staging. Check in this order: physical wiring → MX28 LEVEL 3 BAL knob → MX28 MASTER LEVEL knob → HS7 input level → HS7 power.
- **Fix:**
  1. Verify TRS cables run M4 MONITOR Out 1 (L) → MX28 LEVEL 3 BAL L, M4 MONITOR Out 2 (R) → MX28 LEVEL 3 BAL R. NOT M4 LINE OUT 3-4 TRS (one TRS pair to the left of MONITOR on the rear panel).
  2. Ramp M4 MONITOR knob clockwise from zero; OUT meters should respond
  3. MX28 LEVEL 3 to 12 o'clock; MASTER LEVEL slowly up from low
  4. Confirm HS7 power switches ON, rear-panel input level controls at marked unity
- **Verification:** Audio reaches both HS7 monitors at comfortable listening level.

### Issue: Audible clicks/pops/glitches during Ableton sessions

- **Symptom:** Audio artifacts during Ableton playback or mixing, especially with many plugins active.
- **Cause:** Buffer underruns. Lowest-latency-safety-offsets setting is active and CPU/IO can't deliver audio frames on time under load.
- **Fix:**
  1. MOTU M Series control panel → uncheck "Use lowest latency safety offsets" → close
  2. Or: bump Ableton buffer size (Preferences → Audio → Buffer Size) to 512 or 1024
- **Verification:** Artifacts stop; playback clean during heavy plugin sessions.

### Issue: Bit-perfect playback fails (Spotify/Plexamp resampling to 48 kHz instead of source-native 44.1)

- **Symptom:** Spotify Lossless or Plexamp at 44.1 source material plays at 48 kHz on the M4 instead of switching the device to source rate.
- **Cause:** "Sync Windows sample rate to device" disabled in M Series control panel, OR WASAPI Exclusive disabled in Plexamp.
- **Fix:**
  1. M Series control panel → confirm "Sync Windows sample rate to device" is ON
  2. Plexamp Settings → Audio → confirm "Use exclusive mode (WASAPI Exclusive)" is ON
- **Verification:** Watch M Series control panel sample rate field while playing a 44.1 source via Plexamp — should switch from 48000 to 44100 when playback starts.

---

## 8. Known Limitations

- **No Enhancements tab in Windows Sound Control Panel.** USB Audio Class pro audio interfaces do not surface the Windows Enhancements tab. The Waves MaxxAudio Pro for Dell DSP concern (bit-perfect quality gate) does not apply to the M4 path — Waves binds to Realtek consumer endpoints only.
- **Driver install must precede first USB connection.** If the M4 is plugged in before the MOTU M Series driver is installed, Windows binds to the generic USB Audio Class driver and the MOTU driver install can end up in an inconsistent state. Recovery requires uninstalling the wrongly-bound device and reconnecting after MOTU driver install.
- **Bus-powered USB-C device.** No external power supply. Requires sufficient USB bus power; some dock or hub configurations may not deliver enough. Chassis-direct USB-A on GDMARCHE is the verified-stable connection.
- **Outputs 3-4 hardware-wired to front-panel headphone jacks.** Cannot independently route Out 3-4 to separate line-level monitor pair without using the rear-panel LINE OUT 3-4 TRS jacks (which mirror Out 3-4).
- **Inputs 3-4 are line-level only (no preamp).** Mic or instrument signals require Inputs 1-2 (combo XLR/TRS with mic preamp + 48V phantom).
- **Phantom power switches are per-channel.** Cannot globally toggle 48V; must remember to disable per-channel before plugging in ribbon mics.

---

## 9. Change Log

| Date | Profile version | Change |
|---|---|---|
| 2026-05-28 | 2026.05.1 | Initial profile. M4 installed and verified active primary same day. AIR Hub demoted to 30-day cold-spare evaluation through 2026-06-27. |

---

*Template version 2026.05.1 (from `docs/software/_TEMPLATE.md`).*
