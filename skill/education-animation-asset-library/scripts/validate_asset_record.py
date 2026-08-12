#!/usr/bin/env python3
"""Validate the portable asset-record format used by this Skill."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "asset_id": str,
    "title": str,
    "route": str,
    "asset_type": str,
    "purpose": str,
    "source_project": str,
    "reuse_conditions": list,
    "rights": dict,
    "public_export_eligible": bool,
    "tags": list,
}

ALLOWED_ROUTES = {"vox-paper-collage", "editorial-magazine-explainer"}
ALLOWED_RIGHTS = {"cleared", "pending-verification", "external-reference", "restricted"}


def validate(record: object) -> list[str]:
    if not isinstance(record, dict):
        return ["record must be a JSON object"]

    errors: list[str] = []
    for key, expected_type in REQUIRED_FIELDS.items():
        value = record.get(key)
        if not isinstance(value, expected_type) or (expected_type is str and not value.strip()):
            errors.append(f"{key} must be a non-empty {expected_type.__name__}")

    if record.get("route") not in ALLOWED_ROUTES:
        errors.append(f"route must be one of: {', '.join(sorted(ALLOWED_ROUTES))}")

    conditions = record.get("reuse_conditions")
    if isinstance(conditions, list) and not all(isinstance(item, str) and item.strip() for item in conditions):
        errors.append("reuse_conditions must contain non-empty strings")
    elif isinstance(conditions, list) and not conditions:
        errors.append("reuse_conditions must contain at least one condition")

    rights = record.get("rights")
    if isinstance(rights, dict) and rights.get("status") not in ALLOWED_RIGHTS:
        errors.append(f"rights.status must be one of: {', '.join(sorted(ALLOWED_RIGHTS))}")

    if record.get("public_export_eligible") is True and (
        not isinstance(rights, dict) or rights.get("status") != "cleared"
    ):
        errors.append("public_export_eligible=true requires rights.status=cleared")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path, nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        record_path = Path(__file__).resolve().parents[1] / "assets" / "templates" / "asset-record.template.json"
    else:
        if args.record is None:
            parser.error("record is required unless --self-test is used")
        record_path = args.record

    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read {record_path}: {exc}")
        return 1

    errors = validate(record)
    if errors:
        print(f"FAIL: {record_path}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {record_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
