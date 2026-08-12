"""Basic clinical record validation utilities for MendlyAI.

This module is intentionally simple and uses no real patient data. It is meant as
an initial open-source example that can be extended with additional validation
rules over time.
"""

from typing import Any, Dict, List


REQUIRED_FIELDS = ("patient_id", "age", "symptoms")


def validate_clinical_record(record: Dict[str, Any]) -> List[str]:
    """Return a list of validation errors for a synthetic clinical record.

    An empty list means the record passed the current basic validation rules.
    """
    errors: List[str] = []

    if not isinstance(record, dict):
        return ["Record must be a dictionary."]

    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"Missing required field: {field}")

    patient_id = record.get("patient_id")
    if patient_id is not None and (not isinstance(patient_id, str) or not patient_id.strip()):
        errors.append("patient_id must be a non-empty string.")

    age = record.get("age")
    if age is not None and (not isinstance(age, int) or isinstance(age, bool) or not 0 <= age <= 120):
        errors.append("age must be an integer between 0 and 120.")

    symptoms = record.get("symptoms")
    if symptoms is not None:
        if not isinstance(symptoms, list) or not symptoms:
            errors.append("symptoms must be a non-empty list.")
        elif not all(isinstance(item, str) and item.strip() for item in symptoms):
            errors.append("each symptom must be a non-empty string.")

    return errors


def is_valid_clinical_record(record: Dict[str, Any]) -> bool:
    """Return True when the record passes the current validation rules."""
    return not validate_clinical_record(record)
