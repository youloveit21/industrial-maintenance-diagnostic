# Troubleshooting output contract

Use these headings in this order. Keep confirmed observation separate from interpretation.

## KNOWN

Only directly reported or observed facts, exact documentation, and valid measurements. Include the machine state and measurement reference when relevant. Do not promote an inference into this section.

## EXPECTED

The documented or engineering-expected event at the first failed sequence step. Identify the source when model-specific.

## SUSPECTED

A short ranked set of falsifiable hypotheses. State the evidence for and against each. Use `unknown` when the current facts do not justify ranking.

## NEXT TEST

One safe, decisive action. Include required machine state: power isolated, controls energized, manual/jog, cycle command active, stationary, unloaded, or other exact condition.

## METER SETTING

Specify `AC V`, `DC V`, `ohms`, `continuity`, `Hz`, `current`, `diode`, `scope`, `pressure`, `temperature`, or `N/A`. Include an appropriate range and instrument category/rating when relevant. Never specify resistance or continuity on an energized circuit.

## TEST POINTS

Name both leads/connections or the exact observation points. Prefer terminal/device labels from the supplied print. Do not guess terminal numbers or wire colors. State which lead is the reference and where it lands.

## EXPECTED READING

Give the documented nominal value plus tolerance/range when known. Otherwise state the expected state and label it as an engineering expectation. Account for control type, switching method, machine state, and reference point.

## IF YES

Define the actual pass condition and exactly what it confirms, what it only supports, and what remains unproven.

## IF NO

Define the actual fail/alternate condition and exactly which section of the chain becomes suspect. Do not automatically condemn the device at the test point.

## CONFIDENCE

Use one label and a short reason:

- `confirmed`: direct, reproducible evidence isolates the cause and contradictory evidence is resolved
- `likely`: multiple consistent facts support it, but one important isolation or verification remains
- `possible`: plausible with limited or ambiguous evidence
- `unknown`: identity, sequence, documentation, or measurement evidence is insufficient

When the user returns a reading, update the same structure and choose the next single test. After repair, add `REPAIR VERIFICATION` with repeat cycles, full-sequence result, safety checks, and whether the original fault recurred.
