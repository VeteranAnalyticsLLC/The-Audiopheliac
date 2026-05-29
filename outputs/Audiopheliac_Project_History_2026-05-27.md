# The Audiopheliac — Chronological Project History

**Compiled:** 2026-05-27 (Session 3)
**Sources:** full git log, `docs/daily_log.md`, CLAUDE.md HISTORY, Slack `#theaudiopheliac`, `_dev/04_progress/` session-close summaries, on-disk artifact inventory.
**Scope:** From repository genesis (2025-09-12) through current state (2026-05-22 last commit). Vibe-coded evolution, narrative rather than PM artifact.

---

## Phase 0 — Vinyl Repo Genesis (September 2025)

The Audiopheliac began life as a vinyl-tracking GitHub repo. The first commit (`a4e261d`, 2025-09-12) was the initial scaffold; the next ten days were almost entirely vinyl inventory work (`vinyl_inventory.md`, `vinyl_inventory.csv`, `vinyl_entry_template.md`). The vinyl catalog was the original product. Network and gear documentation arrived alongside it before the end of September (`AV_Network_Master_List`, `Dell_Precision_7540_Specs`, `device_network.md`, `block_diagram.md`) — the home AV system as the second pillar.

Late September added the first persona/instruction layer: `Repeated_Instructions_Addendum`, `EdNet_Personality`, `EdNet_Knowledge_Comms`. These were the seeds of what later became the CLAUDE.md behavioral contract. "EdNet" was an early Claude-persona experiment; deleted on the October cleanup (`558b787`, `a007896`).

## Phase 1 — Signal Mapping and Inventory Discipline (October–November 2025)

October locked in the Studio instrument profile (`instrument_specs_v_2025_10_08.md`) and the first canonical signal map (`Audiopheliac_Signal_Sync_Map.md`, `6bb5fe9` on 2025-10-14). The training_prompt framework went through three versions in October (`v1.0` → `v1.3`); this was a precursor to the formal global instruction framework that landed later.

