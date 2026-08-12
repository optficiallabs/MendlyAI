"""Command-line interface for MendlyAI developer utilities."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from src.api_validator import validate_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mendlyai",
        description="Open-source healthcare software validation utilities from MendlyAI.",
    )
    subparsers = parser.add_subparsers(dest="command")

    validate = subparsers.add_parser(
        "validate-sample",
        help="Validate a synthetic JSON healthcare record.",
    )
    validate.add_argument("path", help="Path to a JSON file containing synthetic test data.")

    return parser


def validate_sample(path: str) -> int:
    record_path = Path(path)
    if not record_path.exists():
        print(f"File not found: {record_path}")
        return 2

    try:
        payload = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read valid JSON: {exc}")
        return 2

    result = validate_payload(
        payload,
        required_fields=["record_id", "encounter"],
        expected_types={"record_id": str, "encounter": str},
    )

    if result["valid"]:
        print("Validation passed.")
        return 0

    print("Validation failed:")
    for error in result["errors"]:
        print(f"- {error}")
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate-sample":
        return validate_sample(args.path)

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
