---
title: "Ableton Live 12 - DAW Specifications & Reference"
version: "2026.05.30"
author: "Gillon Marchetti | The Audiopheliac"
last_updated: "2026-05-30"
repo_link: "https://github.com/MarcArmy2003/The-Audiopheliac"
description: "Reference sheet for Ableton Live 12 in The Audiopheliac studio environment: editions owned, install paths, default session settings, and the Ableton Live Knowledge connector for in-session production assistance."
status: "Active"
---

# Ableton Live 12 - DAW Specifications & Reference

## Overview

Ableton Live 12 is the primary DAW for The Audiopheliac studio (per `CLAUDE.md` Software and DAW Environment). This document records edition info, install paths, default session settings, and external knowledge resources. License activation keys are stored separately and are not part of this repo (see Section 6).

---

## 1. Editions Owned

| Edition | Use | Notes |
|---------|-----|-------|
| Live 12 Suite (Upgrade) | Primary DAW for studio production | Full Suite via paid upgrade path |
| Live 12 Lite | Secondary / Lite-tier features | Entry-level edition (typically bundled) |

Both editions are tied to Gill's Ableton account at ableton.com.

---

## 2. Install / Runtime Paths

Ableton runtime data lives on D: (the original factory drive on GDMARCHE, retained when C: was upgraded to Samsung 990 PRO NVMe). C: holds the project repo, code, and documentation. D: holds DAW / audio data only, per `CLAUDE.md` Workspace Bindings.

| Resource | Path |
|----------|------|
| DAW data root | `D:\The Audiopheliac\` |
| Cache | `D:\The Audiopheliac\Ableton Cache\` |
| User Library | `D:\The Audiopheliac\Ableton User Library\` |
| QSync replication target on NAS | `\\NAS87828E\The Audiopheliac\The-Audiopheliac\` |

The repo `.gitignore` blocks `Ableton Cache/` and `Ableton Temp/` at any depth, plus `*.asd`, freeze artifacts, and the sample-library extensions. Project code, scripts, and docs are not stored on D:; they live on C: at `C:\Users\gillo\6. The-Audiopheliac\` per `CLAUDE.md`.

---

## 3. Default Session Settings

- Sample rate: 48 kHz (per `CLAUDE.md` Software and DAW Environment)
- Bit depth: 24-bit
- Audio interface: MOTU M4 (MOTU M Series ASIO 4.5.0.551, firmware 2.07; simultaneous WDM + ASIO supported; replaces the failed Focusrite Scarlett Solo as of 2026-05-28)
- Monitoring: Yamaha HS7 (pair) + JBL LSR310S subwoofer (via Rolls MX28 LEVEL 3 BAL from M4 MONITOR Outs 1-2 TRS)
- Headphone monitoring: MOTU M4 front-panel headphone outputs (wired to Out 3-4 by default; M Series Console can route Out 1-2 mix to headphones for monitoring the main mix); Rolls MX28 headphone output reserved for multi-source blended monitoring

---

## 4. Studio Signal Path Into Live

```
AT-LP120XUSB (phono out RCA)
  > Schiit Mani II (phono preamp, MM mode)
  > MOTU M4 LINE IN 3-4 (USB-C to GDMARCHE; M Series ASIO)
  > Ableton Live 12

Ableton playback:
  Ableton Live 12
    > MOTU M4 MONITOR Outs 1-2 (TRS balanced)
    > Rolls MX28 Mini-Mix VI (LEVEL 3 BAL)
    > Yamaha HS7 + JBL LSR310S
```

INPUT MONITOR MIX (front-panel knob on the M4) stays toward PLAYBACK for daily listening and toward INPUT or blended for live zero-latency tracking. Full chain reference: `CLAUDE.md` Signal Chain Map - Office Studio.

---

## 5. Ableton Live Knowledge Connector (claude.ai)

An Ableton-specific knowledge connector is available at the claude.ai account level for in-session production assistance.

| Field | Value |
|-------|-------|
| Connector name | Ableton Live Knowledge |
| Directory URL | https://claude.ai/directory/connectors/ant.dir.gh.ableton.ableton-knowledge |
| Source coverage | Ableton Live manual + Learn Live tutorial library |
| Reference site | https://www.ableton.com/en/live/learn-live/ |
| Status | Connected (claude.ai account level, 2026-05-05) |
| Authentication | Ableton account (used at connect time) |

### When to use it

Engage the connector during creative sessions when authoritative Ableton documentation would clarify or accelerate the work. Typical fits:

- DAW workflow (routing, automation, racks, MIDI tools, Max for Live)
- Effect / instrument device behavior (parameters, defaults, edge cases)
- Performance and CPU optimization (buffer, ASIO guard, freeze/flatten)
- Mixing and mastering chains where stock device specifics matter
- Music production technique that maps to Live 12 stock devices
- Audio engineering questions where Ableton's official docs are the source of truth

For non-Ableton engineering or production questions (signal chain hardware, gain staging across analog gear, room acoustics), the connector is not required. Default to the studio's own docs in `docs/` and the canonical signal map.

### When not to use it

The connector is scoped to Ableton-published material. It is not a general music-production reference, not a hardware reference, and not a substitute for `docs/av_master_inventory_2026.md`, `docs/Processing_Hardware.md`, or the signal map. Do not pull it in for questions those sources answer authoritatively.

---

## 6. Activation Keys (Reference Only)

License keys are sensitive and are not stored in this repo. The `.gitignore` blocks `keys/`, `**/Keys/`, `Software_and_Keys.md`, `Software_Licenses.md`, `*_Licenses.md`, `*_License_Keys.md`, `*.lic`, `*.license` at any depth.

Single source of truth (local, never committed): `C:\Users\gillo\Keys\Audiopheliac_Software_Licenses.md`. No project-side copies exist; secrets live in one place to avoid divergence.

---

## 7. Cross-References

- `CLAUDE.md` (Software and DAW Environment, Signal Chain Map - Studio, Reasoning Protocol, Mode Contracts)
- `docs/av_master_inventory_2026.md` (Studio gear: MOTU M4, Yamaha HS7, JBL LSR310S, Casio Privia PX-870)
- `docs/Processing_Hardware.md` (Yamaha R-N800A and processing gear specs)
- `docs/Dell_Precision_7540_Specs.md` (Workstation hosting Live 12)
- `docs/instrument_specs_v_2025_10_08.md` (References Live 12 in DAW chain examples)

---

## 8. Maintenance Notes

- If editions change (upgrade path, new license, edition swap), update both this sheet and the master/project license registries.
- If install paths move (off D: or to a different subfolder under `D:\The Audiopheliac\`), update Section 2 and the gitignore rules for `Ableton Cache/` and `Ableton Temp/`.
- Any change to default session settings (sample rate, bit depth, interface) belongs both here and in `CLAUDE.md` Software and DAW Environment.
