#!/usr/bin/env python3
"""Validate structural invariants for the Industrial Maintenance Diagnostic plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_MODULES = {
    "core-maintenance-diagnostic",
    "ai-psychiatry-diagnostic-guardrail",
    "electrical-controls",
    "plc-sequence",
    "machine-safety",
    "motors-vfds",
    "servos-encoders",
    "hydraulics",
    "pneumatics",
    "temperature-heaters",
    "injection-molding",
    "industrial-robots",
}
REQUIRED_HEADINGS = {
    "KNOWN",
    "EXPECTED",
    "SUSPECTED",
    "NEXT TEST",
    "METER SETTING",
    "TEST POINTS",
    "EXPECTED READING",
    "IF YES",
    "IF NO",
    "CONFIDENCE",
}


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    if manifest["name"] != ROOT.name:
        fail("Plugin folder and manifest name differ")
    if not re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]):
        fail("Plugin version is not strict semver")
    if "mcpServers" in manifest:
        fail("V1 must not activate an MCP server")

    skills_root = ROOT / "skills"
    found = {p.parent.name for p in skills_root.glob("*/SKILL.md")}
    missing = REQUIRED_MODULES - found
    if missing:
        fail(f"Missing required skills: {sorted(missing)}")

    for skill_file in skills_root.glob("*/SKILL.md"):
        text = skill_file.read_text()
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            fail(f"Invalid frontmatter in {skill_file.relative_to(ROOT)}")
        if "[TODO" in text:
            fail(f"Unresolved TODO in {skill_file.relative_to(ROOT)}")

    contract = (skills_root / "core-maintenance-diagnostic/references/output-contract.md").read_text()
    contract_headings = set(re.findall(r"^## (.+)$", contract, flags=re.MULTILINE))
    if not REQUIRED_HEADINGS.issubset(contract_headings):
        fail(f"Output contract missing: {sorted(REQUIRED_HEADINGS - contract_headings)}")

    cases = json.loads((ROOT / "tests/diagnostic-cases.json").read_text())["cases"]
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        fail("Duplicate diagnostic case IDs")
    if len(cases) < 10:
        fail("Behavior suite must contain at least 10 scenarios")
    for case in cases:
        for field in ("id", "module", "prompt", "evidence", "must", "must_not"):
            if not case.get(field):
                fail(f"Case {case.get('id', '<unknown>')} missing {field}")

    json.loads((ROOT / "knowledge/manuals/manifest.schema.json").read_text())
    json.loads((ROOT / "knowledge/manuals/index.example.json").read_text())
    print(f"Validated {len(found)} skills and {len(cases)} diagnostic scenarios.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, json.JSONDecodeError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
