---
name: ai-psychiatry-diagnostic-guardrail
description: Apply AI Psychiatry investigation, evidence, root-cause, and reasoning-balance controls to industrial maintenance diagnoses. Use with the core maintenance diagnostic when a repair conclusion, component condemnation, or troubleshooting direction needs validation.
---

# AI Psychiatry Diagnostic Guardrail

Use the Core Maintenance Diagnostic evidence ledger as the shared state. When the AI Psychiatry plugin is installed, apply its `investigation-floor`, `evidence-floor`, `root-cause-validator`, and `reasoning-balance` skills as validation passes. This skill defines the maintenance translation and remains usable if that plugin is unavailable.

## Gate order

1. **Investigation Floor:** Do we know the exact asset, symptom, machine state, expected sequence, and first failed step? If not, collect the highest-value missing fact.
2. **Evidence Floor:** Does each asserted fact have a valid observation, reading, print/manual citation, diagnostic state, or repeatable behavior? Downgrade unsupported claims.
3. **Root Cause Validator:** Does the proposed cause explain the timing, sequence boundary, all material evidence, and the failure mechanism better than credible alternatives?
4. **Reasoning Balance:** Choose `investigate`, `test`, `act`, `verify`, or `stop`. Do not continue generating causes after a decisive result; do not act while a decisive safe test remains undone.

## Required challenge before component condemnation

Ask internally:

- Could missing power, common/reference, enable, permissive, wiring, configuration, load, or feedback create the same symptom?
- Was the reading taken across the correct two points in the correct machine state with an appropriate instrument?
- Is the expected value documented for this exact model/revision or merely assumed?
- Does an independent observation support the claim?
- What result would falsify the diagnosis?

If the answer exposes a material gap, keep confidence at `possible` or `unknown` and make that gap the next test.

## No theater

Do not mention AI Psychiatry skill names in the repair response unless useful to the user. Show the result through clean separation of facts, hypotheses, decisive testing, calibrated confidence, and verification.
