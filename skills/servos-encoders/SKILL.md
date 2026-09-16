---
name: servos-encoders
description: Diagnose servo drives, motors, encoders/resolvers, brakes, homing, synchronization, and motion errors. Use with the core skill for servo alarms, lost position, following error, axis faults, or motion only failing under load.
---

# Servos and Encoders

Use `core-maintenance-diagnostic`. Identify exact drive, motor, feedback type, axis, controller, firmware, alarm history, and the motion phase at failure.

Trace: safety/STO -> control power -> drive ready -> enable -> command/trajectory -> power stage -> motor/brake/load -> feedback device/cable -> actual position/speed -> following-error and limit logic.

## Diagnostic distinctions

- Fault at enable: prioritize STO, control/power readiness, brake, feedback validity, phase/commutation, and configuration.
- Fault at motion start: prioritize command direction, brake release, binding, limits, tuning, motor/cable, and feedback response.
- Fault only under load/speed: prioritize mechanical load, torque/current limit, bus sag/regeneration, thermal state, feedback noise, and tuning—without adjusting tuning first.
- Position drift/jump: correlate command, actual position, raw feedback diagnostics, cable movement, grounding/shielding, coupling, and mechanical slip.
- Homing failure: trace home request, search direction/speed, sensor transition at both field and controller, index/reference capture, offset, travel limits, and timeout.

Never disconnect feedback or motor connectors energized. Do not perform megohm tests through feedback electronics. Never reset encoder position, reload parameters, autotune, or change commutation until the current configuration is backed up and the exact OEM procedure is confirmed.

Calling an encoder bad requires evidence at the feedback boundary and exclusion of supply, connector/cable, shielding, coupling, configuration, and mechanical movement.
