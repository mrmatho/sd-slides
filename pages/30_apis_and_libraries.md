---
layout: top-title
color: purple-light
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---
::title::

# APIs and Libraries

::content::

A quick look at reusable code, API features, and security concerns.


## What are Code Libraries?

- Collections of prebuilt functions, classes, and helpers.
- Save time by reusing tested code.
- Examples: math utilities, UI components, data parsers.

## What are APIs?

- Interfaces that let software talk to other software.
- Define requests, responses, and supported operations.
- Can be local libraries or remote web services.

---
layout: top-title
color: purple-light
transition: fade
zoom: 1.1
---
::title::

## API Features

::content::

- Endpoints or function calls with clear contracts.
	- *Example: `GET /users/{id}` returns a user profile in a predictable JSON format.*
- Authentication, versioning, and rate limiting.
	- *Example: An API key is required, `/v2/` shows the version, and requests are limited to 100 per minute.*
- Documentation and error handling are essential.
	- *Example: The docs include sample requests, and a `404 Not Found` response explains a missing resource.*

---
layout: top-title
color: purple-light
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

## Security Issues

::content::

- Unprotected APIs can expose sensitive data.
	- *Example: An API that returns user records without requiring authentication lets anyone read private information.*
	- Example: An admin endpoint left open allows anyone to delete or modify data.
- Vulnerabilities: broken auth, injection, insecure transport.
	- Example: A missing or weak API key allows unauthorized access to restricted endpoints.
	- Example: Passing unsanitized input like `'; DROP TABLE users;--` to a query parameter causes SQL injection.
	- Example: Sending API requests over plain HTTP exposes credentials and data to interception.
- Libraries can introduce supply-chain risk and hidden bugs.
	- Example: A popular npm package is compromised by a malicious update that steals environment variables.
	- Example: An unmaintained library contains an unpatched vulnerability that attackers can exploit.

---
layout: top-title
color: purple-light
transition: fade
zoom: 1
---

::title::

## Best Practices

::content::

- Use trusted libraries and lock dependency versions.
- Validate inputs, use HTTPS, and secure credentials.
- Monitor API usage and review permissions regularly.
