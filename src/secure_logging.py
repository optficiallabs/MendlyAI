"""Safe logging helpers for synthetic and non-sensitive MendlyAI workflows."""

from __future__ import annotations

from typing import Any, Mapping

SENSITIVE_KEYS = {
    "patient_id",
    "name",
    "full_name",
    "email",
    "phone",
    "address",
    "date_of_birth",
    "dob",
    "password",
    "token",
    "api_key",
    "secret",
}

MASK = "***REDACTED***"


def redact_value(key: str, value: Any) -> Any:
    """Redact values for keys that may contain sensitive information."""
    if key.lower() in SENSITIVE_KEYS:
        return MASK
    return value


def sanitize_mapping(data: Mapping[str, Any]) -> dict[str, Any]:
    """Return a logging-safe copy of a mapping with sensitive fields redacted."""
    sanitized: dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, Mapping):
            sanitized[key] = sanitize_mapping(value)
        elif isinstance(value, list):
            sanitized[key] = [
                sanitize_mapping(item) if isinstance(item, Mapping) else item
                for item in value
            ]
        else:
            sanitized[key] = redact_value(key, value)
    return sanitized
