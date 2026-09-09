# What this repo is

A deliberate quarantine for AI-generated files. It exists so that output from
Claude, Codex, and other models is kept **separate from real projects** and
cannot damage them.

## Rules for any Claude session working here

- **This repo is your entire scope.** Do not request, attach, or attempt to reach
  other repositories — in particular `ae47250/PathFinder`, which is intentionally
  off-limits. Access being denied is the design, not a misconfiguration to fix.
- **Nothing here is production.** Files land here to be reviewed, verified, and
  then hand-carried elsewhere by the user. Do not assume anything here is wired
  into a running system.
- **This session cannot read the user's Mac.** Cloud sessions have no filesystem
  access to local machines. Local paths the user mentions (e.g.
  `/Users/agust/Developer/Projects/...`) are text, not something to open. If work
  requires local files, say so plainly and early — the user can start a local
  session instead, which does have that access.

## What's currently in here

**PathFinder / Purdue program-card extraction** — 116 Purdue majors turned into
structured program cards for a major-recommendation tool:

- `restOfMajorsSources (3).json` — frozen, authoritative source evidence. All
  citations in the finished cards point at this file by name.
- `restOfMajorsSources.json` — older working copy of the same effort, kept for
  history. Superseded by `(3).json`.
- `restOfMajorsClaude.final.json` — the 116 finished cards.
- `restOfMajorsClaude.audit.json` / `.audit.md` — record of every judgment call.
- `restOfMajorsClaude.handoff.json` — checksums and provenance for verification.

**Unrelated tree-service extraction eval data** — `500-complete-messy-inputs*`,
`recommended-live-api-sample.jsonl`, `tree_mess_100_observations.jsonl`,
`td2-complete-cases-500-generator.py`. Not connected to the PathFinder work.

## Note

General behavior expectations (how to guide, how much to explain, when to check
before concluding) live in the user's account-level Memory, not here. This file
covers only what is specific to this repository.
