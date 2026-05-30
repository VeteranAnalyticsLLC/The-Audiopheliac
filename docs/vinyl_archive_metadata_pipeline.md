# Vinyl Archive Metadata Pipeline

**Version:** 2026.05.1
**Owner:** Gillon "Gill" Marchetti (MarcArmy2003)
**Purpose:** Survey of free and open-source tools for tagging, organizing, and metadata-applying vinyl rips. Recommends which to wire into the planned Discogs integration per CLAUDE.md VINYL COLLECTION MANAGEMENT. Reference data for the Mentor skill when entering metadata / archive-discipline lessons.

---

## The Problem

A clean vinyl rip is half the work. The other half is making the resulting FLACs behave like the rest of a digital music library: correct artist, album, track titles, track numbers, year, genre, album art, and a durable record of HOW the rip was made.

Audacity's built-in metadata editor handles the basics (Edit Metadata Tags before Export Multiple), but it has no awareness of release databases (Discogs, MusicBrainz) and no batch-apply intelligence. For one or two albums it is sufficient; for a growing library it becomes the rate-limiter.

Better tools exist. This doc surveys the field, recommends a pick for the current setup, and stages the longer-term tooling discussion against the Discogs integration already named in CLAUDE.md VINYL COLLECTION MANAGEMENT (Python collection sync + Task Scheduler targeting `Vinyl_Collection_Update_Queue.csv`).

---

## Tool Survey

### Kid3

**License:** FOSS (GPL).
**Platform:** Cross-platform (Windows, macOS, Linux).
**URL:** https://kid3.kde.org/
**Format support:** FLAC, MP3, Ogg, AAC, MP4, Opus, WavPack, APE, ID3v1/v2, Vorbis comments, MP4 metadata.

**Strengths:**
- Mature project, active development under KDE.
- GUI plus CLI plus Qt-based scriptable interface.
- Direct Discogs and MusicBrainz lookup integration; pulls album metadata, track list, year, genre, optionally cover art.
- Batch operations across multiple files / folders.
- Custom filename-from-tag and tag-from-filename mapping.

**Weaknesses:**
- GUI is functional but not slick; learning curve for the more advanced batch operations.
- Cover art handling requires explicit fetch step (not automatic on metadata pull).

**Community endorsement:** Mentioned in r/jungle thread as the community's go-to alternative to Audacity's native metadata editor. Quote: "Use kid3 tagger or similar to automate tagging from Discogs."

**Best fit:** the canonical metadata-application tool for the post-Audacity stage of a vinyl rip. Use it after FLAC export to apply Discogs metadata in batch.

---

### Mp3tag

**License:** Freeware (proprietary, free for personal use).
**Platform:** Windows-native (macOS port available, less polished).
**URL:** https://www.mp3tag.de/
**Format support:** FLAC, MP3, Ogg, MP4/M4A, AAC, WavPack, APE, OGG, Opus, MPC, WMA.

**Strengths:**
- Polished Windows GUI; fastest GUI workflow on Windows.
- Discogs and MusicBrainz lookup integrations (community-maintained).
- Powerful batch rename / batch tag operations.
- Tag-from-filename, filename-from-tag, cover art handling all in one tool.
- Large community, active forum.

**Weaknesses:**
- Not open source. Free but proprietary.
- Windows-first; if Gill ever moves vinyl work to a non-Windows machine, less portable than Kid3.

**Community endorsement:** Mp3tag forum thread on Audacity vinyl digitization specifically recommends Mp3tag as the post-Audacity tagging tool.

**Best fit:** the most efficient GUI option on GDMARCHE for Gill's specific use case. If the manual workflow stays manual, Mp3tag is the most ergonomic option.

---

### discogstagger

**License:** FOSS.
**Platform:** Cross-platform Python CLI.
**URL:** https://github.com/jesseward/discogstagger
**Format support:** FLAC, Ogg, MP3.

**Strengths:**
- Script-friendly; ideal for automation pipelines.
- Pulls full album metadata from Discogs by release ID.
- Designed for tagging entire album directories at once.

**Weaknesses:**
- Project is mature but not actively developed (last meaningful commits years old).
- Requires Discogs API token and basic command-line comfort.
- Older code; may need dependency wrangling to run on modern Python.

**Best fit:** an option to wire into the planned CLAUDE.md VINYL COLLECTION MANAGEMENT Discogs integration if it's still functional at evaluation time. Worth a one-session smoke test before committing.

---

### vinyl-recorder (arthurbenemann)

**License:** FOSS.
**Platform:** Self-hosted web app.
**URL:** https://github.com/arthurbenemann/vinyl-recorder

