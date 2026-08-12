# Release Readiness Guide

This document defines the minimum checks recommended before a MendlyAI release is approved.

## 1. Functional Quality

- Automated tests pass on the target branch.
- New features include suitable tests.
- Known regressions are documented and resolved or explicitly accepted.
- Critical workflows have been checked with synthetic or otherwise suitable test data.

## 2. Security and Privacy

- No credentials, secrets, tokens, private keys, or production configuration are committed.
- Logging does not expose sensitive fields.
- Access-control changes have been reviewed.
- Dependency and software supply-chain findings have been reviewed.
- Security-sensitive changes receive additional maintainer review.

## 3. API and Data Compatibility

- Required fields and data types are validated.
- Breaking interface changes are clearly documented.
- Backward compatibility is checked where required.
- Example data remains synthetic, de-identified, properly licensed, or independently created.

## 4. Documentation

- README and module documentation reflect the current behaviour.
- Configuration changes are documented.
- New public interfaces include usage examples.
- Release notes summarise significant changes.

## 5. Maintainer Review

A release should be marked ready only after a maintainer confirms that functional, security, privacy, dependency, documentation, and compatibility checks have been reviewed.

Suggested final status values:

- READY
- READY WITH KNOWN LIMITATIONS
- REVIEW REQUIRED
- BLOCKED
