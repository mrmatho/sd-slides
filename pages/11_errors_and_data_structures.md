---
layout: cover
color: orange-light
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Errors and Data Structures

---
src: ./u3o1_tracking.md
hide: false 
---

---
layout: top-title-two-cols
color: yellow
zoom: 1.1
class: ns-c-tight
---

::title::

# Today - Errors and Data Structures

::left::

# Errors

- Syntax Errors
- Runtime Errors
- Logic Errors

::right::

# Data Structures

|Study Design Term | Python Equivalent |
|------------------|-------------------|
| one-dimensional arrays | Lists |
| two-dimensional arrays | Lists of Lists |
| records (varying data types, field index) | Dictionaries |

---
layout: top-title
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Errors - Syntax Errors

::content::

A **syntax error** occurs when the code violates the rules of the programming language. These errors are detected by the interpreter or compiler ==before== the program is executed.

Syntax errors can include:

- Missing or mismatched parentheses, brackets, or braces
- Incorrect indentation
- Misspelled keywords or variable names

**How do you find syntax errors?**
- Your IDE should highlight any syntax errors
- When you try to run the code, the Python interpreter will give you an error message: including the **type** of error, the **line number** where the error occurred, and a **description** of the error.

---
layout: top-title
color: blue-light
zoom: 1.3
---
::title::

# Common Python Syntax Errors

::content::

- IndentationError: unexpected indent - check your spacing. Sometimes the line they tell you is before or after the actual error.
- SyntaxError: invalid syntax - check for missing parentheses, brackets, or braces, and ensure all keywords are spelled correctly.

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Errors - Logic Errors

::content::

Logic Errors occur when the code runs fine, but produces incorrect results. They are the only type of error that does not produce an error message, so they can be the hardest to find and fix.

**Logic errors can include:**

- Incorrect use of operators (e.g., using `+` instead of `*`)
- Incorrect variable names
- Incorrect conditions in control structures (e.g., using `>` instead of `<`)
- Incorrect algorithm implementation

**How do you find logic errors?**
- Testing thoroughly, including edge cases
- Using print statements or breakpoints (which we will cover in more detail later)
- Talking through your code- either on your own or with a peer or mentor (rubber duck debugging)

---
layout: top-title
color: blue-light
zoom: 0.9
class: ns-c-tight
---
::title::

# Errors - Runtime Errors

::content::

We are given specific runtime errors that we cover in the study design. They are:

- **Overflow**
  - Occurs when a calculation produces a result that is too large to be represented within the available memory or data type limits.
  - Python typically raises an `OverflowError` when this happens.
- **Index out of range**
  - Occurs when you try to access an index that is outside the bounds of a list or array.
  - Python raises an `IndexError` when this happens.
- **Type mismatch**
  - Occurs when you try to perform an operation on incompatible data types (e.g., adding a string and an integer).
  - Python raises a `TypeError` when this happens.
- **Divide by zero**
  - (Unsurprisingly) occurs when you try to divide a number by zero.
  - Python raises a `ZeroDivisionError` when this happens.

---
layout: top-title
color: green-light
zoom: 1.1
class: ns-c-tight
---

::title::

# Pick the Error

::content::

For each of the following error descriptions, identify the type of error (syntax, logic, or runtime) and the specific error type if applicable.

1. You try to run your code and get an error message that says "SyntaxError: unexpected indent". 
2. Your code tries to multiply two strings.
3. You try to access the 10th element of a list that only has 5 elements.
4. Your program is running large calculations in a loop and it runs for a while, then crashes.
5. You write a function to calculate the area of a rectangle, but you accidentally use the formula for the perimeter.

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Data Structures

::content::

A data structure is a way of organising and storing data in a computer so that it can be accessed and modified efficiently.

The study design specifies three data structures that you need to be familiar with:
- One-dimensional arrays (Python Lists)
- Two-dimensional arrays (Lists of Lists)
- Records (Dictionaries)

We need to understand how to create, access, and modify these data structures, as well as their advantages and disadvantages.

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---
::title::

# Data Structures - One-Dimensional Arrays (Lists)

::content::

A one-dimensional array is a linear collection of elements. In Python, we use **lists** to represent one-dimensional arrays.

They are typically: 

- Ordered: the order of elements is maintained and is important
- Mutable: you can change the elements after the list has been created
- Able to contain duplicate values

Lists are created using square brackets `[]` and elements are separated by commas. For example:

```python
my_list = [1, 2, 3, 4, 5]
another_list = ["golf", "tennis", "soccer"]
```

<Admonition color="green-light" title="Differences between Lists and Arrays">

Technically - a python list has some differences to a one-dimensional array in other programming languages. Lists are permitted to have different data types - but Arrays should be only one data type. Arrays usually have a fixed size, whereas Python lists can grow and shrink.

</Admonition>

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Data Structures - Two-Dimensional Arrays (Lists of Lists)

::content::

A two-dimensional array is a collection of elements arranged in a grid or table format. In Python, we can represent two-dimensional arrays using **lists of lists**.

For example, a 3x3 matrix can be represented as:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
Which could also be written as:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
In this example, `matrix` is a list that contains three sublists, each representing a row of the matrix.

---
layout: top-title
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Data Structures - Records (Dictionaries)

::content::

A record is a collection of fields that can contain different data types. Unlike arrays, records are **not ordered** and are accessed using **field names** rather than indices. In Python, we use **dictionaries** to represent records. We could instead use Objects and Classes to represent records - we will cover that for SAC 3 & 4.

Dictionaries are created using curly braces `{}` and consist of key-value pairs. For example:

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

In pseudocode records are more commonly written as:

```
Person.Name = "Alice"
Person.Age = 30
Person.City = "New York"
```
---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---
::title::

# Using Dictionaries in Python

::content::

Dictionaries are accessed using their keys. For example, to access the name of the person in the previous example, we would use:

```python
print(person["name"])  # Output: Alice
```

You can also add new key-value pairs to a dictionary:

```python
person["email"] = "alice@example.com"
```

And you can modify existing values:

```python
person["age"] = 31
```

---
layout: top-title
color: blue-light
zoom: 1.2
---

::title::

# Do Yourself: Using Data Structures

::content::

1. Create a list of your favourite sports.
2. Create a list of lists to represent a game board for tic-tac-toe.
3. Create a dictionary to represent a City, with fields for name, population, and country.
4. Create a dictionary to represent a Student, with fields for name, age, and a list of their favourite subjects.

**Use the Student dictionary to print out a sentence about each of the subjects they like. For example, "Alice likes Math", "Alice likes Science", etc.**
---
