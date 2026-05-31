# GDMARCHE Home Office — Connection Reference (Final)

**The Audiopheliac | Tech Lab** | 2026-05-21 | Version: v3 (supersedes v2 2026-05-12)

---

## Stations

### 1. Dell WD19DCS — GDMARCHE Primary Dock

| Port | Connected To | Cable | Notes |
|---|---|---|---|
| DP1 | Sansui Monitor 1 | DP → HDMI (passive) | HDMI input on Sansui |
| DP2 | Sansui Monitor 2 | DP → HDMI (passive) | HDMI input on Sansui |
| HDMI | VACANT | — | Available — Anker HDMI switch or direct use |
| USB-C | VACANT | — | **Must remain empty — DP alt mode kills HDMI port** |
| USB-A | M-Audio AIR Hub | USB-A → USB-C | Monitoring/DAC interface — being replaced by MOTU M4 (pending arrival) |
| USB-A | MOTU M4 (pending arrival) | USB-A → USB-C | Replacement primary audio interface — will occupy this port on arrival |
| Ethernet | Spectrum puck | Ethernet | Wired LAN — direct to dock |

### 2. Dell Monitor (Older) — Shared Display

Serves both GDMARCHE and the GFE Latitude 5340 via separate inputs. Input switching via monitor OSD menu.

| Monitor Input | Source Device | Cable | Notes |
|---|---|---|---|
| DisplayPort | WD19DCS (GDMARCHE) | DP → DP | Primary GDMARCHE display |
| HDMI | J5 Create JCD543 dock (GFE Latitude 5340) | HDMI → HDMI | GFE display — switch via OSD |

### 3. J5 Create JCD543 — GFE Dock (Dell Latitude 5340)

Operates in full-feature mode when connected to the Latitude 5340 TB4 port. Video, Ethernet, and USB all functional.

**Note (2026-05-21):** The J5 was previously daisy-chained from the WD19DCS USB-A port, operating in degraded mode (USB hub only, no video). That configuration caused issues and has been retired. The J5 is now connected exclusively to the Latitude 5340 TB4 port. Its sole purpose in the current setup is to route the GFE's display to the Dell monitor via HDMI — manual OSD input switching between DP (GDMARCHE/WD19DCS) and HDMI (GFE/J5).

| Port | Connected To | Cable | Notes |
|---|---|---|---|
| Host cable (USB-C) | Dell Latitude 5340 TB4 | Built-in USB-C cable | Full TB4 — video + data + PD active |
| HDMI | Dell monitor HDMI input | HDMI → HDMI | GFE display via monitor OSD switch |
| USB-A ports | Available | — | GFE peripherals as needed |
| Ethernet | Available | — | Can connect to Spectrum puck if needed |
| Power In (USB-C) | J5 power adapter | USB-C | Required for video and PD to function |

### 4. M-Audio AIR Hub — Audio Monitoring Interface (Interim)

Serving as DAC/monitoring output only while MOTU M4 is in transit. Will be replaced by MOTU M4 on arrival; fate TBD (cold spare or sell).

| Port | Connected To | Cable | Notes |
|---|---|---|---|
| Host (USB-C) | WD19DCS USB-A | USB-C → USB-A | Windows sees as audio device |
| 1/4" TRS L+R | Rolls MX28 Input A | 1/4" TRS | Primary monitoring output — output only, no ADC |
| 1/4" Headphone | Headphones | 1/4" | Independent level control |
| USB-A (×3) | LP120 / Spark 40 / Casio Privia | USB-B → USB-A | Powered — requires external PSU |
| Power | AC outlet | External PSU | Required for hub ports to function |

### 4b. MOTU M4 — Primary Audio Interface (Pending Arrival)

Purchased 2026-05-21 from Guitar Center. Replacing Focusrite Scarlett Solo (failed 2026-05-11) and M-Audio AIR Hub as primary interface. Receipt at `P:\Finances\Purchases_and_Receipts\Audio Equipment\MOTU_M4_GuitarCenter.pdf`.

