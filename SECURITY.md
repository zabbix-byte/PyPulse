# Security Policy

## Supported Versions

The following table shows the versions currently being supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.4.0     | ✅ Yes             |

## Reporting a Vulnerability

If you discover a security vulnerability in PyPulse, please report it **privately** and **responsibly**. Do not open public issues regarding vulnerabilities.

To report a security issue, please email:

**📧 zabbix@ztrunk.space** (fictional email – replace with a real one if needed)

Please include:

- A detailed description of the issue.
- Steps to reproduce (if applicable).
- Any relevant logs, stack traces, or screenshots.
- Your contact information for follow-up.

We aim to respond to security issues within **72 hours**.

---

## Security Best Practices

If you are using PyPulse, consider the following to keep your environment secure:

- **Do not load untrusted web content** in embedded windows.
- Always **sanitize URLs and HTML content** passed into PyPulse.
- Run PyPulse applications with **least privilege** – avoid running as root.
- Keep your **Python environment and dependencies updated**.
- Ensure you are using **secure Chromium flags** (disable remote debugging, enable site isolation, etc.).

---

## Dependencies

We periodically audit our dependencies using [pip-audit](https://github.com/pypa/pip-audit) or similar tools. If you notice a vulnerable dependency that we missed, please report it.

---

## Responsible Disclosure

We support responsible disclosure and will credit reporters in our release notes unless anonymity is requested.

---

Thank you for helping make PyPulse more secure!

