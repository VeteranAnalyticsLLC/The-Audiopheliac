# Vinyl Capture Reference

**Version:** 2026.05.1
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Purpose:** Canonical gear-specific reference for the Audiopheliac vinyl-to-FLAC capture chain. Load on demand when working in the chain or when the Mentor skill (`skills/the-mentor/SKILL.md`) enters Audacity or Ableton mode. This doc is reference data, NOT operational instructions; for the teaching workflow, see the Mentor skill.

---

## Canonical Capture Chain

```
AT-LP120XUSB
  (PHONO/LINE switch: PHONO, internal phono preamp DISENGAGED)
  (Cartridge: Audio-Technica AT-VM95SH Shibata MM, installed 2026-02-09)
  (Tracking force: 2.0 g per manufacturer spec)
  (LP120 USB-B cable: UNPLUGGED during capture sessions)
    |
    | RCA stereo pair + ground wire to ground post
    |
    v
Schiit Mani II
  (Mode: MM)
  (Gain: calibrated per album by test cut, target ~-12 dBFS peaks)
    |
    | RCA-to-1/4" TRS adapter cables (stereo pair)
    |
    v
MOTU M4
  (Rear TRS inputs 3 and 4; line-level, no preamp stage)
  (Software trim via MOTU M Series Console for inputs 3/4)
  (Driver: MOTU M Series ASIO 4.5.0.551)
  (Firmware: 2.07)
  (USB-C to GDMARCHE)
    |
    v
GDMARCHE
  (Dell Precision 7540, Windows 11)
    |
    v
Audacity (primary)
  - Host: Windows WASAPI
    (Stock Audacity does NOT ship with ASIO support due to Steinberg
     SDK licensing. WASAPI is the correct Audacity host on Windows --
     supports 24-bit recording, exclusive-mode low-latency path, no
     Windows mixer in the signal chain. Reserve MOTU M Series ASIO
     for Ableton Live, which supports ASIO natively.)
  - Recording Device: In 3-4 (MOTU M Series)
    (NOT "Loopback (MOTU M Series)" -- loopback captures system
     playback, not physical inputs. The "In 3-4" entry is the
     physical TRS line inputs where the Mani II is wired.)
  - Playback Device: Out 1-2 (MOTU M Series)
  - Channels: 2 (Stereo) Recording Channels
  - Project Rate: 48000 Hz (daily) or 96000 Hz (archive-grade per album)
  - Project Bit Depth: working in 32-bit float, export to 24-bit FLAC
    |
    v
Raw WAV (preserved indefinitely)
    |
    v
Edit WAV (working stage)
    |
    v
FLAC tracks (deliverable)
    |
    v
D:\The Audiopheliac\Creative Studio\07_Exports\Vinyl Rips\<Artist>\<Album>\
  (Auto-syncs to NAS via QSync)
```

**Monitoring during capture:** MOTU M4 front-panel 1/4" headphone outputs, Audio-Technica ATH-M50x, Direct Monitor ON for zero-latency confidence check.

---

## Cartridge: Audio-Technica AT-VM95SH

**Installed on the AT-LP120XUSB 2026-02-09** (replaced the stock AT95E green-tag MM the deck shipped with).

| Spec | Value |
|---|---|
| Type | Moving Magnet (MM) |
| Stylus | Shibata, 2.7 by 0.26 mil (nude) |
| Recommended tracking force | 2.0 g (range 1.8 to 2.2 g) |
| Cartridge weight | 6.1 g |
| Output | ~3.5 to 4.0 mV at 1 kHz, 5 cm/sec |
| Frequency response | 20 Hz to 25 kHz |
| Channel separation | 25 dB at 1 kHz |
| Replaceable stylus | Yes |
| Upgradeable stylus | No |
| Source | https://www.turntablelab.com/products/audio-technica-at-vm95sh-phono-cartridge-w-shibata-stylus |

**AT-LP120X-specific setup notes:**
- Tracking force is set by rotating the entire counterweight (the gauge ring turns with the weight) counterclockwise until 2.0 g is at the reference line.
- VTA: the AT-LP120X tonearm height adjustment may not let the arm sit perfectly level with a taller-than-stock cart. Community consensus (r/turntables) is that perfectly level is the visual target; small deviations within the adjustment range are acceptable and do not significantly affect sonic performance for an MM Shibata at this price tier.
- Anti-skate: set to match tracking force (2.0).

---

## Phono Preamp: Schiit Mani II

**Office Studio, serial CI182351284, acquired Jul 2025.**

| Spec | Value |
|---|---|
| Type | External phono preamp |
| Cartridge support | MM and MC, switchable |
| Gain | Switchable (multiple stops for matching cart output) |
| Ground post | Dedicated (turntable ground wire connects here) |
| Power | External wall wart (use included PSU only) |

