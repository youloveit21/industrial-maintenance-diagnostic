# Evidence and conclusion rules

## Investigation floor

Before recommending a part replacement or adjustment, establish as much of this minimum as the situation permits:

1. exact asset/component identity
2. precise symptom and reproducible machine state
3. expected sequence and first observed divergence
4. relevant energy source and command path
5. at least one observation at, or immediately around, the failed boundary

If an item is missing, say so and select a test or identification step that closes the most important gap.

## Evidence floor

Treat a cause as no stronger than `possible` when it rests only on symptom similarity, a forum report, an unexplained voltage, an unverified alarm definition, or a component's physical proximity to the fault.

To reach `likely`, normally require at least two independent, mutually consistent facts or one decisive isolation test, with no unresolved contradiction that would change the repair.

To reach `confirmed`, require direct isolation or substitution evidence, a documented diagnostic result, or a reproducible before/after repair verification that rules out the credible upstream alternatives. Substitution is evidence only when configuration, compatibility, wiring, and the substituted item's known-good status are established.

## Root-cause validator

For any proposed root cause, record:

- claim: the specific failed condition, not merely a part name
- supporting evidence
- conflicting or missing evidence
- mechanism connecting the cause to the exact symptom and sequence point
- discrimination: why nearby alternatives do not explain the evidence as well
- verification: how the repair will prove or disprove the claim

If the mechanism cannot be stated, the conclusion is premature.

## Reasoning balance

- Investigate when identity, sequence, or decisive evidence is missing.
- Test when competing hypotheses predict different observable results.
- Act when evidence meets the repair threshold and the action is proportionate and safe.
- Verify when a repair or change has been made.
- Stop expanding hypotheses when a decisive result resolves the failed boundary.
- Change diagnostic strategy when repeated tests interrogate the same point without adding information.

## Board and module condemnation gate

Before condemning an electronic board or PLC I/O module, verify as applicable:

- correct supply rails and reference/common under load
- controller state, command, enable, configuration, addressing, and relevant diagnostics
- field wiring/load disconnected or isolated by an approved method
- output behavior measured both at the module and downstream interface
- leakage/ghost voltage evaluated with an appropriate low-impedance method when safe
- shorted/overloaded load and transient suppression checked
- expected behavior confirmed from the exact manual or schematic

## Completion evidence

A repair is not complete merely because an alarm clears. Verify the original operating condition, several representative cycles, relevant safety functions, expected feedback and process values, and no new faults. Record what changed and the evidence that the original cause was removed.
