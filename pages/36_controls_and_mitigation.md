---
layout: top-title
color: blue-light
class: ns-c-tight
hideInToc: false
zoom: 1.5
---

::title::

# Controls and Mitigation

::content::

**Security controls** are the safeguards put in place to protect information systems and data from security threats. They can be **technical** or **non-technical** in nature.

**Mitigation** refers to any actions taken to reduce the impact or likelihood of a security threat or vulnerability.

---
layout: top-title-two-cols
color: blue-light
class: ns-c-tight
zoom: 1.1
---

::title::

# Security Controls

::left::

## From the Study Design

- version control and code repositories
- robust identity and access management
- encryption
- code review
- regular updates and patches to software
- separated development, testing and production environments

::right::

# Mitigation actions

- Within organisations:
  - Security policies
  - Training
  - Clear reporting procedures
  - Audit logs and monitoring

> Note: The Study Design does not explicitly mention mitigation actions - we have to infer them from the vulnerabilities and risks we have explored.

---
layout: top-title-two-cols
color: blue-light
class: ns-c-tight
---

::title::

# Security Controls

::left::

### Version control and code repositories

- Tracks any changes to code over time, allowing developers to revert to previous versions if necessary.
- **Protects security by:**
  - Allowing for easy identification of changes that may have introduced a vulnerabilities
  - Providing a history of code changes for auditing and accountability
  - Facilitating rollback of code to previous versions in case of problems

::right::

### Robust identity and access management

- Provides secure and controlled access to systems and data
- **Protects security by:**
  - Ensuring that only authorised users can access sensitive information and systems
  - Implementing strong authentication methods (e.g., MFA) to prevent unauthorised access

---
layout: top-title-two-cols
color: blue-light
class: ns-c-tight
---

::title::

# Security Controls

::left::

### Encryption

- Converts data (in transit or at rest) into a coded format that can only be accessed by authorised users with the correct decryption key.
- **Protects security by:**
  - Preventing unauthorised access to sensitive information
  - Ensuring data integrity and confidentiality
  - Protecting password and other sensitive information with one-way hashing algorithms

::right::

### Code review

- Involves the examination of code by other developers to identify and fix defects, vulnerabilities, and security issues.
- **Protects security by:**
  - Identifying and fixing vulnerabilities before they are deployed to production
  - Ensuring that code adheres to security best practices and standards
  - Providing an opportunity for knowledge sharing and learning among developers

---
layout: top-title-two-cols
color: blue-light
class: ns-c-tight
---

::title::

# Security Controls

::left::

### Regular updates and patches to software

- Involves applying updates and patches to software to fix known vulnerabilities and improve security.
- **Protects security by:**
  - Reducing the risk of exploitation of known vulnerabilities
  - Ensuring that software is up-to-date with the latest security features and improvements
  - Maintaining compatibility with other systems and software

::right::

### Separated development, testing and production environments

- Involves keeping distinct environments (server, database, and application) for development, testing, and production.
- **Protects security by:**
  - Reducing the risk of accidental or malicious changes affecting live systems
  - Allowing for thorough testing and validation of code before deployment to production
  - Ensuring that sensitive data is not exposed in development or testing environments

---
layout: top-title
color: blue-light
class: ns-c-tight
---
::title::

# Activity

::content::

For each of the security controls, describe a threat that it helps to mitigate, and why this control is effective in mitigating that threat.

**Security Controls:**

1. Version control and code repositories
2. Robust identity and access management
3. Encryption
4. Code review
5. Regular updates and patches to software
6. Separated development, testing and production environments

>Note: It is fine for the threats to be repeated, as long as you describe **how** each control mitigates the threat.
