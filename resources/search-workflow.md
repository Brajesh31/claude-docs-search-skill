# Documentation Search Playbook

## Query construction
Start with the exact symbol or error message. If that fails, search the containing module, a distinctive parameter, a user-facing concept, or related tests. Avoid broad queries until exact searches have been tried.

## Result evaluation
For each result, check:
- Correct project and version.
- Source document, generated API page, example, or stale cache.
- Whether it defines the exact symbol or only mentions it.
- Parameters, return values, errors, and side effects.
- Agreement with current source code.

## Reporting
Cite paths and line numbers where available. Separate verified behavior from inference. If documentation is outdated, identify the source file or version that should be checked next.