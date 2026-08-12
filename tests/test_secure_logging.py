from src.secure_logging import MASK, sanitize_mapping


def test_redacts_sensitive_fields():
    record = {
        "patient_id": "SYN-1001",
        "name": "Synthetic Patient",
        "age": 45,
        "department": "General Medicine",
    }

    safe = sanitize_mapping(record)

    assert safe["patient_id"] == MASK
    assert safe["name"] == MASK
    assert safe["age"] == 45
    assert safe["department"] == "General Medicine"


def test_redacts_nested_sensitive_fields():
    record = {
        "visit": {
            "email": "example@example.org",
            "status": "scheduled",
        }
    }

    safe = sanitize_mapping(record)

    assert safe["visit"]["email"] == MASK
    assert safe["visit"]["status"] == "scheduled"
