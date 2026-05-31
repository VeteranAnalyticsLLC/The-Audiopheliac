# Folder Migration — 2026-05-28

**This folder** was renumbered:

- **OLD path:** `C:\Users\gillo\The-Audiopheliac\`
- **NEW path:** `C:\Users\gillo\6. The-Audiopheliac\`
- **NAS counterpart:** `\\NAS87828E\The Audiopheliac\` (unchanged — NAS share names not numbered, see master map §3)

**Rationale:** Numerical prefix added for sort-ordering at gillo root. Position `6` reflects active personal/lifestyle build with regular sessions.

## Files Updated in Phase A (Cowork, 2026-05-28 first sweep)

- `CLAUDE.md` — Version bumped to 2026.05.3. All `C:\Users\gillo\The-Audiopheliac` references throughout the file (1000+ lines) updated to `C:\Users\gillo\6. The-Audiopheliac`. VAL paths renumbered. NAS Veteran Analytics LLC path renumbered.
- D-drive stale CLAUDE.md (`D:\The Audiopheliac\CLAUDE.md`) marked with deprecation banner pointing to canonical. Full deletion deferred to Rafa lane (Cowork cannot unlink NTFS).

## Files Updated in Phase A++ (Cowork, 2026-05-28 second sweep)

Per `/no-man-left-behind` invocation, the in-folder content sweep that was originally tagged for Phase B Rafa was folded into Cowork:

- `AGENTS.md` — Version bumped to 2026.05.3. Bulk replace_all of `C:\Users\gillo\The-Audiopheliac` → `C:\Users\gillo\6. The-Audiopheliac` and `C:\Users\gillo\Veteran Analytics LLC` → `C:\Users\gillo\1. Veteran Analytics LLC`. Reorg banner added.
- `console\README.md` — Paths updated.
- `prompts\rafa-phase4-plex-data-relocation-2026-05-27.md` — Paths updated. (Note: this file's existence itself violates the `[[feedback-handoff-prompts-in-chat-not-files]]` rule; flagged but content preserved.)
- `docs\Audiopheliac_Paperclip_Reference.md` — Paths updated. (Note: paperclip is deprecated per `[[feedback-do-not-revive-deprecated-tools]]`; this is reference-only historical content.)
- `docs\Audiopheliac_Website_Progress_v2026_04.md` — Paths updated.
- `docs\Audiopheliac_Domain_Registration.md` — Paths updated.
- `docs\Cloudflare_Domain_Registration_Audiopheliac.md` — Paths updated.
- `docs\FLAC_compatibility_with_Spotify.md` — Paths updated.
- `docs\Ableton_Live_12_Specs.md` — Paths updated.
- `docs\Instruction_Addendum_log.md` — Paths updated.
- `docs\brand\Canva_Brand_Kit_Paste_Sheet.md` — Paths updated.
- `docs\software\Spotify.md` — Paths updated.
- `docs\software\Roon.md` — Paths updated. (Note: Roon is deprecated per `[[feedback-do-not-revive-deprecated-tools]]`; this is reference-only historical content.)

Final verification grep (negative lookahead for already-numbered paths): no remaining un-numbered `C:\Users\gillo\The-Audiopheliac` or `C:\Users\gillo\Veteran Analytics LLC` strings anywhere in this folder except the intentional OLD→NEW pairs in this `MIGRATION_2026-05-28.md` file.

## Genuinely Deferred Items (Rafa lane required)

### 1. D-drive cleanup
- `D:\The Audiopheliac\CLAUDE.md` — orphan file, deprecation banner present from Phase A; full deletion requires NTFS unlink which Cowork cannot perform.
- `D:\The Audiopheliac\download_2026-05-05_17-43-19\CLAUDE.md` — additional orphan downloaded copy, also stale.
- `D:\The Audiopheliac\The-Audiopheliac\CLAUDE.md` and `D:\The Audiopheliac\The-Audiopheliac\Suno\CLAUDE.md` — these live inside the QSync mirror of `C:\Users\gillo\6. The-Audiopheliac\`. They will refresh automatically on the next QSync cycle once C-side updates propagate; verify after next sync rather than editing directly.

**Why Rafa-required:** D: is not mounted in Cowork workspace (Glob walks but Read/Edit/Write blocked).
**Rafa task:** `Remove-Item "D:\The Audiopheliac\CLAUDE.md"`, `Remove-Item "D:\The Audiopheliac\download_2026-05-05_17-43-19\CLAUDE.md"`, then verify QSync re-mirror.

### 2. GitHub clone(s) at `5. GitHub_Clones\the-audiopheliac\`

- `C:\Users\gillo\5. GitHub_Clones\the-audiopheliac\CLAUDE.md` — dated 2026-04-05, lags the canonical by 7+ weeks.
- `C:\Users\gillo\5. GitHub_Clones\the-audiopheliac\tender-wright-900476\CLAUDE.md` — worktree previously marked "removed" in AGENTS.md OPEN ACTION ITEMS but the directory still exists.

**Why Rafa-required:** Path-only patch would produce stale-content-with-new-paths hybrid. Correct fix is to commit canonical CLAUDE.md + AGENTS.md to `origin/main` from `6. The-Audiopheliac\`, then `git pull` in `5. GitHub_Clones\the-audiopheliac\`. Worktree prune is also Rafa-lane git lifecycle work.
**Rafa task:** (a) From `C:\Users\gillo\6. The-Audiopheliac\`: `git add CLAUDE.md AGENTS.md MIGRATION_2026-05-28.md`, commit, push. (b) From `C:\Users\gillo\5. GitHub_Clones\the-audiopheliac\`: `git pull`. (c) Inspect and prune `tender-wright-900476` worktree if dangling: `git worktree list`, `git worktree prune`, optional `Remove-Item -Recurse "tender-wright-900476"` if confirmed inactive.

See `C:\Users\gillo\MIGRATION_MASTER_2026-05-28.md` for the full migration map.
