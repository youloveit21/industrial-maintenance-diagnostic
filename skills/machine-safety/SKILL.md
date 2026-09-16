---
name: machine-safety
description: Diagnose industrial safety gates, E-stops, safety relays/PLCs, dual channels, contactor feedback, reset circuits, and safe motion interlocks. Use with the core skill for a safety fault or missing safety permissive.
---

# Machine Safety

Use `core-maintenance-diagnostic`. Preserve the designed safety function throughout diagnosis. Never propose a production bypass or defeat.

Trace: safety demand devices -> both channels -> input terminals -> safety logic/configuration -> reset/start interlock -> safety outputs -> contactors/valves/drives -> external-device monitoring/feedback -> machine permissive.

## Diagnostic controls

- Identify the exact safety device, relay/PLC model, wiring architecture, manual/automatic reset behavior, and diagnostic code.
- Compare channels separately and look for simultaneity/discrepancy faults, cross-shorts, shorts to 24 V/common, welded contacts, and feedback loops that fail to return.
- A closed gate switch does not prove both channels reach the safety controller.
- A safety output LED does not prove downstream contactors, safe torque off channels, dump valves, or feedback contacts changed state.
- Treat reset behavior as part of the safety design; do not jumper reset or substitute ordinary PLC logic.
- After repair, validate every affected safety function according to OEM/site procedures, including stop behavior, reset, restart prevention, and diagnostics.

Keep safety-controller replacement/configuration at `possible` until field circuits, supplies, discrepancy conditions, configuration identity, and diagnostics are checked.
