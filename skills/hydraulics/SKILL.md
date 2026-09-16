---
name: hydraulics
description: Troubleshoot hydraulic pumps, pressure/flow, valves, cylinders, accumulators, proportional controls, and machine motion. Use with the core skill when a commanded hydraulic function is weak, absent, erratic, hot, noisy, or pressure-faulted.
---

# Hydraulics

Use `core-maintenance-diagnostic`. Obtain the hydraulic schematic, fluid/temperature condition, pump type, pressure ratings, command state, load direction, and safe gauge/test ports.

Trace: reservoir/condition -> suction -> prime -> pump/coupling -> unloading/compensation -> system pressure and flow -> directional/proportional valve -> work-port pressure -> actuator/load -> return/backpressure -> position/pressure feedback.

## Rules

- Pressure is resistance to flow, not proof of adequate flow. Interpret pressure at named ports and exact machine states.
- No movement with pressure requires comparison of supply, work ports, return, load, and valve command; it does not alone prove a bad valve or cylinder.
- Fast pressure rise/trip may indicate blocked motion, closed path, incorrect valve state, brake/lock, relief/compensator setting, transducer error, or timing.
- Low pressure may result from low command, unloading, relief leakage, pump wear, suction restriction/aeration, internal leakage, or insufficient drive speed.
- Verify electrical command at a proportional/solenoid valve before entering hydraulic disassembly; then verify spool/driver diagnostics and pressure response.
- Temperature and contamination are evidence: record oil temperature, level, appearance, filter indicators, noise, and changes from normal.
- Adjustments to reliefs, compensators, or proportional gains require the exact OEM procedure and baseline settings. Never turn an adjustment simply to see what happens.

Use rated gauges/hoses and remote observation where required. Depressurize and secure stored/gravity energy before opening a line.