**Setup for AT-VM95SH:**
- Mode: MM
- Gain: start at the middle stop, run a test cut on the loudest track of the album being captured, observe peaks in Audacity. Step one notch up if peaks below -18 dBFS; step one notch down if peaks above -6 dBFS. Target ~-12 dBFS peaks for clean capture with headroom.
- Calibration is per-album because vinyl pressings vary substantially in cut level.

---

## Audio Interface: MOTU M4

**Active primary as of 2026-05-28** (replaces Focusrite Scarlett Solo 4th Gen, RETIRED after failure 2026-05-11).

| Spec | Value |
|---|---|
| Type | USB-C bus-powered audio interface |
| Channels | 4 in / 4 out |
| Bit depth | Up to 24-bit |
| Sample rate | Up to 192 kHz |
| Inputs 1-2 | Combo XLR/TRS with mic preamp + 48V phantom (per-channel switches) |
| Inputs 3-4 | Dedicated 1/4" TRS line-level (no preamp; software trim via M Series Console) |
| Outputs 1-2 (MONITOR) | 1/4" TRS balanced + RCA parallel (TRS active feed to Rolls MX28 LEVEL 3 BAL) |
| Outputs 3-4 (LINE OUT) | 1/4" TRS balanced + RCA parallel (unused; available for tracking-cue or dual-zone monitoring) |
| Headphone outputs | 2x front-panel 1/4" (wired to Outs 3-4 by default; M Series Console can route Outs 1-2 to headphones for main-mix monitoring) |
| Driver | MOTU M Series ASIO 4.5.0.551 + Windows class-compliant |
| Firmware | 2.07 |
| Serial | m4ma0243as |
| Receipt | `P:\Finances\Purchases_and_Receipts\Audio Equipment\MOTU_M4_GuitarCenter.pdf` |

**Vinyl capture wiring (current):**
- Rear inputs 3 and 4 receive the Mani II RCA outputs via RCA-to-1/4" TRS adapter cables (stereo pair).
- Inputs 1/2 are reserved for tracking work (mic, instrument); not used in the vinyl rip path.
- Software trim for inputs 3/4 lives in the MOTU M Series Console application, not the M4 front panel.

**M Series Console initial settings (set 2026-05-28):**
- Sample Rate: 48 kHz
- Buffer Size: 256
- Sync Windows sample rate to device: ON
- Use lowest latency safety offsets: ON (Xeon E-2286M + 112 GB ECC has the headroom; revert if Ableton sessions show audio artifacts under heavy plugin load)

---

## Audacity Reference

**Default project settings for vinyl capture:**

| Setting | Daily | Archive-grade |
|---|---|---|
| Project Rate | 48000 Hz | 96000 Hz |
| Default Sample Format (working) | 32-bit float | 32-bit float |
| Export Bit Depth (FLAC archive) | 24-bit | 24-bit |
| Recording Channels | 2 (Stereo) | 2 (Stereo) |
| Host | Windows WASAPI | Windows WASAPI |
| Recording Device | In 3-4 (MOTU M Series) | In 3-4 (MOTU M Series) |
| Playback Device | Out 1-2 (MOTU M Series) | Out 1-2 (MOTU M Series) |

**Important: Audacity does NOT support ASIO.** Stock Audacity binaries (every official release) lack ASIO support due to Steinberg SDK licensing restrictions on open-source projects. Windows WASAPI is the correct Audacity host on Windows -- supports 24-bit recording, exclusive-mode low-latency path, no Windows mixer in the signal chain. ASIO4ALL (a third-party WDM-to-ASIO wrapper) does NOT help Audacity, because Audacity cannot enumerate ASIO devices at all -- the Host dropdown does not show ASIO regardless of which ASIO drivers are installed on the system. Use MOTU M Series ASIO in Ableton Live, where ASIO support is native and the manufacturer's driver gives the best latency.

**Canonical workflow references (official Audacity Manual, durable URLs):**
- Sample workflow for LP digitization: https://manual.audacityteam.org/man/sample_workflow_for_lp_digitization.html
- Tutorial: Digitizing LPs, tapes or MiniDiscs: https://manual.audacityteam.org/man/tutorial_copying_tapes_lps_or_minidiscs_to_cd.html

**Community references (gotcha-specific):**
- MOTUnation forum, "Getting Started with Motu M4 and Audacity" thread: https://motunation.com/forum/viewtopic.php?t=69330 (documents the M4 inputs 3/4 + Audacity gotcha specifically)
- Audacity Forum, "ripping vinyl at 24bit 96Khz with Audacity": https://forum.audacityteam.org/t/ripping-vinyl-at-24bit-96khz-with-audacity/61548

---

## Archive Destinations — Staging vs Final Library

