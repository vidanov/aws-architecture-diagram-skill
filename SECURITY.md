# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

This project is a skill file (markdown + reference data) with no runtime code, network access, or dependencies. The attack surface is minimal.

If you discover a security issue (for example, a reference file that could cause an agent to generate malicious output), please report it responsibly:

1. **Do not** open a public issue.
2. Email **vidanov@gmail.com** with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
3. You will receive acknowledgment within 72 hours.
4. A fix will be released as soon as possible, and you will be credited (unless you prefer otherwise).

## Scope

Security concerns relevant to this project:

- Prompt injection via reference files
- Stencil names that could trigger unintended behavior in draw.io
- Supply chain concerns with the `npx skills add` installation method

## Out of Scope

- Vulnerabilities in draw.io itself
- Vulnerabilities in AI agents consuming this skill
- Issues with the user's local environment
