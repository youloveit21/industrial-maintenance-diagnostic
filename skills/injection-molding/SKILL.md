---
name: injection-molding
description: Diagnose injection-molding machine clamp, injection, screw, nozzle, ejector, core, hydraulic/servo, heater, safety, and process-sequence faults. Use with the core skill for molding machine alarms or failed machine actions.
---

# Injection Molding

Use `core-maintenance-diagnostic` plus the domain module matching the failed boundary. Obtain exact machine/OEM/controller model, serial, software version, alarm text/code, mold and setup identifiers, and whether the fault follows the machine, mold, material, program, or operating mode.

Build the actual cycle sequence, commonly: safety ready -> mold close stages -> clamp lock/tonnage -> injection unit/nozzle state -> injection/fill -> transfer/pack/hold -> cooling/plasticizing -> decompression -> mold open -> cores/ejectors -> robot handshake -> cycle reset. Adapt it to the exact machine and process; never assume this generic order overrides OEM logic.

## Function chains

- Clamp: request -> safeties/permissives -> close output/valve or servo -> pressure/position/speed -> low-pressure protect -> lock/tonnage -> closed feedback.
- Injection: enable -> safety valve/drive ready -> injection command -> valve/servo -> screw position/speed/pressure -> transfer -> hold feedback.
- Plasticizing: command -> rotation drive/hydraulic motor -> backpressure -> screw recovery position -> timeout.
- Cores/ejectors: mold position permissive -> sequence selection -> command -> valve/output -> motion -> end sensor/timer -> next-step permissive.
- Heaters: use `temperature-heaters`; robotics/handshake: use `industrial-robots`.

## Rules

- Treat process values, controller display scaling, engineering units, and calibrated physical readings separately.
- Preserve parameter backups before any change and record original/new values. Do not use parameter changes to hide a mechanical, electrical, hydraulic, or feedback fault.
- For mold-protect/low-pressure faults, investigate actual obstruction/friction and sequence/position evidence before raising pressure.
- Proprietary alarms and service parameters require exact OEM documentation. Do not infer a Toshiba/Shibaura, Engel, Arburg, Milacron/Fanuc, or other alarm from another family.
- Determine whether an alarm is initiating the stop or merely reported after another permissive/drive/pump/safety loss.

Verify manual functions, dry cycle where authorized, representative automatic cycles, part/process stability, mold protection, safety, and recurrence.
