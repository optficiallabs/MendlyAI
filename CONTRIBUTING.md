# Contributing to MendlyAI

Thank you for your interest in contributing to MendlyAI.

MendlyAI is an open healthcare technology project maintained by Optficial Labs. We welcome contributions from developers, researchers, healthcare technology professionals, students, security specialists, documentation contributors, and open-source maintainers.

Our aim is to keep the project practical, secure, transparent, and useful for real healthcare software development.

## How You Can Contribute

You can contribute in several ways:

* report bugs;
* suggest improvements;
* improve documentation;
* add tests;
* improve clinical data validators;
* contribute API integration utilities;
* improve security checks;
* add workflow examples;
* improve developer tools;
* help with accessibility;
* improve performance;
* review pull requests;
* or propose new modules.

## Before You Start

Before making a contribution:

1. Read the README.
2. Check existing Issues and Pull Requests.
3. Avoid duplicating work already in progress.
4. Open an Issue for major changes before starting development.
5. Do not include confidential healthcare information, patient data, credentials, private keys, or restricted third-party material.

## Development Workflow

A typical contribution process is:

1. Fork the repository.
2. Create a new branch from `main`.
3. Make your changes.
4. Add or update tests.
5. Update documentation where required.
6. Run the available checks locally.
7. Commit your changes with a clear message.
8. Push your branch.
9. Open a Pull Request.

Example branch names:

```text
feature/clinical-validator
fix/api-validation
docs/security-guidelines
test/workflow-cases
```

## Pull Request Guidelines

Each Pull Request should clearly explain:

* what was changed;
* why the change is required;
* how it was tested;
* whether it affects security or privacy;
* whether it changes an API or workflow;
* and whether documentation was updated.

Please keep Pull Requests focused. Large unrelated changes should be separated into different Pull Requests.

## Coding Quality

Contributions should aim for:

* clear and readable code;
* meaningful function and variable names;
* appropriate comments where necessary;
* minimal duplication;
* suitable error handling;
* input validation;
* clear test coverage;
* and maintainable design.

## Testing

New features and bug fixes should include suitable tests wherever practical.

Tests may include:

* unit tests;
* integration tests;
* regression tests;
* API tests;
* invalid-input tests;
* security tests;
* permission tests;
* and workflow tests.

## Security and Privacy

Healthcare software requires careful handling of sensitive information.

Do not commit:

* patient-identifiable information;
* medical records;
* real hospital data;
* passwords;
* API keys;
* private keys;
* access tokens;
* production logs containing sensitive information;
* or restricted proprietary data.

Use synthetic, de-identified, properly licensed, or independently created test data.

If you discover a security vulnerability, do not post it as a public Issue. Follow the process described in `SECURITY.md`.

## Documentation

Please update relevant documentation whenever your change affects:

* installation;
* configuration;
* APIs;
* behaviour;
* workflows;
* security assumptions;
* or release procedures.

## Commit Messages

Use short and meaningful commit messages.

Examples:

```text
Add clinical data validator
Fix API response validation
Improve security documentation
Add workflow regression tests
```

## Code Review

All contributions may be reviewed for:

* correctness;
* maintainability;
* security;
* privacy;
* test coverage;
* documentation;
* and compatibility with the project direction.

Maintainers may request changes before accepting a Pull Request.

## Contributor Conduct

All contributors must follow the project `CODE_OF_CONDUCT.md`.

## Questions

For general contribution questions, please open a GitHub Discussion or Issue where appropriate.

For security matters, follow `SECURITY.md`.

Thank you for helping improve MendlyAI.
