# Public boundary

A useful internal library and a public repository are not the same thing. Public export is a separate, stricter decision.

## Never publish from this library by default

- final videos, drafts, review exports, full project folders, or production packages;
- raw voiceover, source audio, music, fonts, and downloaded media unless their redistribution rights are clear;
- student, client, collaborator, platform, account, browser, or device data;
- tokens, keys, cookies, local configuration, absolute local paths, and logs that can expose them;
- third-party references, screenshots, tutorials, or material labelled external-reference;
- assets marked pending-verification, restricted, or historical-path-missing;
- project-specific claims, numbers, names, or conclusions that will become misleading outside their original context.

## An item can become public only when all four questions are yes

1. **Rights** — may the code, document, or asset be redistributed under the intended license?
2. **Privacy** — does it avoid people, accounts, project history, and hidden machine information?
3. **Portability** — can someone outside the original workspace understand and use it without private dependencies?
4. **Context** — will it still be truthful after names, facts, and visuals are separated from the original project?

Write down the review in the asset record. A passing automated scan cannot answer these questions for you.

## Before pushing

1. Run the public-release validator.
2. Read every file that is about to be added; do not rely only on filenames.
3. Confirm no media, archives, or project exports slipped in.
4. Confirm the repository description and README describe methods and templates, not private work as public stock.
