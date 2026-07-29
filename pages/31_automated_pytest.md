---
layout: top-title
color: purple-light
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---
::title::

# Automated Testing with Pytest

::content::

- Pytest is a popular testing framework for Python that allows you to write simple and scalable test cases.
- To create a test you:
  - Write a function that starts with `test_`.
  - Use `assert` statements to check for expected outcomes.
  - Run the tests using the command `pytest` in the terminal.

---
layout: top-title
color: purple-light
transition: fade
---

::title::

# Pytest Examples

::content::

```python

def first_letter(my_string):
    return my_string[0]

def test_first_letter():
    assert first_letter("hello") == "h"
    assert first_letter("world") == "w"
    assert first_letter("Python") == "P"
```

---
layout: top-title-two-cols
color: purple-light
transition: fade
---
::title::

# More Advanced Pytest Features

::left::

**Fixtures**: Functions that run before each test to set up necessary conditions.

```python

import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

::right::

**Parametrization**: Run the same test with different inputs.

```python

import pytest

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
])

def test_increment(input, expected):
    assert input + 1 == expected
```

---
