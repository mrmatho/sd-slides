---
layout: cover
color: red
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Use Case Diagrams

---
src: ./u3o1_tracking.md
hide: false
---

---
layout: top-title-two-cols
color: red
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Use Case Diagrams - Getting Started

::left::

A **use case diagram** is a visual representation of the interactions between users (or "actors") and a system. It helps to identify the different ways **users can interact with the system** and the various functionalities it provides. Use case diagrams are commonly used in software development to capture and communicate requirements.

***In a simple use case diagram, you have:***

- **Actors**: These are the users or external systems that interact with the system. They are represented as stick figures or icons.
- **Use Cases**: These are the specific actions or functionalities that the system provides to the actors. They are represented as ovals or ellipses.
- **Relationships**: The lines connecting actors to use cases show that there is an interaction between them.

::right::

![Basic UCD](/img/basic_ucd.png)

---
layout: top-title
color: green
zoom: 1.2
class: ns-c-tight
---
::title::

# Actors

::content::

- Actors represent the users or systems
- They can be human users, external systems, or even other software components
- Actors are depicted as stick figures or icons
- They are never named with their name (eg. "Adam", "Belinda", etc.) but rather with their role (eg. "Customer", "Admin", etc.)
- An actor can have multiple use cases, and a use case can be associated with multiple actors

![Actor](\img\actor.png)
---
layout: top-title
color: green
zoom: 1.2
---

::title::

# Use Cases

::content::

- Use cases represent the **specific actions or functionalities** that the system provides to the actors
- They are depicted as ovals or ellipses
- Use cases are best named with a verb and a noun (eg. "Place Order", "Delete User", etc.)

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Check for Understanding - Actors and Use Cases

::content::

1. True/False: An actor is always a human user
2. True/False: An actor can have multiple use cases, and a use case can be associated with multiple actors
3. What would be a good name for a use case that allows a customer to change the details of an order they have placed?
4. Describe what the use case diagram below represents:
![UCD Example](/img/ucd_example.png)

---
layout: top-title
color: green
zoom: 1.1
class: ns-c-tight
---
::title::

# Relationships

::content::

- Relationships show how actors and use cases are connected
- The most common relationship is the "association" relationship, which is represented by a solid line connecting an actor to a use case. This indicates that **the actor interacts with the use case**.
  - This just means they are in some way connected, but it doesn't specify how they are connected. 
- **Include** relationship: This is represented by a dashed arrow pointing from one use case to another. 
  - Include indicates that one use case includes the behavior of another use case. 
  - E.g. "Place Order" might include "Validate Payment" because validating payment is a necessary step in placing an order.
- **Extend** relationship: This is represented by a dashed arrow pointing from one use case to another, but it indicates that the behavior of the second use case **optionally** extends the behavior of the first use case.

---
layout: top-title
color: green
zoom: 1.1
class: ns-c-tight
---
::title::

# Includes and Extends - Example

::content::

![Includes and Extends](/img/includes_extends.png)

Note that: 

- The arrows go in opposite directions: an include relationship points **from the base** use case **to the included** use case, while an extend relationship points **from the extending use case to the base** use case.
- The extend should usually show the condition for when extend occurs. 
- Include or extend are the only associations between two use cases. Regular association should not exist between two use cases - only ever between an actor and a use case.

---
layout: top-title
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Check for Understanding - Relationships

::content::

1. What does an association relationship indicate in a use case diagram?
2. A use case "Generate Report" has a relationship with the use case "Validate Data". What type of relationship would you expect between these two use cases, and why?
3. **Scenario:** A customer can place an order, which includes validating payment and checking inventory. If the inventory is low, the system should extend the "Place Order" use case to include a "Notify Customer" use case. When inventory is low, the manager needs to be notified.
  - Who are the actors in this scenario?
  - What are the use cases in this scenario?
  - Draw the use case diagram.