---
layout: cover
color: blue
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Design Tools for Creating Modules

---
layout: top-title
color: blue-light
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

# Design Tools for Creating Modules

::content::

In Software development, we use a variety of design tools to answer two questions:

1. *What should the module look like?*
2. *How should the module work?*

We use **mock-ups** to answer the first question, which we call the ==visual design== of the module. 

Answering the second question is about the ==logical design== or ==functional design== of the module. We use:

- **Data-dictionaries** to clarify the data variables involved
- **Input-Process-Output (IPO) charts** to clarify the overall process of the module
- **Pseudocode** to clarify the logic of the module
- **Object Descriptions** to clearly define the objects we use once we are using Object-Oriented Programming (OOP) - later in this unit

---
layout: top-title
zoom: 1.3
color: green-light
class: ns-c-tight
---
::title::

# Mock-ups

::content::

Mock-ups are probably the simplest design tool. They are a drawing of what the graphical user interface (GUI) of the module will look like.

Mock-ups should include annotations that clarify the purpose of each element of the GUI, where necessary. 

<Admonition color="yellow-light" title="SAC Mock-ups">

For our first two SAC modules - the mock-ups you receive are just text because the user interface is all terminal based. 

</Admonition>

---
layout: top-title
zoom: 1.15
color: green-light
class: ns-c-tight
---

::title::

# Data Dictionaries

::content::

The data dictionary is a table that describes the variables that are used in the module. It should include:

- The name of the variable (which should be exactly the same as the variable name used in the code)
- The data type of the variable (e.g., string, integer, list, etc.)
- A description of the variable (which should clarify how the variable is used in the module)

<Admonition color="yellow-light" title="Follow the Data Dictionary!">

Once a variable is included in the data dictionary, it should be used in the code named exactly as it is described in the data dictionary. This is important for consistency and clarity. **Remember** - while most of our coding happens individually, software development mostly happens in teams. The data dictionary is part of keeping everyone's code readable for all members of the team, and reduces the chance of errors. 

For our SAC - the data dictionary is provided and gives you a hand with identifying the variables you need to use and how to use them. If a variable is in the data dictionary but not in your code: something has gone horriblly wrong!

</Admonition>

---
layout: top-title
zoom: 1.15
color: green-light
class: ns-c-tight
---

::title::

# Input-Process-Output (IPO) Charts

::content::

An IPO chart is a design tool that helps clarify the overall process of the module. It breaks down the module into three main components:

- **Input**: What data is received by the module? This should align with the variables in the data dictionary.
- **Process**: What does the module do with the input data? This should clarify the main steps or logic of the module.
- **Output**: What does the module output? This should also align with the variables in the data dictionary.


<Admonition color="yellow-light" title="IPO Charts for SACs">

For more complex SAC modules, you will receive an IPO chart. The first SAC has very simple requirements so the addition of an IPO chart was not necessary.

</Admonition>

---
layout: top-title
zoom: 1.15
color: green-light
class: ns-c-tight
---

::title::

# Example IPO Charts

::content::

| Input | Process | Output |
| --- | --- | --- |
| User Details (Name, age, emailValidate age (must be 18 or older) | If valid: "Welcome, [Name]!". If invalid: "Sorry, you must be 18 or older to enter." |
|   | Validate email address (must contain "@" and ".") | If valid: "Welcome, [Name]!". If invalid: "Sorry, you must provide a valid email address." |
|  |  |  |
| Daily hours, job type, weekend Y/n, public holiday Y/n | Calculate pay based on hours, job type, and whether it's a weekend or public holiday. Calculate tax based on pay. | Formatted Pay slip showing gross pay, tax, and net pay. |

---
layout: top-title
zoom: 1.15
color: green-light
class: ns-c-tight
---

::title::

# Pseudocode

::content::

Pseudocode is a design tool for using code-like language to clarify the coding approach.

- It is not actual code, so shouldn't follow the syntax of any particular programming language.
- It should be specific enough to clarify the logic of the code, but not so specific that it becomes actual code.

VCAA use pseudocode with some specific formats - for example, they use `IF...THEN...ELSE...ENDIF` statements to clarify the logic of conditional statements. They also tend to use <- for assignment statements, and use indentation and `END` to clarify the logic of loops and conditions. 

<Admonition color="yellow-light" title="Pseudocode for SACs">

You won't always get pseudocode for your SACs, but when you do it is VERY helpful. Always follow any provided pseudocode closely - it is a very strong hint about the logic you need to implement in your code.

</Admonition>

<Admonition color="blue-light" title="In your SAT">

For your SAT project, you will need to create your own designs, and pseudocode is one that students often want to skip past. Pseudocode is very helpful in that scenario - it makes sure you can have a clear plan for the code before you get bogged down in the details.

</Admonition>

---
layout: top-title
zoom: 1.15
color: green-light
class: ns-c-tight
---

::title::

# Object Descriptions

::content::

Object descriptions are a design tool used in Object-Oriented Programming (OOP) to clarify the objects that will be used in the module. They should include:

- The name of the object
- The attributes of the object (which should align with the variables in the data dictionary)
- The methods of the object (which should clarify the actions that can be performed on the object)

---
layout: top-title
zoom: 1.15
color: purple-light
class: ns-c-tight
---

::title::

# SAT Task - Brainstorming Activity

::content::

Last lesson we talked about CRUD applications - Create, Read, Update and Delete. These are the four main functions of many applications - particularly those that involve databases.

This is a good chance to work in pairs to help you brainstorm some ideas for your SAT project. In your groups: identify ideas that one or more of you might follow up on for your SAT project. Try to identify:

- The main purpose of the application (what problem does it solve? What need does it meet?)
- The main features of the application (what can users do with it?)
- The main data variables involved in the application (what data will the application need to function? What data will it output?)
- Is this idea extendable? (is there potential to add more features or complexity to this idea if you wanted to?)
- Is this idea feasible? (is this something you think you could create with some learning and effort?)