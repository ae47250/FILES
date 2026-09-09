# FILES

This repo is a general-purpose data/working-files store for @ae47250. It holds two unrelated sets of content:

## PathFinder / Purdue program-card extraction

Source-evidence and finished output for a project that turned Purdue University (West Lafayette) undergraduate program requirements into structured "program cards" for the PathFinder major-recommendation tool.

- **`restOfMajorsSources (3).json`** — frozen, authoritative source-evidence file for 116 Purdue majors (the "remaining" majors not already covered elsewhere). Contains program descriptions, required-course sequences, and verbatim requirement text collected from Purdue's official catalog and department pages, with citations for every claim.
- **`restOfMajorsSources.json`** — an earlier working copy of the same kind of source-collection effort, kept for history. `(3).json` supersedes it; new work should use `(3).json`.
- **`restOfMajorsClaude.final.json`** — the finished deliverable: 116 reviewed PathFinder program cards built from the source-evidence file above, each with concept tags and 19 scored characteristic fields, all backed by cited evidence.
- **`restOfMajorsClaude.audit.json`** — machine-readable record of every judgment call made while building the cards: concept changes vs. the prior reviewed baseline, field-value distributions, flagged inconsistencies, per-program notes.
- **`restOfMajorsClaude.audit.md`** — the same audit content as a readable report.
- **`restOfMajorsClaude.handoff.json`** — closing manifest: SHA-256 checksums for the four files above, source provenance, summary counts, and an explicit list of items left unresolved, so the work can be independently verified without redoing it.

## Unrelated: tree-service data-extraction eval sets

A separate, unrelated batch of test/evaluation data for a "messy customer intake" text-extraction task (parsing garbled tree-service job requests into structured fields like customer name, phone, quote amount). Not connected to the PathFinder work above.

- `500-complete-messy-inputs.jsonl`, `500-complete-messy-inputs-local-helper-results.jsonl`, `500-complete-messy-inputs-local-helper-summary.json`
- `recommended-live-api-sample.jsonl`
- `tree_mess_100_observations.jsonl`
- `td2-complete-cases-500-generator.py`
