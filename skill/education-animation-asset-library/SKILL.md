---
name: education-animation-asset-library
description: Manage reusable elements and templates for education explainer animation. Use when Codex needs to search, classify, document, reuse, migrate, or safely publish visual components, motion patterns, subtitle rules, prompts, audio fragments, production contracts, or Remotion templates from education-video projects.
---

# Education Animation Asset Library

Keep the reusable parts of a teaching video easy to find without treating every finished video as a source pack. Search before making, record a component before copying it, and keep source, rights, and use conditions attached to every library entry.

## Choose a route

Use one route at a time. Read [references/route-selection.md](references/route-selection.md) before planning an import or a new build.

- **VOX paper collage**: use for detachable paper-cut elements, depth-layer plans, motion grammar, prompt structures, and scene contracts.
- **Editorial magazine explainer**: use for semantic components, component-contained text, caption layers, scene contracts, and Remotion structures.

For a full editorial-magazine production workflow, hand the selected records to [muzhi-editorial-magazine-skill](https://github.com/JasperMZ-Zcy/muzhi-editorial-magazine-skill). That Skill makes and checks the video; this Skill makes its reusable building blocks searchable and safe to carry forward.

## Work in this order

1. **Search first.** Read the local index and identify the route, topic, function, source, and intended use. Prefer a good existing component over a visual near-duplicate.
2. **Decide whether it belongs.** Keep only pieces that can stand on their own: visual parts, templates, motion rules, caption structures, prompt patterns, sound fragments with clear rights, or production contracts. Leave finished videos, full project packages, raw narration, account data, and source material with uncertain sharing rights in their original project.
3. **Create an asset record.** Start from [assets/templates/asset-record.template.json](assets/templates/asset-record.template.json). Preserve source-project reference, route, function, reuse conditions, rights state, and public-export state.
4. **Keep the file and its record together.** Place a reusable file in the appropriate library category and give the record a stable asset_id. Do not replace a source project file; copy only after the source is known to be reusable.
5. **Reuse deliberately.** Read the record's reuse_conditions before using it. Adapt wording, data, and composition to the new topic; do not carry stale factual content, brand material, or project-specific conclusions into another project.
6. **Validate before a public export.** Read [references/public-boundary.md](references/public-boundary.md), then run the public-release validator. A clean scan is necessary but not sufficient: publish only material whose rights and context are genuinely clear.

## Record the minimum useful facts

Use the fields explained in [references/asset-records.md](references/asset-records.md). At a minimum, every record needs:

- route and asset type;
- concise purpose and searchable tags;
- source-project reference;
- a clear reuse condition;
- rights status;
- public_export_eligible set to false until an individual review clears it.

Use [assets/templates/scene-contract.template.json](assets/templates/scene-contract.template.json) for an adaptable scene handoff. The two Remotion examples show a generic component scene and caption layer; copy their structure, not their subject matter.

## Hard boundaries

- Keep final renders, complete project exports, raw narration, unlicensed music, student information, platform back-office data, credentials, browser profiles, and external-reference assets out of a public export.
- Treat pending-verification, external-reference, and historical-path-missing as private-library states. They are not public assets.
- Do not declare an item public merely because it is technically easy to copy. Rights, privacy, context, and portability must all be clear.
- Do not generate replacement media to fill a missing record. Record the absence honestly and keep the source link if appropriate.

## Validate

Run these checks after editing a record or preparing a release:

~~~powershell
python scripts\validate_asset_record.py assets\templates\asset-record.template.json
python scripts\validate_asset_record.py --self-test
python scripts\validate_public_release.py ..\..
~~~

If a project needs the magazine-explainer production path after the library search, invoke the editorial-magazine-explainer-producer Skill with the selected record IDs and their reuse conditions.
