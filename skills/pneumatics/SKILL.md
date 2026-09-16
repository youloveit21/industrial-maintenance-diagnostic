---
name: pneumatics
description: Troubleshoot industrial compressed-air supply, FRLs, valves, cylinders, vacuum, pressure switches, and flow controls. Use with the core skill for absent, weak, slow, erratic, or leaking pneumatic motion.
---

# Pneumatics

Use `core-maintenance-diagnostic`. Trace: plant supply -> isolation/dump valve -> FRL/regulator -> machine manifold -> pilot/solenoid command -> valve spool -> cylinder/vacuum device -> exhaust/flow controls -> end-position or pressure feedback.

## Rules

- Measure dynamic pressure at the relevant point during the failed action; static supply alone does not prove flow capacity.
- Verify dump/soft-start valve state and pilot pressure before blaming downstream devices.
- At a cylinder, compare pressure at both ports during command and observe exhaust. This separates command/valve/flow issues from binding, load, or internal leakage.
- Slow motion can come from supply restriction, meter-out settings, clogged silencers, undersized tubing, leaks, sticky valves, lubrication/seal condition, or mechanical load.
- Vacuum diagnosis must identify ejector/pump type, supply pressure/flow, vacuum level at source and cup, leaks, filters, part porosity, and vacuum-switch threshold.
- Do not use hands to search for high-pressure leaks; use approved methods.
- Isolate and exhaust pressure, secure loads, and account for trapped pressure before disconnecting tubing or actuators.

Do not condemn a solenoid valve from coil voltage alone; prove pilot/spool response and pressure path.
