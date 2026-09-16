---
name: temperature-heaters
description: Diagnose industrial temperature loops, thermocouples/RTDs, controllers, SSRs/contactors, heaters, fuses, wiring, cooling, and runaway heat. Use with the core skill for no heat, overheat, unstable temperature, sensor errors, or repeated heater-circuit failures.
---

# Temperature and Heaters

Use `core-maintenance-diagnostic`. Identify sensor type, controller model, supply/load voltage, output type, heater configuration, setpoint, process value, output percentage, alarm state, and zone wiring.

Trace: setpoint/mode -> measured temperature -> control error/PID demand -> controller output -> SSR/contactor -> branch protection -> heater voltage/current -> heat transfer/process -> sensor response -> cooling output.

## Rules

- Separate displayed output percentage, physical control output, switching-device state, heater voltage, heater current, and actual heat.
- Low voltage measured with output “off” may be SSR leakage, snubber current, capacitive coupling, or meter impedance. Validate with the OEM method or appropriate load/low-impedance measurement before condemning a board.
- A heater can show nominal resistance cold yet fail hot or to ground; use resistance, current balance, insulation test, and thermal behavior as appropriate, with electronics isolated.
- Sensor polarity, extension wire type, junction location, grounding, open-sensor behavior, and channel configuration matter. Do not substitute ordinary copper wire in thermocouple paths without engineering approval.
- Runaway heat: determine whether controller demand is off while current continues. If so, inspect stuck SSR/contactor, miswiring/backfeed, and output architecture; if demand remains on, investigate mode/tuning/sensor/process feedback.
- Repeated fuse failure requires heater branch isolation, cold/hot current, ground leakage, wiring movement, moisture, and fuse type/rating evidence—never a larger fuse as diagnosis.

Verification includes heat-up, stable control, output/current cycling, overtemperature protection, cooling behavior, and representative production conditions.
