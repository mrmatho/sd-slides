---
layout: cover
color: blue
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Classes and Objects

---
layout: top-title-two-cols
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Object-Oriented Programming (OOP)

::left::

Object-Oriented Programming (OOP) is a programming approach that uses "objects" to design applications and computer programs. It is based on the concept of "classes" and "objects". OOP allows for the creation of modular, reusable, and organized code.

Python supports object oriented programming, and it is the most popular programming paradigm in Python. In OOP, you can define classes to create new types of objects, and you can create instances of those classes (called "objects") to represent specific data and behavior.

::right::

- **Class**: A blueprint for creating objects. It defines a set of *attributes* and *methods* that the objects created from the class will have.
- **Object**: A created instance of a class. The object can have its own values for attributes of the class (called "instance variables") and can use the methods defined in the class.
- **Attributes**: Variables that belong to a class or an object. They can hold data or state information about the object. Attributes can be defined at the class level (shared by all instances) or at the instance level (unique to each instance).
- **Methods**: Functions that belong to a class. They define the behavior of the objects created from the class. Methods can manipulate the attributes of the object and perform actions.

---
layout: top-title-two-cols
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# We've used classes and objects before!

::left::

When we used CSV files, we used CSV DictReader and CSV DictWriter. These are classes that are part of the Python standard library. 

When we created reader instances of these classes, we were creating objects that had specific attributes and methods for working with CSV data.


- **Methods:** `writeheader()` and `writerow()` are methods of the `DictWriter` class that we can call on the `writer` object to perform specific actions related to writing CSV data.
- **Attributes:** The `fieldnames` attribute of the `DictWriter` class is used to specify the field names for the CSV file. When we create a `writer` object, we pass the `fieldnames` as an argument, which sets this attribute for that object.

::right::

```python

from csv import DictReader, DictWriter

with open('data.csv', 'r') as file:
    # reader is an object of the DictReader class
    reader = DictReader(file)  
    for row in reader:
        print(row)

with open('data.csv', 'w') as file:
    # writer is an object of the DictWriter class
    writer = DictWriter(file, fieldnames=['name', 'age'])  
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 30})
    writer.writerow({'name': 'Bob', 'age': 25})
``` 

---
layout: top-title-two-cols
color: blue
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Check for understanding - Match the terms

Match the following terms with their definitions:

::left::

1. Class
2. Object
3. Attribute
4. Method

::right::

A. A created instance of a class that has specific values for its attributes and can use the methods defined in the class.

B. A blueprint for creating objects that defines a set of attributes and methods.

C. A variable that belongs to a class or an object, which can hold data or state information about the object.

D. A function that belongs to a class and defines the behavior of the objects created from the class.

<!-- 
Answer: 
1 - B
2 - A
3 - C
4 - D
-->

---
layout: top-title-two-cols
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Creating a Class

::left::

To create a class in Python, you use the `class` keyword followed by the name of the class and a colon. The body of the class is indented and contains the attributes and methods that define the behavior of the objects created from the class.

```python

class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def greet(self):  # method
        return f"Hi, my name is {self.name}. I am {self.age}."
```

In this example, we have defined a class called `Person` with an `__init__` method (a special method that initializes the attributes of the class) and a `greet` method that returns a greeting message using the attributes of the class.

**If you run this exact code - nothing will happen!**

::right::

 

We have defined the class, but haven't created any objects. 

```python
# creating an object of the Person class
my_person = Person("Alice", 30) 
# calling the greet method on the my_person object
print(my_person.greet())  
```
my_person is an object of the Person class.

**Write the output of this code**

---
layout: top-title-two-cols
color: blue-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# The Constructor (`__init__` method)

::left::

- Whenever Python uses "__" in a method name, it is a special method with a defined purpose. *These are called "dunder" methods (double underscore methods)*.
- The `__init__` method is a special method that is called when an object is created from a class. It must be present for an object to be created. 
- `__init__` is used to initialize the attributes of the class with initial values.
- The `self` parameter is a reference to the current instance of the class. It is used to access the attributes and methods of the class within the class definition.

::right::

```python
from datetime import datetime
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
        self.created_date = datetime.now()  

```

- This `__init__` method requires three parameters: `self`, `name`, and `age`. 
- When we create an object of the `Person` class, we need to provide values for `name` and `age`. 
- The `__init__` method will automatically set the `created_date` attribute to the current date and time.


---
layout: top-title
color: blue-light
transition: fade
zoom: 1.3
class: ns-c-tight
---

::title::

# Lets create a class together!

::content::

Use the Person class example to **create a new class called `Car`** that has **attributes for `make`, `model`, and `year`**, and a **method called `describe`** that returns a string describing the car.

Include code to test that your new Car class works as expected.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def greet(self):  
        return f"Hi, my name is {self.name}. I am {self.age}."

my_person = Person("Bob", 48)
print(my_person.greet())
```
