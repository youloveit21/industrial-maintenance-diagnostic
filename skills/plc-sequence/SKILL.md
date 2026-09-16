---
name: plc-sequence
description: Trace PLC-controlled machine sequences, permissives, interlocks, timers, inputs, outputs, networks, and feedback. Use with the core skill when the failure involves logic state or the command-to-feedback sequence.
---

# PLC and Sequence

Use `core-maintenance-diagnostic`. Treat the PLC as one link in a physical control chain, not automatically as the cause.

Build a sequence table with step, required conditions, expected input states, logic result, expected output, physical action, feedback, timer, and actual state. Stop at the first divergence.

Trace:

`operator/automatic request -> safety and mode permissives -> physical input -> PLC input image -> logic/interlocks/timers -> PLC output image -> physical output -> interface/load -> feedback input`

## Rules

- Distinguish LED state, input image, tag value, logic continuity, output image, module LED, and measured field voltage. None alone proves the others.
- Record scan-dependent/intermittent faults with trends, timestamps, first-out logic, event logs, or safe high-speed capture when available.
- Check forces, overrides, inhibited routines, stale network data, ownership, run/program state, task execution, and configuration only when evidence points there.
- Timer not done is usually a symptom: identify which enable or reset condition prevents accumulation.
- An output instruction true with no physical output requires module/channel/configuration and field checks; a false instruction requires upstream logic/permissive tracing.
- Never advise online edits, forcing, bypassing, downloads, or clearing memory without authorization, backup, change control, and a defined rollback/verification plan.

For proprietary logic or status screens, cite the project/print or exact platform documentation. Ask for rung context above and below the highlighted instruction rather than diagnosing from one cropped bit.
