# Cockpit Source Integration Pattern v2026.05

**Status:** Draft, design phase
**Owner:** Gill Marchetti
**Date:** 2026-05-18 (Session 2)
**Companion to:** `docs/Cockpit_System_Design_v2026_05.md`, `docs/Cockpit_Architecture_Decisions_v2026_05.md`
**Scope contract:** Cockpit System Design §1 (functional requirements, source list), §3 (components, MCP server pattern), §4a (data flow), §7 (UI information architecture); ADR-001 (Cloudflare Worker hosting), ADR-002 (Astro Islands frontend), ADR-003 (LLM model selection), ADR-004 (MCP server hosting); CLAUDE.md §CANONICAL PRODUCT REFERENCES, §CROSS-PROJECT SCOPE BOUNDARIES (Plex Lab/Audiopheliac split).
**In scope:** Music sources for v1. Plex Server + Plex Amp as the first concrete instance triggered by the Lab workspace's 2026-05-18 integration hand-off.
**Out of scope (deferred to separate passes):** Video sources and video playback (pass B). Audio/video production tooling and Studio mode internals (pass C). Hue lighting, LLM agent prompt design, listening history visualization (already covered in System Design and ADRs).

---

## 1. The Problem This Solves

The Cockpit System Design §1 lists multiple music sources by name (local FLAC via MinimServer/UPnP, Spotify, Suno, Net Radio, Discogs catalog, vinyl-as-source). The Lab workspace's hand-off added Plex Server + Plex Amp to that list as another addition, not a substitute for anything already present.

The System Design names the sources. It does not codify HOW a source plugs in. The `console/` Flask prototype has shipped two source integrations in different shapes:

- **Spotify:** server-side OAuth (Spotipy), Flask routes calling the Spotify Web API directly, transport via Spotify Connect on the R-N800A.
- **MinimServer / UPnP:** hand-rolled SSDP discovery, ContentDirectory:Browse + :Search, AVTransport push to the R-N800A's UPnP renderer (Phase E ship, commit `12d55bb`, 2026-05-18).

Adding Plex without a pattern means a third bespoke integration. Adding the next source means a fourth. The implementation gap between the canonical architecture (Cloudflare Worker + MCP server registry per ADR-001 / ADR-004) and the current prototype (Flask + per-source bespoke clients) grows wider with each ad hoc integration.

This pattern doc codifies:

1. The integration contract every source must satisfy.
2. The MCP server pattern (canonical) and the Flask shim pattern (prototype).
3. The UI surface a source presents in the Cockpit.
4. The per-zone routing matrix that connects a source to a destination.
5. Plex / Plex Amp as the first concrete instance of the pattern.
6. The migration path from prototype to canonical.

The framing is additive throughout. New sources extend the matrix; they do not replace existing entries.

---

## 2. Integration Contract

Every source the Cockpit supports exposes, at minimum, these surfaces:

**Discovery and connection**
- Health check: source reachable and authorized.
- Source identity: stable name, type (`local-library` | `streaming` | `radio` | `catalog-only` | `manual`), supported features, supported zone protocols.

**Library**
- Browse: hierarchical traversal of the source's content (artist > album > track, or playlist > track, or station list, or release > master, etc.). Paged results with stable identifiers.
- Search: text search across the source's content. Returns unified result records.

**Playback**
- Play-to-zone: hand off a content reference to a named destination zone. The source declares which zone protocols it can target directly.
- Transport: play, pause, skip, seek, volume. For sources that delegate to the destination's transport (DLNA push to a UPnP renderer, Spotify Connect handing off to the R-N800A, Plex Server `play_media()` to a Plex Amp client), the source returns a handle that the zone transport interface uses.
- State: current track, queue position, source connection state.

**Metadata**
- Track record: title, artist, album, duration, art URL, source-of-record provenance.
- Cross-source identifiers when available (MusicBrainz ID, ISRC, Spotify URI, Plex rating key) for de-duplication and listening-history aggregation.

**Eventing (optional but preferred)**
- Push state changes to the Cockpit backend rather than relying on polling. Sources that natively support push (MinimServer via UPnP eventing, Plex via webhooks, Spotify via Spotify Connect state notifications) cut backend polling load.

