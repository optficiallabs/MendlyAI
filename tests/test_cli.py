import json
import tempfile
import unittest
from pathlib import Path

from src.cli import main


class TestCli(unittest.TestCase):
    def test_validate_sample_passes_for_valid_synthetic_record(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.json"
            path.write_text(
                json.dumps({"record_id": "SYN-0001", "encounter": "outpatient"}),
                encoding="utf-8",
            )
            self.assertEqual(main(["validate-sample", str(path)]), 0)

    def test_validate_sample_fails_for_missing_field(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.json"
            path.write_text(json.dumps({"record_id": "SYN-0001"}), encoding="utf-8")
            self.assertEqual(main(["validate-sample", str(path)]), 1)


if __name__ == "__main__":
    unittest.main()