November introduced the audio system playbook (`audio_system_playbook.md`, `95af5ca` 2025-11-20) — the long-form prose document covering the Office Studio signal chain that survives today as canonical reference reading. The first proper logo asset landed the same day (`The_Audiopheliac_Primary_Logo_GPT.jpg`, the canonical mark that's still the locked primary today).

A PowerShell export SOP joined in mid-November (`powershell_export_sop`). Vinyl and gear wishlists got a strategic-curation overlay (`82054ea` "Enhance Vinyl and Gear Wish List with strategies", `bdcb507`).

## Phase 2 — Automation Scripting Begins (December 2025)

December was the first executable-tooling month. The Focusrite Sample Rate Switcher script (`17b3e6d`, 2025-12-17) and its content-aware refinement (`9ca0707`) shipped the first PowerShell automation. GPU specifications got added to the Dell Precision profile.

Late December cleaned up accumulated cruft (`8ed6f37` through `01d90e1` — bulk deletions of stale signal-sync map, training prompt, device_network, block_diagram, av_master_inventory_28OCT25). The signal/architecture artifacts had outgrown their original homes; the housekeeping pass cleared the way for the new comprehensive `av_master_inventory_2026.md` (`461aedb`, 2026-01-16) and the `Audiopheliac_Signal_Map_v_2026_01.md`.

The Global Instruction Framework v2.0 (`794da71`, 2025-12-23) was the first version of what would later become the modal/persona discipline now lived in CLAUDE.md (Analyst / Technical / Studio / Strategic modes).

## Phase 3 — Inventory Modernization (January–February 2026)

January 2026 brought the consolidated AV master inventory through several versions (`2026.03` → `2026.04`), the family room network topology diagram, and the lanai signal config Python (`lanai_signal_config.py`, 2026-01-10). The Guitar Literacy branch was initialized and then deliberately retired (`f5b0ab6`, `4931815`–`fad2e8d` later removed the orphaned tree) — an off-scope experiment that proved Guitar Literacy belonged elsewhere, not inside The Audiopheliac.

A 2025 vinyl-collection-entries push spread across multiple commits in mid-January (batches 1 through 9). The vinyl_master got several formal versions; `vinyl_master_v_2026_01_full.md` arrived 2026-01-19. The wishlist got its first "curation rules" overlay — the discipline still applied today.

February added Jethro Tull *Aqualung* to the collection (`bdd76ac`), upgraded the wishlist to `v2026.02`, and revised compilation exceptions and collection value details. A long pause followed; February 3 to April 2 saw essentially no commits.

## Phase 4 — CLAUDE.md Era Begins (April 5–21, 2026)

April 5, 2026 was inflection: the first CLAUDE.md committed (`3688efb`). The repo now had a formal behavioral contract for Claude Code. Cross-surface architecture was added the same day (`0083b61`). The persona framework that began as `EdNet` six months earlier was now codified.

April 19 was the explosive build day. In one evening:

- Production `.gitignore` for audio + dev (`6335756`)
- Music automation scaffold + sources config (`cf7f47f`)
- Music library indexer scaffold + fixes (`ee4f059`)
- Spotify library pull script (`880e702`)
- Spotify-to-local matching script (`d60f7e5`)
- Initial static website scaffold (`27beae3`)

The data pipeline (`music_indexer.py` → `library_index.json` → `spotify_pull.py` → `spotify_library.json` → `spotify_local_match.py` → `spotify_local_matches.json` → `spotify_gap_report.py` → `spotify_missing_tracks.txt`) that's still the canonical pipeline today was sketched in those six commits.

April 20 consolidated everything into the `docs/` canonical structure (`a0602c9`), added the canonical project docs, cleaned the .gitignore, and added the Spotify gap reporting tool. The Phase 1 brand layer locked the same day (`1dbc5ee` — "brand: lock Phase 1 tokens, favicon set, and rainbow-spectrum branding kit"). This is where the original spectrum/rainbow visual identity entered the repo.

April 21 added the `_dev/` working directory plus the LLM-ready voice guidelines (`0ff2ced`), relocated brand assets into Astro's `public/` convention, initialized the Astro TypeScript scaffold (`92584b3`), and added BaseLayout + SiteHeader + five page stubs (`4e5178c`). The Cloudflare Pages target was now wired.

`theaudiopheliac.com` domain was registered 2026-04-19 (through 2028-04-19) — `Audiopheliac_Domain_Registration.md` documents the registration record.

## Phase 5 — Nashville Midnight Pivot (May 2–11, 2026)

May 2 attempted a brand pivot: the Nashville Midnight palette (cream + bronze + steel + indigo + midnight) plus brand voice guidelines v2 (`653de97`). The thesis was a sit-by-the-fireplace, listening-room-on-vinyl emotional palette. The pivot included a CLAUDE.md update to v2026.04 Cowork format (`2eb2161`), a site README + Suno account reference, and a final .gitignore harden.

`b532187` (2026-05-05) consolidated CLAUDE.md to v2026.05 — merging the Suno branch with the Nashville Midnight palette adoption.

May 5 was a Suno identity day. Six rapid commits set:
- Suno display name to "The Audiopheliac"
- Audiopheliac motto locked
- Suno profile bio v1.0
- Spotify username corrected to MarcArmy2003, display name to The Audiopheliac
- Suno handle to `@audiopheliac` (the current handle)
- My Taste v1.1 saved and marked complete

`cb84e69` (same day) scaffolded the "Between Stations" album project — the first album project structure in the repo.

May 9 was a Cockpit-design day. `7512768` shipped the first Cockpit design + converter eval + mockup; the indexer got an `_Archive/` exclusion rule (`2f5332b`); the COMMUNICATION DISCIPLINE section landed in CLAUDE.md as `v2026.05.1` (`297739a`). Lena (Studio Assistant on chat) was removed from the production workflow chain (`0bc05a0`) — Cowork + Rafa became the explicit lane discipline.

## Phase 6 — Hardware Reality Check (May 11, 2026)

The Focusrite Scarlett Solo 4th Gen failed (no signal, fried) on 2026-05-11. CLAUDE.md was updated to mark Solo as failed and promote the M-Audio AIR Hub (output-only, no ADC, 24-bit/96kHz, 2× balanced TRS) to primary monitoring interface (`ea2b0db`). The signal map was reconciled across two more commits (`1b3a489`, `dbce735`) to add the MX28 to Studio, activate the 1Mii TX/RX system, retire SVS SoundPath to storage, and move 1Mii RX #2 from Garage to Lanai. The Schiit pair got disambiguated (`3b9a171`): Mani II stays as LP120 phono preamp in Studio; SYS moved to Lanai as 1Mii/karaoke A/B switch.

The same day introduced the `docs/software/` per-package configuration profile pattern (`50cc264`) — seeded with `Spotify.md` as the first profile, template at `_TEMPLATE.md`, convention at `README.md`. The Audiopheliac was now a scope-as-lifestyle-brand build (`e741d7f`): explicit behavioral rule "Do not collapse Audiopheliac scope to solo/hobby framing." Audiopheliac Paperclip Reference doc copied in and scoped down.

Same evening: Cockpit v0.2 shipped (`a7fcd4c`) — YXC for Yamaha controls + Roon Server in Docker on QNAP for library/zones/transport. The first time the prototype had a real library substrate.

## Phase 7 — Full Spectrum Restoration (May 12, 2026)

The Nashville Midnight pivot was walked back overnight. The brand rework session locked Full Spectrum as the primary palette (the original Phase 1 rainbow restored under a new name), with Nashville Midnight archived to `_dev/99_archive/nashville_midnight_sub_brand/` as a possible future classic-audiophile sub-brand. The canonical mark was reaffirmed as the existing raster JPEG at `assets/The_Audiopheliac_Primary_Logo_GPT.jpg` — not the code-driven SVG approximation. Brand voice guidelines `v3.0` codified dual register (manifesto + direct). The audience sharpened: DIY-creative middle-class enthusiast, not credentialed audiophile.

`d162f22` shipped brand v3.0 + Cockpit v0.4 + Roon zone lock. Seven Roon zone names were standardized: `Family Room — Yamaha`, `— Bose`, `— Shield`, `— TV`, `Studio · AIR HUB`, `Lanai - TV`, `Master Bedroom`. Cockpit `preferred_zones` filter locked to the four room prefixes.

`1de3b4d` (same evening, 21:00) shipped Cockpit v0.6 with unified rebuild + Codex audit fixes — CSRF guard, server-side Spotify OAuth, dependency-health bootstrap endpoint, topbar dependency pills.

Yamaha R-N800A got its DHCP reservation (192.168.1.191, MAC 54:B7:BD:9F:AC:18). Lena's GDMARCHE Home Office Connections doc landed at `docs/GDMARCHE_HomeOffice_Connections_v2026_05.md`.

## Phase 8 — Cockpit Rapid Iteration (May 13–14, 2026)

May 13 was a single-day Cockpit dev sprint. Eight commits over twelve hours:

- `b92a363` — Single-trigger launcher + field-test fixes + architecture docs
- `c783646` — v0.6 polish, Codex audit, packaged-app launcher, v0.7 draft
- `bb2df9b` — v0.7 final ship: Full Spectrum layout, per-zone volume, library tabs, Up Next queue
- `9208d80` — HISTORY entry documenting the v0.7 ship
- `7060077` — Fix roon.py APPINFO website, launch.pyw Bridge binary path, CLAUDE.md binary paths (AIR Hub-zone ghost-rebind fix landed today after Scarlett's output descriptor went stale)
- `fed615f` — Static-cache disable + v0.7 cache-bust + `/api/roon/clear-auth` endpoint + Reconnect UI

Same day: Creative Studio scaffold built on D: drive (independent peer of repo mirror), Robocopy strike from `/MIR` to `/E /XO` to remove wipe risk, Audiopheliac_NightlySync scheduled task moved to SYSTEM run account.

May 14 was the Cockpit "polish then strip" day. Morning: cockpit mockup implementation, Cockpit microcopy pass (brand-voice v3 alignment), homepage redesign with two-column hero and spectrum bars (`ef938ac`). Mid-day: task-observer meta-skill installed (`f02e493`, upstream CC BY 4.0 from rebelytics.com). Afternoon: Cockpit v0.8 shipped (`71da0b7`) — config presets, 5 Roon tabs, Spotify queue in Up Next. Then late afternoon: Cockpit v0.9 (`2dad9ca`) — strip Roon, rebuild UI on Spotify + YXC. Final evening: v0.9.1, v0.9.2 (album browsing, MinimServer DLNA, responsive layout, 4-section search), PWA conversion, LAN binding, Suno launcher tab, launch.pyw bind-host fix.

Seven Cockpit version bumps in 36 hours. End-of-day state: Cockpit was a PWA at `127.0.0.1:5000` + `192.168.1.120:5000`, four library sources, Roon zones, Spotify search/queue, MinimServer DLNA browse.

## Phase 9 — Charter and Reorientation (May 18, 2026)

May 18 was a four-act day. Act 1: hybrid logging charter adopted. Every session-close now dual-writes to Slack `#theaudiopheliac` AND `docs/daily_log.md` (`4ae6e7d`), with line-count verification on the daily_log append. Paperclip deprecated and stripped from active workflow. Roon deprecated (trial cancelled before auto-renew $149.88/yr) and MinimServer promoted back to primary.

Act 2: Cockpit Phase A+B shipped (`4d9ba2e`). v0.9 Spotify + YXC refactor went into main. Roon plumbing pulled. Production bug fixed in `launch.pyw` (singleton anchor was checking for `preferred_zones` field that v0.9 had dropped; Windows SO_REUSEADDR was masking the bind collision so every shortcut click silently spawned a second Flask).

Act 3: Cockpit Phase E shipped (`12d55bb`). Direct DLNA MinimServer integration. New 740-line `console/minimserver.py` (stdlib + requests, no new deps): SSDP discovery, ContentDirectory:Browse + :Search, AVTransport:SetAVTransportURI + Play. New `/api/miniserver/*` routes. Verified end-to-end by Rafa: 520 albums / 6719 items / 148 playlists indexed; Oasis "Hello" played through the Yamaha from MinimServer. Four defects caught and fixed in flight.

Act 4 — the hard stop. Gill called a halt after I (Cowork) shipped three commits against a guessed product model ("the Cockpit is a Spotify+Yamaha+MinimServer remote, the Yamaha is the canonical destination") without ever opening `docs/Cockpit_System_Design_v2026_05.md` or `docs/Cockpit_Architecture_Decisions_v2026_05.md`. The canonical product is much larger: four zones, multiple playback protocols, MusicCast grouping, Hue lighting, LLM agent over MCP registry, listening history viz. Phase D4 UX work was reverted and the session ended on a CLAUDE.md restructure (`d008247`) introducing the new §CANONICAL PRODUCT REFERENCES section, the SESSION-INIT requirement to read System Design + ADR every session, three new behavioral rules (Scope contract, Ambient assumption check, "console/ is a prototype not the product"), and a new §CROSS-PROJECT SCOPE BOUNDARIES section codifying the Lab/Audiopheliac Plex split.

## Phase 10 — Pass A Pattern Doc + Task-Observer Hardening (May 19–22, 2026)

May 19 (Session 2): restart session triggered by a Plex integration hand-off from the Lab. I framed the Plex question as multiple-choice substrate ("MinimServer-only vs hybrid vs Plex Amp vs unified Plex"). Gill corrected: integrations are additive, not substitutive. Second product-model error in two sessions. Two-move discipline now in place via auto-memory: `feedback-canonical-doc-first-for-cockpit` (read the spec) plus `feedback-cockpit-is-additive-not-substitutive` (default to additive).

Pass A shipped as `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` — 12 sections, ~2400 words. Defines the integration contract every source satisfies (health, browse, search, play-to-zone, transport, state, metadata), MCP-server pattern (canonical) + Flask-shim pattern (prototype) with `console/` migration path, per-source UI surface, per-zone routing matrix grounded in the current SIGNAL CHAIN MAP, Plex/Plex Amp as first concrete instance, source-of-record pattern for overlapping sources, eight open questions for Gill. Studio mode scope expanded to three lanes (audio production + visual editing + AI video integration) mid-draft when Gill flagged that pass C is multi-disciplinary.

Pattern doc was drafted but the Rafa commit prompt was never run — pattern doc and the Session 2 daily_log entry remain untracked in the working tree.

May 22 (latest commit): task-observer hardening (`1fc8631`). Added mandatory pre-flight gate and Step 0 in SESSION-INIT requiring `task-observer` skill invocation as the first call of every session-init.

## Phase 11 — Where We Are Today (2026-05-27, this session)

Session 3 opened with:

- 3 carry-forward classes from Session 2: Phase D4 working-tree changes from Session 1 still uncommitted (revert recommended); Session 2 pattern doc untracked; CLAUDE.md §CANONICAL PRODUCT REFERENCES needs the pattern doc added once Gill reviews it.
- Skill-observation review 14 days stale (last review 2026-05-13).
- Eight open questions in pattern doc §10 awaiting resolution.
- 8 modified files in working tree, 12 untracked items.
- Session 3 first action: this history doc.

---

## What Lives in the Repo Today

**Canonical product references (required reading at session-init):**

- `docs/Cockpit_System_Design_v2026_05.md` — four-zone Cockpit spec
- `docs/Cockpit_Architecture_Decisions_v2026_05.md` — five ADRs
- `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` — Pass A integration contract (untracked)
- `brand-voice-guidelines-v3.md` — dual register voice modes
- `docs/Audiopheliac_Listening_Profile_v2026_04.md` — genre spine and playlist rules
- `docs/Audiopheliac_Site_Architecture.md` — public-site architecture
- `media/audio_system_playbook.md` — Office Studio chain (version-aged)

**Code surfaces:**

- `console/` — Flask prototype Cockpit (~v0.9.2). Spotify + YXC + direct DLNA MinimServer integration. Runs at `127.0.0.1:5000` and `192.168.1.120:5000`. PWA-installable. Singleton-anchored launcher.
- `automation/` — `music_indexer.py`, `spotify_pull.py`, `spotify_local_match.py`, `spotify_gap_report.py`. The daily data pipeline.
- `site/` — Astro + Cloudflare Pages public site. Seven-page scaffold. Full Spectrum palette ported in tokens.css. Canonical mark embedded.
- `skills/monitor-layout-lock/` — local Claude skill definition.

**Data:**

- `data/library_index/library_index.json` — 6,845 tracks indexed (last full run during May 9 First Tracks add).
- `data/spotify/spotify_library.json` — Spotify library snapshot.
- `data/manifests/spotify_local_matches.json` + `spotify_missing_tracks.txt` — gap report outputs.

**Brand layer:**

- Full Spectrum palette locked. Canonical raster mark locked. Brand voice v3 with dual register. Canva brand kit `kAHGkHrcJYU` (color/font paste still pending in Canva UI). Nashville Midnight archived as future sub-brand.

**Reference docs (per-package profiles):**

- `docs/software/Spotify.md` — Premier / Lossless / bit-perfect chain through AIR Hub.
- `docs/software/Yamaha-RN800A.md` — YXC API surface and firmware-confirmed limitations.
- `docs/software/Roon.md` — DEPRECATED archive; trial cancelled 2026-05-18.
- `docs/software/_TEMPLATE.md` — skeleton for new profiles.

**Hardware ground truth (current as of 2026-05-21):**

- MOTU M4 purchased, awaiting arrival (replacing AIR Hub as primary interface; AIR Hub becomes cold spare).
- Focusrite Scarlett Solo Gen 4: failed 2026-05-11, removed from chain.
- Family Room: Yamaha R-N800A + Pro-Ject Phono Box S2 Ultra + Technics SL-1200MK2 (Ortofon Blue) + Polk ES60.
- Office Studio: AT-LP120XUSB + Schiit Mani II + AIR Hub + Rolls MX28 + Yamaha HS7 + JBL LSR310S.
- Lanai: 1Mii RX → Schiit SYS → Bose 3-2-1 + Singing Machine.
- Garage: Bose SoundTouch Genius + Amazon Echo.

**Music substrate (active):**

- MinimServer on NAS serving `\\NAS87828E\Music` to R-N800A via UPnP/DLNA.
- Suno @audiopheliac account active; commercial use rights; 10,000 credits/month.
- Spotify Premier; Local Files of `M:\The Audiopheliac` (Suno output archive).
- Discogs: token-auth; vinyl master catalog v2026.03 with median pricing.

**Vinyl collection:**

- `Vinyl/vinyl_master_v_2026_02_full.md` — full catalog with Discogs median pricing.
- Wishlist at `Vinyl/Vinyl_Wish_List_v2026.04.md`.
- Recent adds: Zach Bryan, Shaboozey, Gavin Adcock, Red Clay Strays.

**Cross-project boundaries:**

- Plex infrastructure (qpkg, network, storage, clients, transcoder) → Lab workspace.
- Plex audio routing into Yamaha + MinimServer integration → Audiopheliac.

---

## What's Not in the Repo Yet (Tracked Open Items)

- Cockpit canonical implementation (Cloudflare Worker + Astro + MCP-registry).
- Astro site full content (page stubs are scaffolded; content authoring pending).
- Amazon PA-API gear proxy live (waiting on PA-API qualifying sales).
- Discogs Python collection sync + Task Scheduler.
- MOTU M4 setup (post-arrival).
- Plex source integration in the Cockpit (gated on Lab Phase 3 NAS folder normalization + eight pattern-doc open questions).
- Cockpit Studio mode (three lanes: audio + visual + AI video).
- Cockpit video consumption mode (Plex video, Cast, AirPlay 2, eARC).

---

## The Arc

What started as a vinyl tracker became a multi-surface music intelligence system spanning a public website on Cloudflare, a private home control center on Flask (with a designed-but-unbuilt canonical Cloudflare Worker successor), an automated music pipeline matching Spotify against local FLAC, a Suno commercial music production account, a per-package documentation discipline, a dual-write session-close charter with line-count verification, a four-zone signal-chain map, a per-room playback protocol matrix, and a brand layer with locked palette + dual voice register + canonical mark.

The pattern is consistent: vibe-coded, fast iteration, but with regular reorientations when the product model drifts. The CLAUDE.md HISTORY section reads like a forensic record of those reorientations as much as a changelog. The 2026-05-18 session-level reorientation is the load-bearing example — three commits shipped against a guessed product model, then a hard stop and a structural CLAUDE.md fix to prevent recurrence.

The Audiopheliac is currently mid-build on Pass A (music source integration pattern). Pass B (video consumption) and Pass C (Studio mode, three lanes) are deferred. The Cockpit canonical architecture is designed but unbuilt; the `console/` prototype is the only live implementation.

Where every cable, waveform, and decibel earns its keep.
