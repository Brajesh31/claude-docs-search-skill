---
name: docs-search
description: Find relevant API references, symbols, guides, and generated documentation in an indexed codebase. Use before implementing changes when project-specific signatures or conventions need verification.
---

# Codebase Documentation Search

## Purpose
Search documentation generated from a codebase, including API references, symbol descriptions, comments, guides, and project notes. Distinguish indexed evidence from guesses.

## Search workflow
1. Identify the available index or search backend, its location, supported types, and freshness metadata.
2. Translate the request into exact identifiers, concepts, and likely document types.
3. Search exact names and keywords first.
4. Search related types, modules, examples, and guides.
5. Retrieve the full matching document or source section.
6. Verify signatures, parameters, return types, examples, and version context.
7. Compare documentation against source code when correctness matters.
8. Report paths, document IDs, relevant details, and uncertainty.

## Search modes
- Exact identifier: function, class, method, module, endpoint, or configuration key.
- Keyword: phrase or domain concept.
- Type filter: function, class, interface, component, module, guide, or README.
- Related search: synonyms and adjacent API concepts.
- Freshness check: determine whether the indexed entry predates relevant source changes.

## Evidence rules
- Never invent a function signature or API behavior.
- Flag stale or incomplete documentation.
- A search snippet is not a complete API contract.
- If no result is found, say so and suggest a narrower query or indexing the relevant source.
- Do not modify an index unless the user asks for indexing or refresh.

## Local fallback
scripts/search_docs.py performs simple keyword matching across local text and source files. It is not semantic search and does not replace a dedicated indexed backend.

## Output
Return the best matching references, why they match, verified details, and any uncertainty about version or freshness.