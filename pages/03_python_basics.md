---
layout: top-title
color: blue
transition: fade
zoom: 1
hideInToc: false
---

::title::

# Python Basics

::content::

**Welcome to Python programming!**

This section covers the fundamental building blocks of Python programming:

<div class="grid grid-cols-2 gap-4">

<div>

<SpeechBubble color="purple-light" shape="round" position="l" class="ns-c-tight">

## Variables
- Store data in named containers

</SpeechBubble>

<br>

<SpeechBubble color="orange-light" shape="round" position="l" class="ns-c-tight">

## Conditions
- Make *decisions* with `if/elif/else`

</SpeechBubble>

</div>

<div>

<SpeechBubble color="sky-light" shape="round" position="r" class="ns-c-tight">

## Loops
- **`for` loops**: Iterate over *sequences*
- **`while` loops**: Repeat as long as condition is `True`


</SpeechBubble>

<br>

<SpeechBubble color="green-light" shape="round" position="r" class="ns-c-tight">

## Functions
- Reusable blocks of code


</SpeechBubble>

</div>

</div>

<style>
  .grid {
    margin-top: 2rem;
  }
</style>

---
layout: top-title-two-cols
color: purple
zoom: 0.87
---

::title::

# Variables and Data Types

::left::

## What are Variables?

Variables are **containers** that store data values. Think of them as labeled boxes where you can put information.

```python
# Assigning values to variables
name = "Alice" # String
age = 16 # Integer
height = 1.65 # Float
is_student = True # Boolean
```
<br> 

<Admonition title="Variable Names" color="purple-light">

Variable names should be:
- Descriptive and meaningful
- Use lowercase with underscores (snake_case)
- Start with a letter or underscore
- Cannot be Python keywords

</Admonition>

::right::

## Common Data Types

<v-clicks>

<SpeechBubble color="sky-light" position="l" shape="round">

**String (str)** - Text data

```python
greeting = "Hello, World!"
subject = 'Software Development' # Double or single quotes are fine
```

</SpeechBubble>

<SpeechBubble color="green-light" position="l" shape="round">

**Integer (int)** - Whole numbers

```python
student_count = 25
year_level = 11
temperature = -5 # Negative numbers still integers
```

</SpeechBubble>

<SpeechBubble color="orange-light" position="l" shape="round">

**Float** - Decimal numbers

```python
temperature = 23.5 # The decimal point makes it a float
price = 19.99
```

</SpeechBubble>

<SpeechBubble color="purple-light" position="l" shape="round">

**Boolean (bool)** - True or False

```python
is_raining = False # Must be capitalized
has_passed = True
```

</SpeechBubble>

</v-clicks>

---
layout: top-title-two-cols
color: sky
zoom: 0.85
---

::title::

# Working with Variables

::left::

## Type Conversion

You can convert between data types:

```python
# String to integer
age_str = "16"
age_int = int(age_str)  # 16

# Integer to string
score = 95
score_str = str(score)  # "95"

# String to float
price_str = "19.99"
price = float(price_str)  # 19.99
```

## Type Checking

You can use `type()` to check the data type:

```python
name = "Alice"
print(type(name))  # <class 'str'>

age = 16
print(type(age))   # <class 'int'>
```

::right::

## Basic Operations

<SpeechBubble color="blue-light" position="l" shape="round">

**Arithmetic Operations**

```python
# Numbers
x = 10
y = 3

sum = x + y        # 13
difference = x - y  # 7
product = x * y     # 30
quotient = x / y    # 3.333...
integer_div = x // y # 3
remainder = x % y   # 1
power = x ** y      # 1000
```

</SpeechBubble>

<br>

<SpeechBubble color="green-light" position="l" shape="round">

**String Operations**

```python
# Concatenation
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name

# Repetition
laugh = "ha" * 3  # "hahaha"
```

</SpeechBubble>

---
layout: top-title
color: yellow
zoom: 1
---

::title::

# Conditions: Making Decisions

::content::

## If Statements

Conditions allow your program to make decisions and execute different code based on whether something is true or false.

```python
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside!")
elif temperature > 10:
    print("It's cool outside!")
else:
    print("It's cold outside!")
```
<br>

<Admonition title="Indentation Matters!" color="yellow">

Python uses **indentation** (4 spaces) to define code blocks. All code that belongs to an if statement must be indented.

</Admonition>

---
layout: top-title-two-cols
color: orange
zoom: 1.1
---

::title::

# Comparison Operators

::left::

## Comparing Values

Comparison operators compare values and return `True` or `False`:

```python
x = 10
y = 5

x == y   # Equal to: False
x != y   # Not equal to: True
x > y    # Greater than: True
x < y    # Less than: False
x >= y   # Greater than or equal to: True
x <= y   # Less than or equal to: False
```

::right::

