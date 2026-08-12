import unittest

from src.clinical_validator import is_valid_clinical_record, validate_clinical_record


class ClinicalValidatorTests(unittest.TestCase):
    def test_valid_record(self):
        record = {
            "patient_id": "SYN-001",
            "age": 42,
            "symptoms": ["fever", "cough"],
        }
        self.assertTrue(is_valid_clinical_record(record))
        self.assertEqual(validate_clinical_record(record), [])

    def test_missing_required_field(self):
        record = {"patient_id": "SYN-002", "age": 30}
        errors = validate_clinical_record(record)
        self.assertIn("Missing required field: symptoms", errors)

    def test_invalid_age(self):
        record = {
            "patient_id": "SYN-003",
            "age": 150,
            "symptoms": ["headache"],
        }
        errors = validate_clinical_record(record)
        self.assertIn("age must be an integer between 0 and 120.", errors)

    def test_empty_symptoms(self):
        record = {
            "patient_id": "SYN-004",
            "age": 25,
            "symptoms": [],
        }
        errors = validate_clinical_record(record)
        self.assertIn("symptoms must be a non-empty list.", errors)


if __name__ == "__main__":
    unittest.main()
