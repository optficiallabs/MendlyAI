# Codex Workflow for MendlyAI

This folder documents how MendlyAI plans to use Codex CLI and OpenAI API credits to support open-source software maintenance, testing, review, and release preparation.

## Goals

The Codex workflow is intended to help maintainers reduce repetitive engineering work while keeping all important decisions under human review.

## Planned Uses

### Repository Analysis
- understand project structure and module relationships
- identify affected files when issues are reported
- review configuration, tests, and documentation together

### Pull Request Review
- summarise code changes
- identify possible defects, missing validation, regressions, and maintainability concerns
- highlight security- or privacy-sensitive changes for manual review

### Test Preparation
- suggest unit, integration, regression, boundary, invalid-input, and permission tests
- help identify untested code paths
- support reproducible test cases

### Issue Triage
- analyse bug reports
- identify likely affected components
- suggest reproduction steps
- help prepare focused fixes and validation tests

### Secure Code Review
- review sensitive-data handling
- identify hard-coded secrets, weak validation, unsafe logging, access-control mistakes, and risky configuration changes
- support dependency and software supply-chain review

### Documentation Maintenance
- compare code changes with documentation
- identify outdated API descriptions, setup instructions, and release notes

### Release Validation
- review tests, unresolved issues, security findings, dependency changes, documentation, and configuration before release

## Maintainer Control

Codex-assisted findings are advisory. Maintainers remain responsible for approving code changes, merging pull requests, handling security-sensitive decisions, and publishing releases.

## Data Handling

Public examples and tests must use synthetic, de-identified, properly licensed, or independently created data. Real patient information, credentials, production secrets, and confidential third-party material must not be submitted to public workflows.

## Evaluation

We plan to evaluate the workflow using measurable indicators such as valid defects identified, unnecessary findings, useful tests generated, regression detection, review time saved, maintainer acceptance, and cost per repository or pull request.
