---
name: motors-vfds
description: Troubleshoot industrial motors and variable-frequency drives, including power, commands, references, STO, faults, output, braking, and mechanical load. Use with the core skill when a motor will not run, runs incorrectly, trips, or lacks torque.
---

# Motors and VFDs

Use `core-maintenance-diagnostic`. Capture exact drive/motor nameplates, topology, fault code and timestamp, command source, speed reference source, control mode, and whether the fault occurs at enable, acceleration, steady load, deceleration, or stop.

Trace: incoming power -> DC bus/precharge -> drive ready/STO -> run enable/direction -> speed/torque reference -> drive output -> motor cable -> motor -> brake/coupling/load -> speed/current feedback.

## Rules

- Retrieve the exact drive manual before defining a fault code or parameter.
- Compare commanded frequency/speed, actual output frequency, output current, DC bus, torque/load indication, and motor motion.
- Separate “drive receives command,” “drive reports running,” “output voltage/frequency exists,” and “motor develops torque.”
- Check mechanical brake release voltage and air gap where applicable before calling a motor bad.
- For overcurrent, ground fault, or overload, separate motor/cable insulation, acceleration/deceleration, load jam, brake, tuning, and drive power-stage causes with approved isolation tests.
- Ordinary handheld meters can misread PWM outputs. Follow the drive manufacturer's test method and instrument requirements.
- Do not megger through a connected drive, encoder, thermistor, or electronics. Isolate per OEM procedure.
- Parameter changes require a backup, exact original/new values, documented reason, authorization, and rollback.

Verification includes direction, speed range, current under representative load, acceleration/deceleration, braking, thermal behavior, and fault recurrence.