The vinyl rip workflow has TWO destinations, not one. The staging path holds the working files (project + RAW WAVs). The music library is where finished FLACs live for listening.

### Staging (working files only — .aup3 and RAW WAVs)

**Root:** `D:\The Audiopheliac\Creative Studio\07_Exports\Vinyl Rips\`

**Hierarchy:**

```
07_Exports\Vinyl Rips\
  <Artist>\
    <Album>\
      _working\
        <Artist> - <Album>.aup3
        Side A - RAW.wav
        Side B - RAW.wav
        Side A - EDIT.wav   (optional, if EDIT stage exported)
        Side B - EDIT.wav   (optional)
```

D: syncs to NAS via QSync. Replicated path: `\\NAS87828E\The Audiopheliac\The-Audiopheliac\Creative Studio\07_Exports\Vinyl Rips\` (per CLAUDE.md INFRASTRUCTURE AND SYNC).

**Staging naming:**
- Artist folder: `<Artist Name>` as published (no leading "The").
- Album folder: `<Album Title>` (no year, no rip date — kept simple at the staging level).
- Working WAVs: `Side <A|B> - <RAW|EDIT>.wav` (folder hierarchy carries artist/album context).
- Audacity project: `<Artist> - <Album>.aup3`.

### Final FLAC library (the listening destination)

**Root:** `M:\` (the music library — same root Plex monitors and the Bronco's USB workflows pull from).

**Hierarchy:**

```
M:\
  <Artist>\
    <Album Title> (<Release Year>) - Vinyl Rip (<DDMMMYY rip date>)\
      01-Track Title.flac
      02-Track Title.flac
      ...
```

**Example (locked-in canonical):**

```
M:\David Bowie\Let's Dance (1983) - Vinyl Rip (30MAY26)\
  01-Modern Love.flac
  02-China Girl.flac
  03-Let's Dance.flac
  04-Without You.flac
  05-Ricochet.flac
  06-Criminal World.flac
  07-Cat People (Putting Out Fire).flac
  08-Shake It.flac
```

**Final library naming:**
- Artist folder: `<Artist Name>` as published (no leading "The"). Same convention as staging.
- Album folder: `<Album Title> (<Release Year>) - Vinyl Rip (<DDMMMYY>)`.
  - Release year is the year of the album's original release (1983 for Let's Dance), not the pressing year if a reissue.
  - "Vinyl Rip" tag distinguishes vinyl-source FLACs from CD-source backup FLACs of the same album. This matters because Gill may eventually rip vinyl copies of albums he already has digitized from CDs (e.g., a Tom Petty Wildflowers special-edition vinyl rip alongside the CD backup).
  - DDMMMYY rip date provides provenance and disambiguates if the same album is ever re-ripped (e.g., with better gear in a future session). Trade-off: DDMMMYY is human-readable but does not sort chronologically when listed alphabetically; if chronological sort matters, use ISO 8601 (YYYY-MM-DD) instead.
- FLAC tracks: `NN-Track Title.flac` (two-digit track number, dash separator, song title, .flac extension). The dash separator matches Audacity's default "Numbering before Label/Track Name" export pattern.

**Workflow order:**
1. RAW WAVs and .aup3 project live in the staging `_working\` folder for the life of the rip work and remain there as historical provenance.
2. Final FLACs export INTO the library's album folder directly — NOT into the staging tree.
3. The staging tree is the source-of-truth for "this was rip-engineered in Audacity on these dates with these settings." The library tree is the listening surface.

**Metadata fields on FLAC export:**
- Artist, Album, Title, Track number / total tracks, Year (release year), Genre, Album artist (compilations), Comment.
- Comment template: `Vinyl rip: AT-LP120XUSB / AT-VM95SH / Mani II / MOTU M4 / Audacity / YYYY-MM-DD`.

For tagging tool options beyond Audacity's native metadata editor, see `docs/vinyl_archive_metadata_pipeline.md`.

---

## When to Update This Doc

Update this doc when any of the following change:
- Cart swap (re-document tracking force, mode, gain target).
- Phono preamp change.
- Audio interface change.
- Adapter cable change.
- Driver / firmware version bump.
- Archive destination path change.
- Default sample rate / bit depth change (sync with CLAUDE.md SOFTWARE AND DAW ENVIRONMENT default).
- New canonical reference URL.

Source documents to keep in sync:
- `CLAUDE.md` HARDWARE, SIGNAL CHAIN MAP Office Studio, SOFTWARE AND DAW ENVIRONMENT, OPEN ACTION ITEMS.
- `av_master_inventory_2026.md` (both root and `docs/` copies if both still exist).
- `docs/Audiopheliac_Audio_Source_Inventory_v2026_05.md`.

---

*Reference data. For workflow lessons, see `skills/the-mentor/SKILL.md`.*
