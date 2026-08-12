import unittest

from src.api_validator import validate_field_types, validate_payload, validate_required_fields


class TestApiValidator(unittest.TestCase):
    def test_required_fields_pass(self):
        payload = {"record_id": "SYN-0001", "encounter": "outpatient"}
        self.assertEqual(validate_required_fields(payload, ["record_id", "encounter"]), [])

    def test_missing_required_field(self):
        payload = {"record_id": "SYN-0001"}
        errors = validate_required_fields(payload, ["record_id", "encounter"])
        self.assertIn("Missing required field: encounter", errors)

    def test_field_type_validation(self):
        payload = {"age": "forty-two"}
        errors = validate_field_types(payload, {"age": int})
        self.assertEqual(len(errors), 1)
        self.assertIn("Invalid type for age", errors[0])

    def test_validate_payload_returns_structured_result(self):
        payload = {"record_id": "SYN-0001", "age": 42}
        result = validate_payload(
            payload,
            required_fields=["record_id", "age"],
            expected_types={"record_id": str, "age": int},
        )
        self.assertTrue(result["valid"])
        self.assertEqual(result["errors"], [])


if __name__ == "__main__":
    unittest.main()
