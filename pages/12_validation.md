---
layout: cover
color: blue-light
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Validation

---
src: ./u3o1_tracking.md
hide: false
---

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# What is Validation?

::content::

Validation is the process of checking that **input data** is sensible, complete, and in the correct format before the program uses it.

It helps prevent errors and keeps data reliable.

Examples include checking:

- a number is within an allowed range
- a required field is not blank
- text matches an expected format (for example, an email)

---
layout: top-title
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Validation in Applied Computing Study Design

::content::

Validation is a broad topic and it is possible to include validation rules that fall outside the following categories. But for the purposes of Software Development, the Study Design lists:

- Existence checks
- Type checks
- Range checks

---
layout: top-title-two-cols
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Existence Checks

::left::

## Description

An existence check ensures that a value exists. This is usually either:

1. Making sure a value has been entered for a required field (for example, a name or email address)
2. Checking that a value exists in a list of valid options (for example, a country name or product code) 
  - ***NOTE** This is less common and some teachers argue about whether or not this is actually an existence check*

::right::

## Example Code

In Python, we can check for existence using:

```python

# Check if a value is not empty
if len(name) > 0:
    print("Name is valid")
else:
    print("Name is required")

# Check if a value has been set
if age is not None:
    print("Age is valid")
else:
    print("Age is required")

# Check if a value exists in a list of valid options
valid_countries = ["Australia", "USA", "UK"]
if country in valid_countries:
    print("Country is valid")
else:
    print("Invalid country")
```

---
layout: top-title-two-cols
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Range Checks

::left::

## Description

A range check ensures that a value falls within a specified (reasonable) range. This is commonly used for numerical values, such as ages, prices, or quantities.

::right::

## Example Code

In Python, we can check for ranges using:

```python

# Check if a value is within a range
if 0 <= age <= 120:
    print("Age is valid")
else:
    print("Invalid age")
```

---