## Using Comparisons in Conditions

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or lower")
```
<br>

<Admonition title="Watch Out!" color="red-light">

`=` is for **assignment** (giving a value to a variable)

`==` is for **comparison** (checking if two values are equal)

</Admonition>

---
layout: top-title-two-cols
color: purple
zoom: 0.9
---

::title::

# Logical Operators

::left::

## Combining Conditions

Logical operators combine multiple conditions:

<SpeechBubble color="purple-light" position="l" shape="round">

**and** - Both conditions must be True

```python
age = 16
has_license = True

if age >= 16 and has_license:
    print("Can drive!")
```

</SpeechBubble>

<br>

<SpeechBubble color="green-light" position="l" shape="round">

**or** - At least one condition must be True

```python
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No school today!")
```

</SpeechBubble>

::right::

<SpeechBubble color="orange-light" position="l" shape="round">

**not** - Reverses the condition

```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

</SpeechBubble>

<br>

## Combining Multiple Conditions

```python
grade = 85
attendance = 95

if grade >= 80 and attendance >= 90:
    print("Excellent performance!")
elif grade >= 70 or attendance >= 90:
    print("Good job!")
else:
    print("Keep working hard!")
```

<Admonition title="Tip" color="yellow-light">

Use parentheses (brackets) for complex conditions to make them clearer:

`if (age >= 16 and has_license) or has_permit:`

</Admonition>

---
layout: top-title-two-cols
color: green
zoom: 1
---

::title::

# Loops: For Loops

::left::

## Repeating Actions with For Loops

For loops are used to iterate over a sequence (like a list, range, or string).

```python
# Loop through a range of numbers
for i in range(5):
    print(f"Count: {i}")
# Output: Count: 0, Count: 1, Count: 2, Count: 3, Count: 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a string
for letter in "Python":
    print(letter)
```
::right::

<Admonition title="The range() Function" color="green-light">

`range(5)` generates numbers from 0 to 4 (5 numbers total)

`range(1, 6)` generates numbers from 1 to 5

`range(0, 10, 2)` generates even numbers from 0 to 8 (step by 2)

</Admonition>


---
layout: top-title-two-cols
color: teal
zoom: 0.87
---

::title::

# Loops: While Loops

::left::

## Repeating While a Condition is True

While loops continue executing as long as a condition remains true.

```python
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count
# Output: Count is: 0, 1, 2, 3, 4

# User input example
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted!")
```

<Admonition title="Warning!" color="red">

Make sure your while loop will eventually become False, or it will run forever (infinite loop)!

Always include a way to exit the loop.

</Admonition>

::right::

## Loop Control Statements

<v-clicks>

<SpeechBubble color="sky-light" position="l" shape="round">

**break** - Exit the loop immediately

```python
i = 0
while i < 10:
    if i == 5:
        break  # Stop when i is 5
    print(i)
    i += 1
# Output: 0, 1, 2, 3, 4
```

</SpeechBubble>

<SpeechBubble color="purple-light" position="l" shape="round">

**continue** - Skip to the next iteration

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip when i is 3
    print(i)
# Output: 1, 2, 4, 5
```

</SpeechBubble>

<Admonition title="Tip" color="yellow-light">

`break` and `continue` work in any loops (ie. both`for` and `while`). 

</Admonition>

</v-clicks>

---
layout: top-title-two-cols
color: indigo
zoom: 1
---

::title::

# Functions: Organizing Your Code

::left::

## What are Functions?

Functions are **reusable blocks of code** that perform a specific task. They help you:
- Avoid repeating code
- Make your code more organized and readable
- Break complex problems into smaller pieces

```python 
# Defining a function
def greet():
    print("Hello, Software Development student!")

# Calling the function
greet()  # Output: Hello, Software Development student!
```
::right::

<Admonition title="Function Anatomy" color="indigo">

- **def** - Keyword to define a function
- **greet** - Function name (use descriptive names)
- **()** - Parentheses for parameters (can be empty)
- **:** - Colon to start the function body
- **Indented code** - The function's code block
- **Calling a function** - When you want to use the function. Write the function name followed by parentheses: `greet()`

</Admonition>

---
layout: top-title-two-cols
color: purple
zoom: 0.9
---

::title::

# Functions with Parameters

::left::

## Passing Information to Functions

Parameters allow you to pass data into functions:

```python
# Function with one parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!
greet_person("Bob")    # Hello, Bob!

# Function with multiple parameters
def calculate_area(width, height):
    area = width * height
    print(f"Area: {area}")

calculate_area(5, 10)  # Area: 50
```

<Admonition title="Parameters vs Arguments" color="purple-light">

**Parameters** are variables in the function definition

**Arguments** are the actual values you pass when calling the function

</Admonition>

::right::

## Default Parameters

You can give parameters default values:

```python
def greet_with_title(name, title="Student"):
    print(f"Hello, {title} {name}!")

