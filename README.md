# Industrial Maintenance Diagnostic

An evidence-led Codex/ChatGPT plugin for industrial machine troubleshooting. It traces the expected machine sequence, finds the first failed step, and specifies one safe, decisive test before recommending parts.

## Version 1 scope

- Core diagnostic workflow and strict troubleshooting response contract
- AI Psychiatry-compatible investigation, evidence, root-cause, and reasoning-balance gates
- Modular skills for electrical controls, PLC/sequence, machine safety, motors/VFDs, servos/encoders, hydraulics, pneumatics, temperature/heaters, injection molding, and industrial robots
- Model-specific documentation priority and manual metadata design
- Scenario-based quality tests and project validation
- Future MCP and repair-history database specification, intentionally not activated in V1

## Required troubleshooting response

Every actionable repair response separates `KNOWN`, `EXPECTED`, `SUSPECTED`, `NEXT TEST`, `METER SETTING`, `TEST POINTS`, `EXPECTED READING`, `IF YES`, `IF NO`, and `CONFIDENCE`.

## Operating principle

`Identify -> sequence -> first divergence -> measure -> prove -> repair -> verify`

Exact as-built prints and exact-model OEM documentation outrank generic assumptions. A component is not condemned until the supply, command, path, load, feedback, test method, and credible alternatives are addressed as applicable.

## Repository layout

- `.codex-plugin/plugin.json` — plugin manifest
- `skills/core-maintenance-diagnostic/` — shared diagnostic engine and contract
- `skills/*/SKILL.md` — focused domain modules
- `knowledge/manuals/` — manual metadata/index structure; copyrighted source files are not bundled
- `docs/architecture.md` — V1 runtime design
- `docs/future-mcp-and-database.md` — later tool and data architecture
- `tests/diagnostic-cases.json` — behavior scenarios and required invariants
- `scripts/validate_project.py` — deterministic structural checks

## Validate

```bash
python3 scripts/validate_project.py
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

Behavioral quality should also be evaluated against the scenario rubric in `tests/README.md`; structural validation alone cannot prove diagnostic quality.

## Readiness and repair records

See [release readiness](docs/release-readiness.md) for completed work and remaining installation, documentation, and behavioral evaluation steps.

Use [the blank repair record](templates/repair-record.json) to capture a machine, symptom, measurements, hypotheses, repair, and verification separately from OEM manuals. See [record instructions](templates/README.md). This is a portable record template, not an active database or automatic memory service.
