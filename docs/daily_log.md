# The Audiopheliac — Daily Log

**Repo:** `The-Audiopheliac` (https://github.com/MarcArmy2003/The-Audiopheliac)
**Owner:** Gillon "Gill" Marchetti
**Established:** 2026-05-18
**Charter:** #theaudiopheliac channel charter, hybrid logging architecture (Option C). See `CLAUDE.md` §SESSION-CLOSE PROTOCOL Step 3 for the dual-write contract.

---

## Scope lock

This file is the durable archive of record for **The Audiopheliac only**. It is dedicated to this product and this repo. It is NOT shared with:

- `valor-core/docs/daily_log.md` (VAL / VeteranAnalytics.com)
- Any VeteranIntel.org daily log
- Any other product's session record

Do not write Audiopheliac sessions into a VAL or VI log. Do not pull VAL or VI sessions into this one. If a session legitimately touched multiple products, split the close summary by product and write each entry to its own log.

---

## Format

Each session-close appends a new section at the bottom of this file. Append-only. Never overwrite. Never merge with prior entries.

```
## Session [N] — [YYYY-MM-DD]

**Work done:**
- ...

**Commits:**
- `[short SHA]` — [one-line description]

**Decisions:**
- ...

**Corrections:**
- ...

**Next actions:**
- ...
```

Pre-close verification (per CLAUDE.md §SESSION-CLOSE Step 3c): line-count diff before/after the append. Confirm the line count grew by the expected amount before reporting session complete. Slack alone has historically silently absorbed close signals while the GitHub append dropped out; the line-count check exists to catch that failure mode.

---

## Entries

<!-- Session entries append below this line, newest at bottom. -->

## Session 1 — 2026-05-18

Inaugural session under the dual-write charter. Single long Cowork session that traversed three coherent work blocks, one hard-stop reorientation, and the project-hygiene pass that closed it.

**Work done:**
- Adopted the #theaudiopheliac channel charter (hybrid logging architecture, Option C). Codified the dual-write SESSION-CLOSE contract in CLAUDE.md §SESSION-CLOSE PROTOCOL: every close writes BOTH a Slack channel post AND a `docs/daily_log.md` append, with a line-count verification step to catch the failure mode where one write silently drops. This entry is the first execution of that contract.
- Seeded `docs/daily_log.md` as the Audiopheliac-only durable archive (scope-locked from valor-core and VeteranIntel daily logs).
- Deprecated paperclip across The Audiopheliac. Stripped it from the active-workflow blocks in CLAUDE.md (IDENTITY AND ROLE, RAFA Operational routing, BEHAVIORAL RULES, CROSS-SURFACE ARCHITECTURE, SESSION-INIT, MID-SESSION SYNC, SESSION-CLOSE, SESSION TRIGGER WORDS). Replaced the PAPERCLIP SURFACE section with a deprecation notice. Banner-flagged `docs/Audiopheliac_Paperclip_Reference.md` as historical archive. Tombstoned the two paperclip auto-memory entries; added a `feedback_lane_discipline_cowork_rafa.md` replacement.
- Deprecated Roon (trial cancelled before subscription kicked in; Roon did not meet playback purposes). Cleaned CLAUDE.md (HARDWARE, SOFTWARE, SIGNAL CHAIN MAP, PROJECT FOLDER STRUCTURE, BEHAVIORAL RULES, OPEN ACTION ITEMS, HISTORY). Banner-flagged `docs/software/Roon.md` as historical archive. Promoted MinimServer back to primary media server.
- Phase A+B ship: committed the Cockpit v0.9 Spotify+YXC refactor that had been sitting uncommitted in the working tree, folded in today's Roon-plumbing cleanup, deleted `console/roon.py`, fixed a production bug in `launch.pyw` (singleton anchor was checking for `preferred_zones` which v0.9 dropped, causing every shortcut click to spawn a duplicate Flask process; replaced with `cockpit_version` anchor exposed via `/api/config`). Eight files modified, one deleted. Shipped as commit `4d9ba2e`.
- Phase E ship: direct UPnP/DLNA MinimServer integration. New module `console/minimserver.py` (~500 lines, stdlib + requests, no new dependencies) covering SSDP discovery, ContentDirectory:Browse + :Search, AVTransport:SetAVTransportURI + Play. New `/api/miniserver/*` routes in `console/app.py`. Frontend wiring in `console/static/app.js`. Verified end-to-end by Rafa: SSDP returns state=ready with MinimServer + Yamaha; browse root returns the real MinimServer tree (520 albums / 6719 items / 148 playlists); search returns coherent results; play handoff loaded Oasis "Hello" from MinimServer and played it through the Yamaha. Four defects caught and fixed during verification (duplicate route block, status_snapshot last-wins SSDP order, media_server() no MinimServer preference, double-unescape silently zeroing pages). One functional limitation fixed (`_build_search_criteria` now compounds across `dc:title`, `upnp:artist`, `upnp:album`, `dc:creator` instead of title-only). Shipped as commit `12d55bb`.
- Phase D4 drafted (design-out-the-error UX pass): hide Spotify Devices card, restructure MUTE tile to `.power` pattern, filter Yamaha source row to physical inputs only, atomic Library-tab dispatch, destination indicator. **NOT COMMITTED.** Gill called a hard stop after pointing out my "Yamaha is the canonical destination" model was wrong — the canonical Cockpit has four zones and Office listening doesn't route to the Family Room Yamaha by default. The Phase D4 changes are still on disk uncommitted; treat as stale and not to be revived.
- Session-level reorientation: forensic acknowledgement that I built the entire session on a guessed product model without reading `docs/Cockpit_System_Design_v2026_05.md` or `docs/Cockpit_Architecture_Decisions_v2026_05.md`. Landed structural fixes in CLAUDE.md to prevent recurrence: new §CANONICAL PRODUCT REFERENCES section at the top, §SESSION-INIT PROTOCOL requires reading System Design + ADR every session and a "Product framing" line in the status block, PROJECT FOLDER STRUCTURE entry for `console/` rewritten to explicitly mark it as a prototype (not the spec), three new behavioral rules (Scope contract, Ambient assumption check, `console/` is a prototype), new §CROSS-PROJECT SCOPE BOUNDARIES section with the Lab/Audiopheliac split for Plex. Rewrote `console/README.md` to lead with the prototype framing. Updated `console/app.py` module docstring. Two new auto-memory entries (`project_cockpit_scope.md`, `feedback_canonical_doc_first_for_cockpit.md`). NOT COMMITTED yet; queued for Rafa.

**Commits:**
- `4ae6e7d` — docs: charter dual-write SESSION-CLOSE, deprecate paperclip + Roon
- `4d9ba2e` — feat(cockpit): ship v0.9 Spotify + YXC refactor; remove Roon plumbing
- `12d55bb` — feat(cockpit): Phase E ship — direct DLNA MinimServer integration

**Decisions:**
- Hybrid logging architecture (Slack live signal + GitHub daily_log durable archive) adopted as the operating contract.
- Paperclip out across The Audiopheliac. Active workflow is Cowork + Rafa only.
- Roon out. MinimServer is the primary library/playback substrate.
- The Cockpit is a four-zone home AV control center per `docs/Cockpit_System_Design_v2026_05.md`. The `console/` Flask app is a prototype slice, not the product. The canonical architecture is Cloudflare Worker + Astro + MCP server registry per `docs/Cockpit_Architecture_Decisions_v2026_05.md`.
- No Plex integration in the Audiopheliac workspace until the Lab workspace finishes the Plex infrastructure consolidation. The cross-project scope boundary is now codified in CLAUDE.md §CROSS-PROJECT SCOPE BOUNDARIES.

**Corrections:**
- I built the session on a guessed product model and never opened the canonical design docs. The CLAUDE.md PROJECT FOLDER STRUCTURE entry for `console/` was treated as specification when it was just a description of a prototype implementation. Every subsequent UX patch anchored to the wrong frame. Forensic record is the 2026-05-18 HISTORY entry "session-level reorientation." Structural CLAUDE.md fixes landed to prevent recurrence; auto-memory entries written so the discipline survives across sessions.
- "Yamaha is the canonical destination" assumption was wrong. Office listening is independent (GDMARCHE → AIR Hub → MX28 → HS7). The four-zone destination model is in System Design §1.
- Pre-close verification step in the dual-write contract caught the same failure mode I'm documenting: a session that doesn't have a discipline forcing it back to first principles will accept wrong premises and ship against them.

**Next actions:**
- New Cowork session, fresh start. First action: `audio:open` to fire the updated SESSION-INIT PROTOCOL which now requires reading System Design + ADR docs and stating product framing back. If the next session's status block doesn't include the Product framing line, the new protocol wasn't followed — flag it immediately.
- Rafa prompt for the reorientation-pass commit is drafted (see Slack); needs to be run to push CLAUDE.md + console/README.md + console/app.py + this daily_log entry to origin/main.
- Phase D4 working-tree changes (Phase D4 frontend work) remain uncommitted on disk. Recommend they be reverted in the next session rather than re-attempted — they were built against the wrong product model.
- Canonical-docs-first discipline: any work touching the Cockpit must cite the canonical doc + section in the prompt's Scope-contract line.

**Open carry-forwards (not blocking the close):**
- Phase C re-probe (vTuner navigation with receiver powered on) — Rafa Prompt 4 drafted but not run. Gates the Phase G Net Radio decision.
- Roon footprint removal on NAS (Docker container at `/share/Container/RoonServer/`, `ghcr.io/roonlabs/roonserver:latest` image) and on GDMARCHE (Bridge service uninstall, Remote desktop app uninstall, `roon_token.json` cache clear). Rafa-lane.
- Untracked clutter in the working tree (`console/prototypes/`, `temp_covers/`, `assets/brand/`, `docs/*.pdf`) — triage pass needed.
- The Phase D4 uncommitted working-tree changes — revert recommended in next session.

## Session 2 — 2026-05-18

Restart session after Session 1's hard-stop reorientation. Triggered by a Plex integration hand-off from the Lab workspace landing at the moment Cowork opened. Executed the updated SESSION-INIT PROTOCOL cleanly (Product framing line caught the new contract), made one product-model error inside the new protocol (corrected by Gill), and shipped the first artifact under the pass-A design discipline.

**Work done:**
- SESSION-INIT executed under the updated protocol. Read canonical docs (`docs/Cockpit_System_Design_v2026_05.md`, `docs/Cockpit_Architecture_Decisions_v2026_05.md`), `docs/daily_log.md`, and Slack `#theaudiopheliac` back through 2026-05-13. Output the Product framing line in the status block per the new protocol contract. Reorientation discipline from Session 1 close fired correctly.
- Framed the Lab's eight-bullet Plex integration hand-off as a multiple-choice substrate question (MinimServer-only vs hybrid vs Plex Amp vs unified Plex). Gill corrected: the Cockpit is additive; MinimServer stays, Spotify stays, Plex is being ADDED to the source set, not chosen instead of any of it. Second product-model error in two sessions, this one inside the new protocol rather than against it.
- Saved feedback auto-memory `feedback-cockpit-is-additive-not-substitutive` and updated MEMORY.md index. Memory pairs with `feedback-canonical-doc-first-for-cockpit` from Session 1: yesterday's memory handles "read the canonical doc first," today's memory handles "even after the doc is read, default to additive when integrating new sources." Two-move discipline against the same class of product-model error.
- Discussed structured skill-driven design pass vs continuing with tactical entry points. Recommended pass A (`/engineering:system-design` for the music-source integration pattern, with Plex as the first concrete instance) first; passes B (video consumption) and C (Studio mode: audio + visual + AI video production) as deferred follow-ons. Gill concurred ("Concur with recc. Draft it.").
- Invoked `/engineering:system-design`. Drafted `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` (12 sections, ~2400 words). Covers: integration contract every source satisfies; MCP server pattern (canonical) and Flask shim pattern (prototype) with `console/` migration path; per-source UI surface; per-zone routing matrix grounded in current SIGNAL CHAIN MAP; Plex/Plex Amp as the first concrete instance; source-of-record pattern for overlapping sources (MinimServer + Plex both indexing the same NAS files); migration path from prototype to canonical Cloudflare Worker + Astro + MCP-registry architecture; 8 open questions for Gill reframing the Lab's hand-off bullets under additive integration; acceptance criteria; deferred scope (passes B and C explicitly excluded).
- Gill flagged that Studio mode (pass C) includes visual editing and AI video integration alongside audio production. Updated §12 of the pattern doc to spell out Studio's three lanes (audio production, visual editing, AI video integration) under additive framing. Saved project auto-memory `project-studio-mode-scope` and updated MEMORY.md.
- Verification pass against the canonical refs: every Cockpit claim cites System Design §1/§3/§4a/§7 or ADR-001 through ADR-005; every hardware/signal-chain claim grounded in CLAUDE.md HARDWARE + SIGNAL CHAIN MAP (Office AIR Hub chain, Family Room R-N800A protocols including AirPlay 2, Lanai 1Mii primary with Cast as capability-not-actively-routed, Garage Bluetooth); scope contract cited inline; no substitution framing slipped in; brand voice constraint respected (architecture doc, not user-facing copy).

**Commits:**
- (pending Rafa) — `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` (new file) + this `docs/daily_log.md` Session 2 append

**Decisions:**
- Cockpit integrations are additive by default. Substitution requires an explicit Gill call (memorialized in auto-memory `feedback-cockpit-is-additive-not-substitutive`).
- Pass A landed first as the structured design pass. Passes B (video consumption) and C (Studio mode: audio + visual + AI video production) are deferred to their own sessions.
- `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` is the third canonical Cockpit doc, supplementing System Design and ADR. Should be added to CLAUDE.md §CANONICAL PRODUCT REFERENCES so future sessions read all three; held off on the unilateral CLAUDE.md edit pending Gill's review of the pattern doc itself.
- Studio mode scope is three lanes: audio production (Ableton, Audacity, Suno, supporting apps), visual editing (apps TBD), AI video integration (services TBD). Memorialized in auto-memory `project-studio-mode-scope`. Pass B (video consumption) is distinct from pass C (visual production).
- No visual rebrand. Full Spectrum + canonical mark stay locked. `/brand-voice:brand-voice-enforcement` governs any future user-facing copy the design pass produces.

**Corrections:**
- Plex integration framed as multiple-choice substrate question on first response. Gill corrected: additive. Fix applied in-session (memory written + pattern doc drafted under the additive framing). Two-move discipline now in place: yesterday's `feedback-canonical-doc-first-for-cockpit` catches the read-the-doc move; today's `feedback-cockpit-is-additive-not-substitutive` catches the integration-shape move that lands after the canonical doc is read.

**Next actions:**
- Run the Rafa commit prompt (drafted in chat at close) to push the pattern doc + this daily_log entry to origin/main.
- Update CLAUDE.md §CANONICAL PRODUCT REFERENCES to include `docs/Cockpit_Source_Integration_Pattern_v2026_05.md` as a required read for any source-integration work. Hold for Gill's review of the pattern draft first.
- Work through the eight open questions in §10 of the new pattern doc when ready; resolves the Lab's hand-off and unblocks their Phase 3 NAS folder normalization. Lab can run Phases 1 and 2 (diagnostic + qpkg consolidation, keep Plex + MinimServer) regardless.
- Pass C (Studio mode design) when ready: three lanes (audio + visual + AI video). Scope reflects the 2026-05-18 expansion.
- Pass B (video consumption: Plex video, Cast, AirPlay 2 video, eARC routing for the TVs) when ready.

**Open carry-forwards (not blocking the close):**
- Phase D4 working-tree changes from Session 1 still uncommitted. Revert recommended.
- Session 1's CLAUDE.md reorientation-pass edits still uncommitted (Rafa prompt drafted at Session 1 close).
- Roon footprint removal on NAS (Docker container at `/share/Container/RoonServer/`, `ghcr.io/roonlabs/roonserver:latest` image) and on GDMARCHE (Bridge service uninstall, Remote desktop app uninstall, `roon_token.json` cache clear). Rafa-lane.
- Untracked clutter in the working tree (`console/prototypes/`, `temp_covers/`, `assets/brand/`, `docs/*.pdf`) — triage pass needed.
- The eight open questions in §10 of the new pattern doc.

## Session 3 — 2026-05-28

Long mixed session that traversed Plex Phase 4 persistence fix verification, an Audiopheliac project history doc, Plex web UI walkthrough, MOTU M4 first-time setup and Office Studio chain swap, plus assorted protocol additions to CLAUDE.md. Gill called the session "mixed in with other things" and elected to close so the next session can be dedicated to MOTU M4 software (Ableton + Plexamp Audio).

**Work done:**
- Phase 4 Plex persistence fix verified at ~12h uptime: PID 24649 running clean, `PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/share/Plex/Library` visible in live process `/proc/<pid>/environ`, `claimed="1"`, machineIdentifier preserved, data footprint 1.4 GB and growing on the new persistent path. TMPDIR architectural footnote accepted as-is (cache device for transcoder scratch is a feature). Rollback insurance remains on disk pending ~1 week monitoring window.
- Audiopheliac project history doc drafted (`outputs/Audiopheliac_Project_History_2026-05-27.md`, 22KB, 11 phases from genesis 2025-09-12 through current state) at Gill's request as a vibe-coded evolution narrative. Set as a living document for milestone updates going forward.
- CLAUDE.md SESSION-CLOSE PROTOCOL Step 0 added: mandatory `/no-man-left-behind` skill invocation before any documentation update, commit, or close-record write. Pattern mirrors SESSION-INIT's task-observer Step 0.
- CLAUDE.md Hand-off prompt delivery convention added under RAFA section: all Rafa prompts delivered in chat code blocks for copy-paste; never saved to `prompts/rafa-<task>-<date>.md`. Matches VAL workspace protocol.
- CLAUDE.md Backend-rewiring-proceeds-immediately rule added under BEHAVIORAL RULES: when Audiopheliac or Cockpit changes cause downstream rewiring of attached apps' backend configs (Plex library paths, Spotify Connect device hints, YXC enabled inputs, DLNA targets, AIR Hub/MOTU routing, Cockpit `config.json` source list, Ableton mappings, Suno destinations, vinyl pipeline targets, Hue Entertainment, Net Radio presets, MusicCast grouping, per-package profiles), the wiring fix proceeds in the same session, not deferred.
- CLAUDE.md para-memory-uninstalled note added near the Task Observer pre-flight block: skill is no longer installed (Gill removed 2026-05-28); patterns survive via task-observer protocols.
- Plex Settings spec doc created at `docs/Plex_Media_Server_Settings_v2026_05.md` (v2026.05.28.1). Locked General, Remote Access, Library settings with rationale tied to objectives O1-O8. Music library Advanced settings preflight pre-populated for the eventual Phase 5 add (Sonic Analysis ON, Prefer local metadata ON, Genres: Embedded Tags, Album Loudness Analysis ON). Remaining settings pages flagged as pending per-page review with Gill.
- Plex web UI walkthrough partial: server renamed to "The Audiopheliac NAS"; Remote Access stays ON (Gill flagged CarPlay use case); General + Remote Access + Library tabs reviewed with explicit value recommendations. Quality / Network / Transcoder / DLNA / Languages / Scheduled Tasks reviews deferred.
- MOTU M4 arrived and installed: driver MOTU M Series ASIO 4.5.0.551, firmware 2.07, serial m4ma0243as. Office Studio chain rewired: M4 MONITOR Outs 1-2 (1/4" TRS balanced) → Rolls MX28 LEVEL 3 BAL → HS7 monitors + LSR310S sub. AIR Hub demoted to 30-day cold-spare evaluation through 2026-06-27. M Series Console: 48 kHz / buffer 256 / lowest-latency-safety-offsets ON / sync-Windows-sample-rate-to-device ON.
- Project records batch update for the M4 swap landed against the renumbered project path (`C:\Users\gillo\6. The-Audiopheliac\` per the morning folder reorganization): CLAUDE.md HARDWARE Audio Interface block, SIGNAL CHAIN MAP Office Studio block, SOFTWARE driver line, GAIN STAGING PRINCIPLES, OPEN ACTION ITEMS table, Canonical Product References AIR Hub mention, `console/config.json` Studio destination `sub`, new `docs/software/Motu-M4.md` profile (full per-package profile from template with troubleshooting runbook and known limitations), `docs/Audiopheliac_Audio_Source_Inventory_v2026_05.md` §2d driver table + version bump to 2026.05.28.3.
- Two task-observer observations appended to `skill-observations/log.md`: (1) M4 walkthrough Step 5 asserted Device Manager placeholder entry pre-connection (false — Device Manager only shows currently-connected devices); (2) M4 walkthrough Step 10 asserted Enhancements tab existed for MOTU M Series output (false — USB Audio Class pro interfaces don't surface Enhancements tab in Windows Sound Control Panel). Both observations principle-tagged to the verification-first family.
- Para-memory plugin uninstalled by Gill. Note added in CLAUDE.md near the task-observer pre-flight block. Cross-cutting principles file at `skill-observations/cross-cutting-principles.md` updated with the patterns previously captured in para-memory feedback files so they survive as task-observer protocol guidance.
- No-Man-Left-Behind sweep at session close folded in: stray `prompts/rafa-phase4-plex-data-relocation-2026-05-27.md` file deleted via Cowork delete permission grant; Lab cross-workspace log path corrected from old un-numbered `The-Audiopheliac` reference to numbered `6. The-Audiopheliac` per the migration rule.

**Commits:**
- (pending Rafa) — batch commit for all 2026-05-28 doc updates: CLAUDE.md, `console/config.json`, `docs/software/Motu-M4.md` (new), `docs/Plex_Media_Server_Settings_v2026_05.md` (new), `docs/Audiopheliac_Audio_Source_Inventory_v2026_05.md`, `skill-observations/log.md`, `skill-observations/cross-cutting-principles.md`, this `docs/daily_log.md` Session 3 append.

**Decisions:**
- MOTU M4 is active primary as of 2026-05-28; AIR Hub is cold spare under 30-day evaluation through 2026-06-27.
- Plex Remote Access stays ON for CarPlay use case (upload speed Mbps still pending so a remote stream can't saturate Spectrum uplink).
- `/no-man-left-behind` skill is now a mandatory pre-flight at session-close (Step 0).
- Hand-off prompts are delivered in chat, not saved to `prompts/` (matches VAL convention).
- Backend rewiring proceeds inline with the upstream change, not deferred.
- Para-memory plugin uninstalled; task-observer protocols absorb the integrations.
- Next session is dedicated to MOTU M4 software setup (Ableton Audio prefs reconfig, Plexamp Audio settings reconfig). Plex web UI page-by-page review continues in parallel or in a separate session.

**Corrections:**
- Verification-first miss on M4 walkthrough Step 5 — asserted Device Manager would show a placeholder entry pre-connection. False; Gill self-diagnosed and corrected. Logged as task-observer observation.
- Verification-first miss on M4 walkthrough Step 10 — asserted Enhancements tab existed for the MOTU M Series output. False; USB pro audio interfaces don't surface that tab. Gill caught it. Logged as task-observer observation.
- Mount-drop confusion mid-session: tried to write to old un-numbered `The-Audiopheliac` paths after the folder renumbering happened. Gill provided the migration map (`MIGRATION_MASTER_2026-05-28.md`); reoriented to numbered paths and proceeded.

**Next actions:**
- Dedicated MOTU M4 session: walk through Ableton Audio Preferences (MOTU ASIO driver, M4 device, sample rate 48 kHz, buffer 256, I/O channels) and Plexamp Audio settings (Output Device MOTU M Series, ASIO if Plexamp ≥ 4.10 else WASAPI Exclusive, Resample OFF, Bit Depth Match Source, Pre-amp Gain 0, DSP OFF, Volume Leveling + Gapless ON).
- Plex web UI page-by-page review: Quality, Network, Transcoder, DLNA, Languages, Scheduled Tasks, Extras, Online Media Sources, Authorized Devices, Webhooks. Then Phase 5 (Music library add with Advanced settings preflight).
- Set Plex Remote Access Internet upload speed Mbps to actual Spectrum upload rate.
- RCA-M → TRS-M adapter pair purchase to unblock the vinyl rip path (Schiit Mani II → M4 LINE IN 3-4).
- Rollback insurance cleanup after ~1 week monitoring: delete `/share/CACHEDEV1_DATA/.qpkg/PlexMediaServer/Library.moved-20260527-191819` + `Library.empty-restart-20260527-192131` + the init script backup once Plex restart-cycle survival is confirmed.

**Open carry-forwards (not blocking the close):**
- `docs/av_master_inventory_2026.md` has 9 AIR Hub references across hardware inventory rows, signal flow diagrams, and topology summaries. Substantial structural update required to swap to MOTU M4; out of scope for inline fix per no-man-left-behind operational test (would require redesign of sections, not a one-line edit). Audit pass when convenient.
- `media/audio_system_playbook.md` is already flagged in CLAUDE.md §CANONICAL PRODUCT REFERENCES as "version-aged (mentions Scarlett Solo and AIR Hub; MOTU M4 is now active primary as of 2026-05-28)." Pre-existing acknowledgment of staleness; full rewrite is its own work.
- Plex web UI cleanup beyond what's done: Remote Access stays ON, upload speed Mbps still pending.
- Phase 5 Plex Music library add deferred until web UI cleanup completes.
- Plex Quality / Network / Transcoder / DLNA / Languages / Scheduled Tasks / Extras / Online Media Sources / Authorized Devices / Webhooks settings review — deferred (requires user input via screenshots).
- Sonic analysis backgrounding will run for ~hours on ~6800 tracks once the Music library is added.
- Roon footprint removal on NAS (Docker container + image) and on GDMARCHE (Bridge service + Remote app + token cache) remains Rafa-lane carry-forward.
- Untracked clutter triage in the working tree.
