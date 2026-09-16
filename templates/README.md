# Repair record template

Copy `repair-record.json` into private storage for each diagnostic session. Within a local checkout, `records/private/` is ignored by Git; this does not encrypt files or protect previously committed files. Keep actual plant records out of this public repository.

- Null means unknown or not recorded, not zero or a successful result.
- Use stable IDs and ISO 8601 dates/times with time zones.
- Add one measurement object per reading. Include operating state, instrument setting, both test points/reference, units, and the source for an expected range.
- Keep observations and hypotheses separate. Confidence is `unknown`, `possible`, `likely`, or `confirmed`; it is not a calculated probability.
- Link sources by document ID, revision, page/section, and applicability. Keep the actual manuals in the separate document store.
- Preserve original readings. Record corrections and parameter changes with date, reason, and original/new values.
- Set session status to `verified` only after recording the original fault's verification result and relevant sequence/safety checks. Otherwise use `open`, `awaiting-evidence`, or `repaired-unverified`.

The blank entries show the record shape. Duplicate them as needed or remove unused entries. This template is not a validated database schema and does not save anything automatically.
