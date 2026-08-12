# Security Policy

Security and privacy are core requirements of MendlyAI.

Because the project relates to healthcare software, security issues must be handled carefully and responsibly.

## Reporting a Security Vulnerability

Please do not report security vulnerabilities through public GitHub Issues.

If you believe you have found a vulnerability, please report it privately to:

**[security@optficial.ai](mailto:security@optficial.ai)**

If this address is not yet configured, please use:

**[contact@optficial.ai](mailto:contact@optficial.ai)**

Please include:

* a clear description of the issue;
* the affected component;
* steps to reproduce the issue;
* expected and observed behaviour;
* possible security impact;
* and any suggested mitigation, if known.

Do not include real patient information, production credentials, confidential customer data, or restricted third-party information in the report.

## Responsible Disclosure

We request that security researchers:

* allow reasonable time for investigation and remediation;
* avoid accessing or modifying real patient information;
* avoid service disruption;
* avoid privacy violations;
* avoid testing systems without authorisation;
* and avoid publicly disclosing unresolved vulnerabilities.

## Scope

Security reports may cover:

* authentication;
* authorisation;
* access control;
* sensitive-data exposure;
* insecure logging;
* unsafe configuration;
* dependency vulnerabilities;
* API security;
* input validation;
* software supply-chain risks;
* secure storage;
* workflow security;
* and related issues.

## Out of Scope

The following are generally outside the intended security testing scope unless specifically authorised:

* denial-of-service testing;
* social engineering;
* physical security;
* attacks against third-party services;
* attacks against production healthcare environments;
* collection of real patient information;
* credential theft;
* and unauthorised penetration testing.

## Data Protection

The public repository must not contain:

* patient-identifiable information;
* confidential hospital information;
* medical records;
* private API keys;
* passwords;
* tokens;
* production database dumps;
* private certificates;
* or restricted proprietary material.

All public examples should use synthetic, de-identified, or properly licensed data.

## Supported Versions

During early development, security fixes will generally be applied to the current `main` branch and the latest stable release.

As the project matures, supported release versions will be listed here.

## Security Updates

Confirmed vulnerabilities may result in:

* patches;
* configuration changes;
* documentation updates;
* dependency upgrades;
* release notes;
* or security advisories.

Where appropriate, fixes will be validated before public disclosure.

## Healthcare Disclaimer

MendlyAI is a software project and should not be treated as a substitute for organisational security controls, clinical governance, professional medical judgement, regulatory compliance, or formal security assessment.

Production use should include appropriate security review, privacy review, testing, monitoring, access controls, and organisational approval.

Thank you for reporting security issues responsibly.
