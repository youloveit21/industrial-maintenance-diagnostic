---
name: electrical-controls
description: Troubleshoot industrial control power, transformers, fuses, relays, contactors, sensors, solenoids, and AC/DC wiring. Use with the core skill when the failed sequence boundary is an electrical supply, signal, interface, or load circuit.
---

# Electrical Controls

Use `core-maintenance-diagnostic` and its output contract. Establish the schematic voltage, grounding/common scheme, device state, and control architecture before interpreting a reading.

Trace in this order: source -> disconnect/protection -> transformer or DC supply -> reference/common -> control device -> switching element -> conductor/terminal -> load -> return path.

## Measurement rules

- Voltage is measured between two named points. Never say only “check voltage on terminal X.”
- For a load that should energize, compare voltage across the load with each side to the documented reference. This distinguishes missing source, missing return, and open load/wiring.
- Validate low unexpected voltages for leakage, solid-state off-state current, capacitive coupling, high-impedance meters, shared commons, and backfeed before condemning a controller.
- For fuses and contacts, an energized voltage-drop test may be more decisive than continuity, but only when a qualified person can perform it safely. Otherwise isolate energy and test resistance.
- Check coils against their nameplate voltage/type. Do not assume AC/DC or suppressor polarity.
- A commanded output at the PLC does not prove voltage at the load; voltage at the load does not prove current or mechanical action.

## Common decisive splits

- Correct supply into protection but not out under load: protection/device/connection boundary.
- Correct voltage across an energized coil with no pickup: coil/mechanical assembly becomes likely after rating and frequency are confirmed.
- Correct voltage at output terminal but absent at load: downstream wiring/interface path.
- Voltage present on both load terminals to the same reference but near zero across the load: missing potential difference, often return/switching path.
- Sensor supply correct but output never changes at sensor: target/setup/sensor; output changes at sensor but not PLC terminal: wiring/input boundary.

Do not infer wire function from color alone. Use terminal labels, device markings, and the current as-built drawing.
