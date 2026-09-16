# Version 1 readiness

## Implemented

- Core diagnostic skill, strict response contract, and evidence gates.
- Ten domain modules plus the AI Psychiatry-compatible guardrail skill.
- Exact-document source priorities and manual metadata format.
- Ten behavioral scenario definitions and a scoring rubric.
- Structural validation script and GitHub validation workflow.
- Portable blank repair record, separate from the manual index.
- Future MCP/database design; no active server or database.

## Remaining before claiming operational readiness

1. Install the plugin in the intended client and verify discovery and invocation. A GitHub upload is not installation. Record the client, plugin revision, and result; client-specific installation instructions should be verified at that time.
2. Add authorized OEM documents for the actual machine/controller/firmware, with revision, applicability, and page citations. The example manual index contains no real manual.
3. Run all ten scenarios in fresh plugin-enabled sessions and score actual responses using `tests/README.md`. Save the responses, model/client version, plugin commit, scores, and hard failures. Structural checks validate definitions, not diagnostic performance.
4. Run supervised trials against resolved, redacted maintenance cases. Check measurement references, conflicting evidence, and repeatability before relying on conclusions in the field.

## Later work, intentionally deferred

- Authenticated retrieval and persistent repair history through the planned MCP/database.
- A separately deployed interactive website, if requested; this repository currently packages skills.
- Distribution/license choice before a broader release. A public repository alone is not an explicit open-source license.

## Repository cleanup

The generic `.github/workflows/blank.yml` starter printed “Hello, world!” and did not validate the plugin. It was removed. `.github/workflows/validate.yml` remains the real project check. No website theme files were found on the main branch during this review.
