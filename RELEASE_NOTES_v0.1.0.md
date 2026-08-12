# MendlyAI v0.1.0 — Initial Open-Source Release

## Overview

MendlyAI v0.1.0 is the first public open-source development release of the MendlyAI healthcare software toolkit by Optficial Labs.

This release establishes the project foundation for clinical data validation, API validation, secure logging, developer workflows, testing, benchmarks, documentation, and Codex-assisted maintainer workflows.

## Included in v0.1.0

- Clinical data validation utilities
- Clinical API validation module
- Secure logging with sensitive-field redaction
- Synthetic healthcare example data
- Initial benchmark cases
- Command-line interface
- Python packaging metadata
- Automated unit tests with GitHub Actions
- Dependency review workflow
- Pull request template
- Bug report and feature request templates
- Security policy
- Contribution guidelines
- Code of Conduct
- Development roadmap
- Release-readiness guidance
- Codex CLI workflow documentation

## Installation

Clone the repository:

```bash
git clone https://github.com/optficiallabs/MendlyAI.git
cd MendlyAI
```

Install in editable mode:

```bash
python -m pip install -e .
```

Run the CLI against the synthetic sample record:

```bash
mendlyai validate-sample examples/sample_patient_record.json
```

Run the test suite:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Security and Privacy

This release uses only synthetic or public-safe example material. It does not contain patient-identifiable information, confidential hospital data, credentials, production secrets, or restricted proprietary material.

MendlyAI is intended to support healthcare software development and workflow tooling. It is not a substitute for clinical judgement, regulatory review, organisational security controls, or production security assessment.

## Open-Source Licence

MendlyAI is released under the Apache License 2.0.

## Current Status

v0.1.0 is an early development release intended for evaluation, contribution, testing, and continued open-source development.

## Next Priorities

- expand clinical API validation
- strengthen secure logging and privacy checks
- add more benchmark scenarios
- improve dependency and release checks
- extend Codex CLI maintainer workflows
- add additional tests and documentation
- collect community feedback and contributions

## Maintained By

Optficial Labs Pvt Ltd., Hyderabad, India

Website: https://optficial.ai/
