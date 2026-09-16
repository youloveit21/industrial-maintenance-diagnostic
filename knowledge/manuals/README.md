# Focused manual library

Do not place unrelated file collections here. Add only documentation that is legally available to the user and relevant to supported assets.

Organize source files outside Git when licensing, confidentiality, or size requires it. Track their metadata in an index conforming to `manifest.schema.json`.

Recommended logical path:

`manufacturer/product-family/model/controller/revision/document`

Required metadata includes title, OEM, document number, revision/date, applicable models/controllers/firmware, language, source URL or internal URI, checksum, and verification status.

Rules:

- Preserve the original file; do not rewrite it as if it were OEM content.
- Record OCR status and page numbering differences.
- Keep superseded revisions but mark their status and applicability.
- Search exact model/controller/revision first.
- Cite page, section, figure, table, or drawing coordinate in diagnostic responses.
- Treat community material as a lead, not as an authoritative manual.
- Never commit confidential plant prints, credentials, or restricted OEM files to a public repository.
