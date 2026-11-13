# Documentation Index Contract

A useful searchable index should retain:

| Field | Meaning |
|---|---|
| id | Stable document or chunk identifier |
| path | Original repository path |
| title | Human-readable heading or symbol |
| kind | Function, class, interface, guide, README, or other type |
| language | Source language or document format |
| symbol | Qualified symbol name when applicable |
| content | Indexed text |
| source_revision | Commit or revision used to generate the entry |
| updated_at | Index generation time |

## Index quality
- Preserve source path and revision.
- Keep chunks small enough to retrieve but large enough to retain context.
- Avoid indexing generated output twice.
- Exclude secrets, binaries, vendored dependencies, and irrelevant build output.
- Refresh changed files and remove stale entries.
- Record parser failures rather than silently skipping files.

This is a suggested schema. Existing backends may use different field names.