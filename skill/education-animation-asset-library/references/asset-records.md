# Asset records

An asset record is the small piece of context that keeps a reusable file from becoming an anonymous file with a good name.

## Required fields

| Field | What to record |
| --- | --- |
| asset_id | Stable, human-readable identifier. Do not recycle it. |
| title | What the asset does, not just what it looks like. |
| route | vox-paper-collage or editorial-magazine-explainer. |
| asset_type | For example visual-element, motion-template, caption-template, prompt-template, production-contract, or remotion-template. |
| purpose | The explanation or production problem it solves. |
| source_project | A source-project reference that stays inside the private library when necessary. |
| reuse_conditions | What may change, what must be checked, and where it should not be used. |
| rights.status | cleared, pending-verification, external-reference, or restricted. |
| public_export_eligible | Start with false; change only after an individual review. |
| tags | Route, function, visual family, and subject-neutral search terms. |

## Useful optional fields

- dependencies: files, fonts, packages, or runtime assumptions;
- search_text: a short natural-language description for keyword search;
- availability: use present, historical-path-missing, or another honest state;
- reviewed_at and reviewed_by: record the last ownership/privacy review;
- notes: short explanation of non-obvious reuse limits.

## Examples of good titles

- “Three-step comparison card with editable labels”
- “Safe-zone caption layer for vertical explainers”
- “Paper-cut reveal contract for a cause-to-result transition”

Avoid titles that only say “asset 12,” “new component,” “nice picture,” or the original video title.
