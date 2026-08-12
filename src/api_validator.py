"""Simple reusable validation helpers for MendlyAI API payloads.

This module is intentionally lightweight and uses only standard Python.
Public examples should use synthetic, de-identified, properly licensed,
or otherwise suitable data.
"""

from typing import Any, Dict, Iterable, List


def validate_required_fields(payload: Dict[str, Any], required_fields: Iterable[str]) -> List[str]:
    """Return validation messages for required fields that are missing or empty."""
    errors: List[str] = []

    if not isinstance(payload, dict):
        return ["Payload must be a JSON object."]

    for field in required_fields:
        if field not in payload:
            errors.append(f"Missing required field: {field}")
            continue

        value = payload[field]
        if value is None or value == "":
            errors.append(f"Required field is empty: {field}")

    return errors


def validate_field_types(payload: Dict[str, Any], expected_types: Dict[str, type]) -> List[str]:
    """Return validation messages when present fields have unexpected Python types."""
    errors: List[str] = []

    if not isinstance(payload, dict):
        return ["Payload must be a JSON object."]

    for field, expected_type in expected_types.items():
        if field in payload and payload[field] is not None and not isinstance(payload[field], expected_type):
            errors.append(
                f"Invalid type for {field}: expected {expected_type.__name__}, "
                f"received {type(payload[field]).__name__}"
            )

    return errors


def validate_payload(
    payload: Dict[str, Any],
    required_fields: Iterable[str],
    expected_types: Dict[str, type] | None = None,
) -> Dict[str, Any]:
    """Validate a payload and return a simple structured result."""
    errors = validate_required_fields(payload, required_fields)

    if expected_types:
        errors.extend(validate_field_types(payload, expected_types))

    return {
        "valid": not errors,
        "errors": errors,
    }