**Strengths:**
- All-in-one: capture, track-split, MusicBrainz/Discogs auto-tagging, lossless FLAC output.
- Web UI is approachable.
- Runs locally; no cloud dependency.

**Weaknesses:**
- Replaces the Audacity/Ableton learning arc with a black-box workflow. Bypasses the lessons The Mentor is teaching.
- Less mature than the standalone-tool stack.
- Active development, but smaller user base than Kid3/Mp3tag.

**Best fit:** a candidate for "after Gill has internalized the manual workflow and wants to speed up" - the productization stage, not the learning stage. Not appropriate for Lesson 1 of the Mentor scope.

---

### vinylflow (olimic1000)

**License:** FOSS.
**Platform:** Cross-platform tool with Docker option.
**URL:** https://github.com/olimic1000/vinylflow

**Strengths:**
- Marketed as "digitize vinyl 10x faster": automated track splitting, Discogs metadata, organized output.
- Newer project, active development.
- Docker deploy option fits Gill's existing NAS Container Station infrastructure.

**Weaknesses:**
- Same as vinyl-recorder: replaces the manual workflow with automation. Bypasses learning.
- Newer; less battle-tested than mature alternatives.

**Best fit:** similar to vinyl-recorder. Candidate for post-learning speed-up phase. Worth re-evaluating once the Mentor scope completes Lesson 1.

---

## Recommendation Matrix

| Stage | Tool | Rationale |
|---|---|---|
| **Lesson 1 active (current):** Manual workflow, learn the chain | Audacity native metadata editor | Built into the tool Gill is learning. One less context switch. Sufficient for the first few albums. |
| **Post-Lesson 1:** Manual workflow, faster metadata | Mp3tag | Most ergonomic Windows GUI. Pairs cleanly with the manual Audacity capture/edit/export flow. |
| **Productization (optional, future):** Automated Discogs integration per CLAUDE.md VINYL COLLECTION MANAGEMENT plan | Kid3 (GUI/CLI hybrid) OR discogstagger (pure CLI) | Both are scriptable. Kid3 is more actively maintained; discogstagger is closer to the Python-CLI shape CLAUDE.md already names. Decide at integration design time. |
| **All-in-one capture+tag (not recommended for Audiopheliac scope):** Replace the manual flow entirely | vinyl-recorder or vinylflow | Defeats the Mentor's teaching arc. Available if the learning goal is complete and Gill wants throughput. |

---

## Integration with CLAUDE.md VINYL COLLECTION MANAGEMENT

CLAUDE.md VINYL COLLECTION MANAGEMENT section names a planned Discogs integration:
- Intake path: `Vinyl_Collection_Update_Queue.csv`
- Discogs collection endpoint: `/users/{username}/collection/folders/0/releases`
- Auth: single `Authorization: Discogs token={TOKEN}` header
- Note: "Personal access token for collection/wantlist sync; no OAuth required for single-user access"

That plan currently scopes Discogs as a COLLECTION-management integration (knowing what's in Gill's collection). It does NOT yet scope Discogs for RIP metadata (applying release data to a freshly-captured FLAC set).

**Recommended next step (when this lane becomes priority):** extend the VINYL COLLECTION MANAGEMENT scope to include a rip-tagging hook, decide between Kid3 or discogstagger as the back end, write a Python script that takes a path to a freshly-exported album folder and a Discogs release ID, fetches the metadata, writes tags to all FLACs in the folder, optionally downloads cover art, and updates `Vinyl_Collection_Update_Queue.csv`.

This is project work, not Mentor work. The Mentor teaches the manual flow; the project automates the manual flow once it's stable.

---

## Decision Defaults

Until Gill chooses otherwise:
- **Active stage tagging:** Audacity native metadata editor at FLAC export.
- **First library batch-tagging session:** Mp3tag (Windows GUI, fast).
- **Future Discogs integration design session:** revisit Kid3 vs discogstagger as the scriptable back end.

---

## When to Update This Doc

Update when:
- A tool in the survey is deprecated or replaced.
- A new tool meaningfully changes the landscape (Discogs API change, new FOSS project, etc.).
- The CLAUDE.md VINYL COLLECTION MANAGEMENT scope changes to include rip-tagging.
- Gill chooses a different default for any of the three stages above.

Source documents to keep in sync:
- `CLAUDE.md` VINYL COLLECTION MANAGEMENT.
- `docs/vinyl_capture_reference.md` (metadata field list at FLAC export).
- `skills/the-mentor/SKILL.md` Section 9 (file and archive discipline).

---

*Reference data. For workflow lessons, see `skills/the-mentor/SKILL.md`.*
