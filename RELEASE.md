# PyDeployCLI v1.1 Release

## 07/13/2026

## Improvements
All Improvements Were Done In Order:
- Any typos or errors were corrected, and consistency was restored across the code to keep good organization.
- Organization: I used f-string interpolation to organize variables.
- Optimization: I managed to reduce duplicate service control logic (if functions) using a simple helper function.
- An extra quit option was added to the main menu selection.
- Bug Fix: I used `textwrap` library using `dedent ` is used to remove leading whitespace.
  > The f-string used to generate the `systemd` unit file had a potential issue. I recently learned that triple-quoted strings preserve leading whitespace, so the generated `.service` file contained leading spaces on every line except `[Unit]`. Most systemd versions tolerate this, but older ones may not.
- README: I changed a bit of the wording and it's updated accordingly to the new v1.1 release.