**Out of contract**
- Sources are NOT required to mix audio into a single output stream. The Spotify DRM boundary makes that infeasible, and the architectural cost is high for the others. Sources are coordinated, not mixed.
- Sources are NOT required to support every zone. A source declares which zones it can target; the UI hides invalid combinations and the LLM agent's tool descriptions encode the same matrix.

---

## 3. MCP Server Pattern (Canonical)

Per ADR-004, the canonical Cockpit uses one MCP server per source. Each MCP server is a long-lived process hosted on QNAP Container Station (default) or GDMARCHE (for sources whose dependency lives there, like Ableton-OSC). The Cockpit backend (Cloudflare Worker + Durable Object per ADR-001) discovers MCP servers via the MCP server registry, invokes tools per user action, and fans out state changes over WebSocket.

Each source's MCP server implements the §2 contract as MCP tools:

| Contract surface | MCP tool naming | Returns |
|---|---|---|
| Health | `[source]_health` | `{ reachable, authorized, version }` |
| Browse | `[source]_browse` | `{ items, next_cursor }` |
| Search | `[source]_search` | `{ results, total }` |
| Play to zone | `[source]_play_to` | `{ playback_handle, zone, source }` |
| Transport | `[source]_transport` | `{ action, ok }` |
| State | `[source]_state` | `{ now_playing, queue_position, ... }` |

The LLM agent loop (Claude Haiku for default turns, Sonnet for scene composition per ADR-003) uses the same MCP tool surface for natural-language control. Tool descriptions are how the agent learns each source's capabilities and zone-compatibility matrix; the agent never needs to know source-specific implementation detail.

---

## 4. Flask Shim Pattern (Prototype / `console/`)

The current `console/` Flask app is the bridge between today and the canonical architecture. Until the Cloudflare Worker + MCP registry is built, each source is implemented as a Python module in `console/` exposing the §2 contract as Flask routes.

**Convention:**

- One module per source: `console/[source].py` (`spotify.py`, `minimserver.py`, `plex.py`).
- Routes follow `/api/[source]/[surface]` (`/api/plex/browse`, `/api/plex/play-to`, `/api/plex/state`, etc.).
- Each module exports a class or function set whose method names match the §2 contract.
- Auth and secrets live in `console/config.json` per existing pattern.

**Migration discipline:**

- Each source module is structured so it can be lifted into an MCP server with minimal rework: the contract methods become the MCP tools.
- Sources that already exist in the prototype (`spotify.py`, `minimserver.py`) are retroactively reshaped to match the §2 contract where they don't already. Surface naming gets tightened; behavior stays the same.
- New sources (Plex, future) are written contract-first.

This pattern survives the canonical migration. Modules that match the contract today become MCP servers tomorrow with renamed methods, not rewritten code.

---

## 5. UI Surface (Per Source)

Every source presents the same shape of UI in the Cockpit, parameterized by the source's declared capabilities:

**Source card (right rail per System Design §7):**

- Source identity: brand mark, name, connection state pill.
- Quick action: "Use as next source for [active zone]" — disabled if the source can't target the active zone.
- Toggleable expanded state: search box, recent results.

**Source library page (`/library/[source]` route under canonical Astro routing, or `console/templates/index.html` library tab under prototype):**

- Browse tree (left rail), result grid (main), per-source filters (right when applicable).
- Unified result card: art, title, artist or album, source-of-record badge, "Play in zone" affordance with zone picker constrained to compatible zones.
- Source-specific affordances live in a per-card overflow menu (Spotify "Add to Spotify playlist," Plex "View in Plex," Discogs "View release page," Suno "Open in Suno Studio"). Never in the primary control affordances.

**Queue strip (per zone, in Cockpit primary mode):**

