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
    - ***NOTE** Case 2 is less common and some teachers argue about whether or not this is actually an existence check*

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

# Type Checks

::left::

## Description

A type check ensures that a value is of the expected data type. This is important because different data types have different properties and operations.

For example, if a program expects a number but receives text, it may cause an error when it tries to perform calculations.

Type checks are especially important in languages that are not strongly typed (like Python) where variables can hold values of any type.

::right::

## Example Code

In Python, we can check for types using the `isinstance()` function:

```python
# Check if a value is an integer

if isinstance(age, int):
    print("Age is valid")
else:
    print("Age must be an integer")

# Check if a value is a string
if isinstance(name, str):
    print("Name is valid")
else:
    print("Name must be a string")

# Check if a value is number (either int or float)
if isinstance(price, (int, float)):
    print("Price is valid")
else:
    print("Price must be a number")
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

Range check can also be used for length of text inputs, and for dates (for example, a date of birth cannot be in the future).

::right::

## Example Code

In Python, we can check for ranges using:

```python

# Check if a value is within a range
if 0 <= age and age <= 120:
    print("Age is valid")
else:
    print("Invalid age")

# Check if the length of a text input is within a range
if 1 <= len(username) and len(username) <= 20:
    print("Username is valid")
else:
    print("Username must be between 1 and 20 characters")

# Check if a date is in the past
from datetime import datetime
if date_of_birth < datetime.now():
    print("Date of birth is valid")
else:
    print("Date of birth cannot be in the future")
```

---
layout: top-title
color: blue-light
zoom: 1.4
class: ns-c-tight
---
::title::

# Using a function for validation

::content::

In the previous examples, we were printing error messages directly in the validation code. In a real program, we would usually want to handle validation errors more gracefully.

A good approach is to create a function that performs the validation and returns a boolean value indicating whether the input is valid or not. This allows us to separate the validation logic from the rest of the program and makes it easier to reuse the validation code. The function might also return an error message that can be displayed to the user.

---
layout: top-title
color: blue-light
zoom: 1.1
class: ns-c-tight
---
::title::

# Example: Validation Function

::content::

Here is an example of a validation function in Python that checks if an age input is valid:

```python

def validate_name(name):
  '''
  Validates that the name is a string between 2 and 25 characters long.
  @param name: The name to validate'''
    if not isinstance(name, str):
        return False, "Name must be a string"
    if len(name) < 2 or len(name) > 25:
        return False, "Name must be between 2 and 25 characters"
    return True, ""

# Example usage
name = None
while name is None:
    name_input = input("Enter your name: ")
    is_valid, error_message = validate_name(name_input)
    if is_valid:
        name = name_input  # Convert input to integer if valid
    else:
        print(f"Invalid name: {error_message}")
```

---
layout: top-title
color: green-light
zoom: 1.2
class: ns-c-tight
---

::title::
# Do Yourself: Validation Function

::content::

1. Create a validation function to check if a postcode is valid. A valid postcode should be:
    - A string
    - 4 characters long
    - Able to be converted into an integer

2. Create a list of valid and invalid postcodes. Write a loop to test your validation function with each postcode and print the results.

---

