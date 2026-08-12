# MendlyAI

**MendlyAI is an open healthcare technology project from Optficial Labs focused on clinical documentation, triage support, structured medical information, shift handovers, secure connected-care workflows, and reusable developer utilities.**

The project is designed around one practical principle: healthcare software should make clinical work clearer and safer while keeping qualified professionals in control of important decisions.

## What the project currently includes

MendlyAI is in early open-source development and already includes:

- clinical data validation utilities;
- API payload validation;
- privacy-aware secure logging;
- synthetic healthcare examples;
- unit tests and automated GitHub Actions;
- dependency review for pull requests;
- benchmark examples;
- release-readiness guidance;
- contributor and security policies;
- Codex CLI maintainer workflow documentation;
- and an installable Python command-line entry point.

## Why this project matters

Healthcare applications commonly interact with electronic records, laboratory systems, pharmacy services, clinical documentation platforms, databases, APIs, cloud services, and other connected software. These systems need clear validation, secure data handling, reliable tests, controlled releases, and transparent maintenance practices.

MendlyAI provides small, reusable components that healthcare software teams can adopt independently rather than requiring a complete platform replacement.

## Installation

MendlyAI currently requires Python 3.10 or later.

Clone the repository:

```bash
git clone https://github.com/optficiallabs/MendlyAI.git
cd MendlyAI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```bash
pip install -e .
```

## Command-line usage

After installation, the `mendlyai` command becomes available.

Validate the included synthetic example:

```bash
mendlyai validate-sample examples/sample_patient_record.json
```

You can also run the module directly:

```bash
python -m src.cli validate-sample examples/sample_patient_record.json
```

The command returns a structured validation result showing whether the sample meets the current validation rules and, when relevant, which fields require attention.

## Running the tests

Run all unit tests locally with:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

The same test suite runs automatically through GitHub Actions for pushes and pull requests targeting `main`.

## Current developer modules

| Module | Purpose |
|---|---|
| `src/clinical_validator.py` | Basic checks for structured clinical records |
| `src/api_validator.py` | Required-field and type validation for API payloads |
| `src/secure_logging.py` | Redacts configured sensitive fields before logging |
| `src/cli.py` | Command-line interface for developer workflows |
| `benchmarks/` | Initial reproducible software-quality benchmark examples |
| `codex/` | Maintainer workflow documentation for Codex CLI |

## Security and privacy

The public repository must not contain identifiable patient information, confidential hospital records, credentials, authentication tokens, private keys, production secrets, or restricted proprietary data.

Public tests and examples should use only synthetic, de-identified, properly licensed, or independently created information.

Security vulnerabilities should not be posted as ordinary public issues. Please follow the private reporting process in `SECURITY.md`.

## Human oversight

MendlyAI is intended to support healthcare software development and workflow tooling. It is not a replacement for doctors, nurses, pharmacists, clinical specialists, security teams, regulatory review, or organisational governance.

Any production use involving healthcare information should include appropriate professional review, access controls, privacy safeguards, testing, monitoring, legal and regulatory review, and organisational approval.

## Codex and maintainer workflows

The repository includes a dedicated `codex/README.md` describing how maintainers can use Codex CLI for tasks such as:

- repository understanding;
- pull-request review;
- issue triage;
- test preparation;
- secure-code review;
- documentation maintenance;
- and release validation.

Important code and release decisions remain with human maintainers.

## Repository structure

```text
MendlyAI/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── ROADMAP.md
├── pyproject.toml
├── requirements.txt
├── src/
├── tests/
├── examples/
├── benchmarks/
├── docs/
├── codex/
└── .github/
```

## Contributing

Contributions are welcome from developers, healthcare researchers, security professionals, students, clinicians, and open-source maintainers.

Before contributing, please read:

- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `ROADMAP.md`

A pull request should explain what changed, why the change is needed, how it was tested, whether security or privacy is affected, and whether documentation was updated.

## Project status

**Current stage: v0.1.0 release-candidate preparation.**

The immediate priorities are to stabilise the initial validators and security utilities, improve benchmark coverage, exercise the pull-request workflow, strengthen documentation, and prepare the first public development release.

## Organisation

**Optficial Labs Pvt Ltd.** develops focused technology products for education, healthcare, and agriculture.

- Education: Dhimant
- Healthcare: Mendly
- Agriculture: BhoomiAI

Website: https://optficial.ai/

Contact: contact@optficial.ai

## Project team

- **Dr. Asadi Srinivasulu — Chief Advisor:** research direction, technical guidance, evaluation, and project oversight.
- **Dr. Tarkeswar Barua — R&D Head:** research planning, technical validation, development supervision, and testing.
- **Dr. Pradeep G — Project Coordinator:** implementation planning, repository management, testing, documentation, and reporting.
- **Goddindla Nagarjuna — Intern:** software development, integration, and testing support.
- **Harini Priyanshu Adike — Intern:** testing, documentation, data preparation, and validation.
- **Paila Sharmila — Intern:** healthcare workflow testing, documentation, and research support.
- **Mullaa Sufiyan Khan — Intern:** development support, testing, integration, and reproducibility.

## Licence

MendlyAI is released under the **Apache License 2.0**. See `LICENSE` for the complete terms.

---

**MendlyAI — building clearer, safer, and more reliable healthcare software workflows through open development and practical engineering.**