- Source-of-record badge on each queued item so a mixed queue (Spotify track + MinimServer FLAC + Plex track in the same zone's queue) is legible.

The design principle: the user controls a ZONE; sources feed content into the zone. Source-specific UI lives in source-specific overflow menus, not in the primary transport or queue controls.

---

## 6. Per-Zone Routing Matrix

Each zone declares its supported protocols. Each source declares which protocols it can target. The Cockpit's play-to-zone resolver matches source capability against zone capability and picks the best route. The UI hides invalid source-zone combinations.

**Zone protocol support (grounded in CLAUDE.md SIGNAL CHAIN MAP and HARDWARE):**

| Zone | Supported destination protocols |
|---|---|
| Office Studio | MX28 line input via AIR Hub on GDMARCHE; the GDMARCHE host can run Spotify desktop, Plex Amp, a UPnP renderer (Audirvana, BubbleUPnP), or any other audio app; output is `GDMARCHE > AIR Hub > MX28 (Input A) > HS7 + LSR310S` |
| Family Room | YXC (R-N800A native control), MusicCast (multi-zone distribution), UPnP (DLNA renderer on R-N800A, verified Phase E), Spotify Connect (R-N800A native), AirPlay 2 (R-N800A native), Cast (Chromecast 4K, Shield Pro at the TV) |
| Lanai | 1Mii RX (downstream of Family Room's Yamaha PRE OUT > MB15b > 1Mii TX); Cast to Lanai TV Chromecast (192.168.1.239) as a secondary, capability-not-actively-routed option per CLAUDE.md SIGNAL CHAIN MAP |
| Garage | Bluetooth to SoundTouch Genius (primary, phone-mediated); Yamaha Bluetooth from Family Room (secondary, sporadic at distance) |

**Source capability (current state):**

| Source | Office Studio | Family Room | Lanai | Garage |
|---|---|---|---|---|
| MinimServer / UPnP | via UPnP renderer on GDMARCHE (not yet installed) | YES (DLNA push to R-N800A, verified Phase E) | indirect (via Family Room 1Mii wireless) | no direct path |
| Spotify | via Spotify desktop on GDMARCHE (currently runs; Cockpit control TBD) | YES (Spotify Connect on R-N800A) | indirect (via Family Room) | indirect (phone Bluetooth, user-mediated) |
| Plex (Server + Amp) | via Plex Amp on GDMARCHE | via Plex Amp on Shield Pro at the TV, or AirPlay 2 from a Plex client, or Cast (see §7) | via Plex Amp on Lanai TV Chromecast, or indirect via Family Room (see §7) | no direct path |
| Suno | via browser on GDMARCHE | via browser-side Cast to Shield Pro or via Family Room AirPlay 2 | indirect | no direct path |
| Net Radio | no direct path | YES (R-N800A native source) | indirect (via Family Room) | no direct path |
| Discogs catalog | catalog-only (not a playback source) | catalog-only | catalog-only | catalog-only |
| Vinyl-as-source | manual now-spinning entry tied to the room with the turntable (Office for AT-LP120XUSB, Family Room for SL-1200MK2); not a Cockpit-controllable playback path |

"Indirect" means the audio reaches the zone, but the Cockpit cannot directly address that zone for that source — playback is initiated on the upstream zone and follows the wireless distribution chain. The UI labels these as "via [upstream zone]" rather than as primary play targets.

Cells marked "no direct path" do not appear as play options in the source's zone picker. They MAY appear if the user adds hardware or installs new software that changes the matrix; the matrix is data, not code.

---

## 7. Plex / Plex Amp: First Concrete Instance

**Source identity in the Cockpit:** "Plex." One source from the user's perspective. Internally, Plex Server provides the §2 library surface and Plex Amp clients provide the §2 playback surface. They appear as one source on the Cockpit's source rail with one badge on result cards.

**Library shape:**

- Plex Server indexes the same NAS music folders that MinimServer indexes. Both servers index. Both return their respective results when the Cockpit calls their browse or search. The UI shows MinimServer and Plex as separate sources on the rail; the user picks whichever they prefer for any given action, or relies on per-zone default source preference (see §8).
- Plex Server library scope for music: scoped to the NAS music folder per the Lab workspace's Phase 3 folder normalization. The canonical music path is `\\NAS87828E\Music\` per CLAUDE.md MUSIC LIBRARY ALBUM OUTPUT (mapped at `M:\`). Confirm Lab's final folder normalization decision before committing to the Plex library scope; that decision is in their lane.
- Plex Server's movies and TV libraries are out of scope for the Cockpit's music surface. They surface in the video design pass (B, deferred).

**Plex Amp client placement per zone (proposed; open questions in §10):**

| Zone | Plex Amp host candidate | Audio output path | Notes |
|---|---|---|---|
| Office Studio | Plex Amp desktop on GDMARCHE | `GDMARCHE > AIR Hub > MX28 (Input A) > HS7 + LSR310S` | Same chain as Spotify desktop on GDMARCHE; existing audio interface, no new hardware |
| Family Room | Plex Amp on Shield Pro at the TV | `Shield Pro > HDMI > R-N800A` | Shield Pro is already in the Family Room and Cast-target capable; Plex Amp on Shield transcodes audio by default. If bit-perfect is required, evaluate Plex DLNA push to R-N800A's UPnP renderer (same path as MinimServer Phase E) as an alternative |
| Lanai | Plex Amp on Lanai TV via Cast (Lanai TV at 192.168.1.239) | Lanai TV > J-Tech eARC extractor > Bose 3-2-1 TV 1 input | Lanai TV currently retains Cast capability per CLAUDE.md SIGNAL CHAIN MAP; this is the alternative to staying on the 1Mii wireless feed from Family Room |
| Garage | No Plex Amp client | n/a | Garage stays Bluetooth-only; Plex Amp via phone Bluetooth would add nothing over Spotify-via-phone |

**Cockpit Plex MCP / Flask shim (prototype implementation):**

- Library and playback control via Plex Server's HTTP API (well-documented; `python-plexapi` is the established Python library). `play_media(client, media)` directs a named client to play a media item.
- Plex Amp clients register with Plex Server and are addressable by friendly name. The Cockpit resolves "play X on the Family Room" to "tell Plex Server to play X on the Shield-Pro-Plex-Amp client."
- Module: `console/plex.py`. Routes: `/api/plex/health`, `/api/plex/browse`, `/api/plex/search`, `/api/plex/play-to`, `/api/plex/transport`, `/api/plex/state`.
- Auth: Plex server URL + auth token stored in `console/config.json` (gitignored per existing convention).

**Eventing:**

- Plex Server supports webhooks for playback state (`media.play`, `media.pause`, `media.stop`, `media.scrobble`, `media.resume`). Register the Cockpit backend URL as a webhook receiver; the Cockpit fans state out to the UI over WebSocket without polling.
- In the prototype, webhook receiver is a Flask route (`/webhooks/plex`). In the canonical Worker, it becomes an authenticated webhook endpoint terminating at the Durable Object.

---

## 8. Source-of-Record and the Cross-Source Library View

When multiple sources index the same content (NAS FLACs indexed by both MinimServer and Plex Server), the Cockpit needs a source-of-record pattern to avoid the user picking "play this album" and not knowing which source actually plays.

**Pattern:**

- Result grid shows source provenance badges on each card (M for MinimServer, P for Plex, S for Spotify, etc.).
- A "deduplicate" toggle on the library page collapses duplicate albums under one card and exposes the source choice as a dropdown on the card.
- Per-zone default source preference is configurable, e.g., "Family Room prefers MinimServer when both have the track; Office Studio prefers Plex Amp when both have the track." Defaults to "user's last-picked source for this zone" with a global fallback.

This decouples the user's mental model ("play this album") from the source-resolution detail, while preserving the user's ability to deliberately pick a specific source when they care.

---

## 9. Migration Path

**Now (Session 2, 2026-05-18):**

- This pattern doc lands as `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` and is added to the canonical references in CLAUDE.md §CANONICAL PRODUCT REFERENCES.
- Spotify and MinimServer modules in `console/` are reviewed for §2 contract conformance. Surface naming gets tightened where it doesn't already match; behavior is unchanged.
- Plex module (`console/plex.py`) is written contract-first.

**Near term (Cowork side, prototype):**

- Update `console/spotify.py` and `console/minimserver.py` to expose the §2 contract identically (same method names, same return shapes where the surface applies).
- Add `console/plex.py` per §7. New routes `/api/plex/*`.
- Update `console/static/app.js` to render the §5 UI surface for any source the Cockpit queries, instead of bespoke per-source rendering.

**Medium term (canonical migration):**

- Lift each `console/[source].py` module into its own MCP server hosted on QNAP Container Station per ADR-004.
- Stand up the Cockpit Cloudflare Worker per ADR-001.
- Migrate Flask routes to Worker endpoints calling MCP tools. Same contract, different transport.
- Cockpit UI moves to Astro Islands at `theaudiopheliac.com/cockpit` per ADR-002.
- Cloudflare Access fronts the route per ADR-005.

The pattern survives the migration. Modules that satisfy the §2 contract today become MCP servers tomorrow with minimal rework.

---

## 10. Open Questions for Gill

These are the decisions the Lab workspace asked for, refined through the additive lens. None of them are substrate questions — MinimServer stays. They are integration-shape questions for Plex.

1. **Plex Server install topology.** Single Plex install with movies, TV, and music as library sections, or a dedicated music Plex Server alongside the existing one. Lab is deferring to this answer for their Phase 3 NAS folder normalization. Operational simplicity favors single install; library separation favors dedicated.
2. **NAS music folder canonical path.** Today's HARDWARE entries point at `\\NAS87828E\Music\`. Lab's Phase 3 may propose a different normalization. This pattern doc holds either way; the concrete path is in Lab's lane.
3. **File format standard for music files on the NAS.** Lossless only (FLAC, ALAC), or mixed (vinyl rips, lossy legacy content). Affects what both Plex Server and MinimServer index, and how the Cockpit deduplicates across sources.
4. **Tagging tool and standard.** Beets, MusicBrainz Picard, manual, or hybrid. Affects metadata quality, cross-source identifier matching, and listening-history aggregation.
5. **Family Room Plex Amp host.** Shield Pro via Cast (already in place), or DLNA push from Plex Server to R-N800A's UPnP renderer (same path as MinimServer Phase E, no transcoding), or both with the user picking per session. Bit-perfect-vs-convenience trade.
6. **Per-zone default source preference.** Per-zone configurable, always ask, or always use last-picked. Affects friction on the most common action.
7. **Lanai Plex Amp.** Add Plex Amp on the Lanai TV Cast endpoint, or leave Lanai on the 1Mii wireless feed from Family Room only.
8. **Vinyl-rip ingestion workflow.** Where new rips land on the NAS, in what format, with what tagging. Both Plex and MinimServer pick them up automatically from the canonical music folder; the question is the rip-tool and tag-discipline upstream.

---

## 11. Acceptance

The pattern is accepted (and the Plex integration ship-ready in the prototype) when:

- `console/spotify.py` and `console/minimserver.py` expose the §2 contract identically (method names, return shapes).
- `console/plex.py` follows the same contract from day one.
- A new source can be added by writing a new module that satisfies §2 and registering it in the Cockpit UI source rail; no per-source UI rendering changes are needed.
- The LLM agent (when wired up post-canonical migration) can issue tool calls against any source by name without source-specific orchestration logic in the prompt.
- The per-zone routing matrix from §6 is encoded as configuration (`console/config.json` or equivalent), not hard-coded in JS or Python.

---

## 12. What This Pattern Doesn't Cover

- **Video sources and video playback** (Plex video, Cast video, AirPlay 2 video, eARC routing for the Lanai TV and the Family Room TV). Separate design pass (B). Same MCP-pattern logic, different protocol set and a UI architecture decision about whether video lives as a fourth Cockpit mode or as a separate set of routes.
- **Production tooling (Studio mode).** Studio mode is named in System Design §7 but under-specified. Scope spans three production lanes:
  - Audio production: Ableton Live 12, Audacity, Suno, supporting applications.
  - Visual editing: not yet scoped, app set TBD.
  - AI video integration: not yet scoped, service set TBD.

  Pass C covers where these tools surface in the Cockpit, how Studio relates to Cockpit primary mode (listening), whether visual and AI video share a contract with audio production tools or need a sibling contract, and whether the action targets from System Design §1 (send-to-Ableton, fire Live scene) live in Studio or Cockpit. Visual editing and AI video are an additive expansion of Studio mode flagged 2026-05-18, not a replacement of the audio production lane.
- **Hue lighting integration.** Covered in System Design §1 and §3. The Hue MCP is a sibling of the music source MCPs but uses a different contract because it is not a source; it is a destination effect.
- **LLM agent prompt design.** ADR-003 covers model selection. The agent's system prompt, tool-routing logic, and conversation memory are a separate design surface that consumes this pattern but doesn't shape it.
- **Listening history visualization.** Covered in System Design §1 and §5 (storage). The history layer consumes source provenance and source-of-record metadata produced by this pattern.

---

*This doc supplements `docs/Cockpit_System_Design_v2026_05.md` and `docs/Cockpit_Architecture_Decisions_v2026_05.md`. Read all three before any source-integration work.*