greet_with_title("Alice")
# Output: Hello, Student Alice!

greet_with_title("Bob", "Mr.")
# Output: Hello, Mr. Bob!
```

## Multiple Arguments

```python
def introduce(name, age, subject):
    message = f"{name} is {age} years old"
    message += f" and studies {subject}"
    print(message)

introduce("Alice", 16, "Software Dev")
# Alice is 16 years old and studies Software Dev
```

---
layout: top-title
color: red
zoom: 0.87
---

::title::

# Functions with Return Values

::content::

## Returning Values from Functions

Functions can return values using the `return` keyword:

```python
# Function that returns a value
def add_numbers(a, b):
    result = a + b
    return result

# Use the returned value
sum = add_numbers(5, 3)
print(sum)  # Output: 8

# Or use it directly
print(add_numbers(10, 20))  # Output: 30
```
<br>

<Admonition title="Return vs Print" color="red-light">

**print()** displays output to the screen

**return** sends a value back to where the function was called, so you can use it in your code.

We are using functions to `return` values in our coding exercises. This makes the automated testing simpler, as well as teaching you good programming practices.

</Admonition>

---
layout: top-title-two-cols
color: red
zoom: 1
---
::title::

## More Return Examples

::left::

<v-clicks>

<SpeechBubble color="sky-light" position="l" shape="round">

**Calculate and return**

```python
def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

result = calculate_average(80, 90, 85)
print(f"Average: {result}")
```

</SpeechBubble>
<br>

<SpeechBubble color="green-light" position="l" shape="round">

**Return boolean values**

```python
def is_passing_grade(score):
    return score >= 50

if is_passing_grade(75):
    print("Passed!")
else:
    print("Failed")
```

</SpeechBubble>

</v-clicks>

::right::

<v-clicks>

<SpeechBubble color="orange-light" position="l" shape="round">

**Return strings**

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

grade = get_grade(85)
print(f"Your grade: {grade}")
```

</SpeechBubble>

</v-clicks>

---
layout: top-title-two-cols
color: green-light
zoom: 0.92
---

::title::

# Putting It All Together

::left::

### Functions

```python
def categorize(minutes):
    """Label a task by its expected duration"""
    if minutes < 25:
        return "short"
    elif minutes <= 50:
        return "medium"
    else:
        return "long"

def summarize_plan(tasks):
    """Print each task with a label and return totals"""
    total = 0
    long_tasks = 0
    # Using enumerate to give each task a number
    for i, (name, mins) in enumerate(tasks, start=1): 
        label = categorize(mins)
        print(f"{i}. {name:12} {mins:>3} min - {label}")
        total += mins
        if mins > 50:
            long_tasks += 1

    average = total / len(tasks)
    return total, average, long_tasks

```
::right::

### Main Program 

```python
# Main program
# Plan of study tasks, each with a name and duration in minutes
plan = [
    ("Math revision", 30),
    ("English essay", 60),
    ("Software exercises", 20),
    ("Break", 10),
]

# summarize_plan returns 3 values, so we unpack them here
total, avg, longs = summarize_plan(plan)
# \n prints a new line character. This makes the output cleaner.
# f-string formats the output 
# putting the variables in the string and rounding avg to 1 dp
print(f"\nTotal: {total} min, Avg: {avg:.1f} min, Long tasks: {longs}")
```

<br>

<Admonition title="Example Program" color="purple-light">

This program stores a study plan as a list of tasks with durations, categorizes each task based on its length, and summarizes the total and average study time.

</Admonition>

---
layout: top-title
color: green
zoom: 0.9
---

::title::

# Python Basics Summary

::content::

<div class="grid grid-cols-2 gap-4">

<div>

<SpeechBubble color="purple-light" shape="round" position="l" class="ns-c-tight">

## Variables
- Store data in named containers
- Common types: `str`, `int`, `float`, `bool`
- Use descriptive names in snake_case

</SpeechBubble>

<br>

<SpeechBubble color="orange-light" shape="round" position="l" class="ns-c-tight">

## Conditions
- Make decisions with `if/elif/else`
- Use comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Combine conditions with `and`, `or`, `not`

</SpeechBubble>

</div>

<div>

<SpeechBubble color="sky-light" shape="round" position="r" class="ns-c-tight">

## Loops
- **`for` loops**: Iterate over *sequences*
- **`while` loops**: Repeat as long as condition is `True`
- Control with `break` and `continue`

</SpeechBubble>

<br>

<SpeechBubble color="green-light" shape="round" position="r" class="ns-c-tight">

## Functions
- Reusable blocks of code
- Start with `def` keyword
- Accept parameters for input
- `return` values for output
- Make code organized and readable

</SpeechBubble>

</div>

</div>

<style>
  .grid {
    margin-top: 2rem;
  }
</style>
