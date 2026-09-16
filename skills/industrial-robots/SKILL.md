---
name: industrial-robots
description: Diagnose industrial and injection-molding robots, axes, home positions, traverse faults, grippers, controller I/O, interlocks, and machine handshakes. Use with the core skill for robot alarms, lost position, failed motion, or cell-sequence faults.
---

# Industrial Robots

Use `core-maintenance-diagnostic` and `servos-encoders` when the failed boundary is motion feedback. Identify robot manufacturer/model/controller/software, axis, program/job, tool, exact alarm, operating mode, and cell state.

Separate the robot's internal sequence from the machine handshake:

`cell safety -> robot ready/auto -> machine permission -> program step -> axis command -> motion complete -> tool action -> part confirmation -> clear-of-mold/safe-zone -> machine release`

## Rules

- Map each handshake signal in both controllers: source, destination, normal state, transition, timeout, and physical meaning.
- A signal shown ON at the sender does not prove it arrives at the receiver. Check field/network status at both ends and timing.
- For home/traverse faults, distinguish taught home coordinates, home sensor/reference, mastering/calibration, software zone, hard limit, drive feedback, and mechanical position.
- Do not reteach positions, reset mastering, change payload, or clear servo data until current values and backups are secured and the exact OEM recovery is known.
- For gripper/vacuum faults, trace output -> valve/vacuum source -> tool action -> part sensor/pressure switch -> program confirmation.
- A different program producing the same axis alarm points toward shared hardware/configuration/feedback, but does not prove which component failed.
- Recovery motion requires controlled mode, reduced speed where required, clear cell, authorized personnel, and OEM/site procedure. Never defeat cell safety.

Verify correct program, home/reference, all affected paths, handshakes, tool confirmation, safe zones, automatic cycles, and restart behavior.