**Why M4:** 4-channel USB-C interface with 2 combo XLR/TRS mic/line inputs (1-2) + 2 dedicated line TRS inputs (3-4). Best ADC at price tier. Inputs 3-4 designed for permanent Schiit Mani II connection (stereo vinyl archiving requires two simultaneous line inputs — Scarlett Solo lacked this). No rewiring for vinyl recording once permanently wired.

| Port | Planned Connection | Cable | Notes |
|---|---|---|---|
| Host (USB-C) | WD19DCS USB-A | USB-C → USB-A | Will replace AIR Hub on this port |
| Input 1 (XLR/TRS combo) | Mic (when purchased) | XLR | Primary vocal/instrument mic input |
| Input 2 (XLR/TRS combo) | Guitar (Epiphone LP / Seagull) | 1/4" TS | Plug/unplug as needed |
| Input 3 (TRS line) | Schiit Mani II L out | RCA-M → TRS-M | Permanent — stereo vinyl L channel |
| Input 4 (TRS line) | Schiit Mani II R out | RCA-M → TRS-M | Permanent — stereo vinyl R channel |
| Output 1+2 (TRS) | Rolls MX28 Input A | 1/4" TRS | Replaces AIR Hub output in signal chain |
| Headphone (1/4") | ATH-M50x | 1/4" | Independent level control |

**Pending setup tasks on arrival:** Install MOTU ASIO driver; reconfigure Ableton Preferences → Audio → Driver Type: MOTU ASIO; purchase RCA-to-TRS adapter pair (Mani II to M4 inputs 3-4); create `docs/software/Motu-M4.md` profile; update CLAUDE.md signal chain map.

### 5. Anker HDMI Switch — Opportunistic Use

Not in primary monitor chain.

- Connected to WD19DCS HDMI port when in use
- Use cases: iPhone display mirroring, guest device, secondary screen as needed
- One-button input switching between connected sources

### 6. Hyper HyperDrive Flex 5-Port USB-C Hub — Lanai / Portable

Not deployed at desk — lanai and portable use only.

- Connects to GDMARCHE or GFE USB-C port when on lanai
- Single monitor support — no DP alt mode conflict risk in portable config
- No external power required

---

## Standing Constraints

1. **WD19DCS USB-C port must remain empty at all times.** Any DP alt mode device on that port disables the dock HDMI port.
2. **J5 is no longer connected to WD19DCS.** Previous daisy-chain from WD19DCS USB-A caused issues and was retired. J5 connects exclusively to the Latitude 5340 TB4 port. Do not reconnect J5 to the Dell Dock.
3. **AIR Hub is DAC / output only** — no recording input. MOTU M4 is the replacement (pending arrival).
4. **MOTU M4 goes to WD19DCS USB-A** on arrival — same port currently occupied by AIR Hub. AIR Hub is removed when M4 is installed; USB-A ports on AIR Hub (LP120, Spark 40, Privia) will need to move to WD19DCS or a hub.
5. **GDMARCHE IP 192.168.1.119, DHCP reservation confirmed 2026-05-05.** The earlier reference to 192.168.1.75 in v2 was stale; CLAUDE.md HARDWARE is the current-state record.

---

## Source

Lab notes captured 2026-05-12. v3 updates (2026-05-21): J5 dock correctly repositioned to GFE-only; MOTU M4 pending-arrival entry added; AIR Hub noted as interim; IP conflict resolved (192.168.1.119 confirmed per CLAUDE.md). Supersedes v2 2026-05-12. Filed by Lena (Studio Assistant, chat); saved by Cowork.

## Cross-reference

- `config/audiopheliac_signal_map_v_2026_05.md` — full signal chain across all zones.
- `docs/av_master_inventory_2026.md` — gear inventory and serials.
- `docs/Dell_Precision_7540_Specs.md` — workstation specs.
- `CLAUDE.md` HARDWARE section — current state of record (IP conflict noted above).
