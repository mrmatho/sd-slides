---
layout: cover
color: green-light
transition: fade
zoom: 1
class: ns-c-tight
hideInToc: false
---

# Finalised Design and Design Tools

---
layout: top-title
color: green-light
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Finalised Design and Design Tools

::content::

For your finalised design, we need a much clearer and more detailed representation of the design. This should include: 

- Annotated mockups (more detail than sketches, including annotations to explain design decisions)
- Data Dictionary for key variables and data structures
- IPO Chart
- Pseudocode and Object Descriptions (Very High: 9-10)

---
layout: top-title
color: green-light
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

# Mockups

::content::

Mockups are detailed visual representations of the user interface, showing the layout, design elements, colour scheme, typography and interactions. They are more polished than sketches and include annotations to explain design decisions.

Mockup tools: 
- Pro-level: 
  - Figma (professional level)
- Base level:
  - Canva
  - PowerPoint (simple and effective)
  - Google Drawings

---
layout: top-title
color: green-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Data Dictionary

::content::

We've looked at data dictionaries before, but a data dictionary must include:
- Variable Name
- Data Type
- Description

If needed for clarity, it can also include an example value

| Variable Name | Data Type | Description | Example Value |
| --- | --- | --- | --- |
| customer_name | String | The name of the customer | "John Doe" |
| order_details | Dict | A Dict containing details of the customer's order |   \{ "item": "Laptop", "quantity": 1, "price": 999.99 \}  |

---
layout: top-title
color: green-light
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# IPO Chart

::content::

An IPO (Input-Process-Output) chart is a tool used to represent the inputs, processes and outputs of a system. It helps to clarify the flow of data and the operations performed on that data. 

Your IPO chart should start from the DFD and identify the life-cycle of key data flows, showing how data is transformed and processed within the system.

| Input | Process | Output |
| --- | --- | --- |
| username and password | Validate Login | login_success (Boolean) |
| order_details | Process Order | order_confirmation (Dict) |

---
layout: top-title-two-cols
color: green-light
transition: fade
zoom: 1.2
class: ns-c-tight
---
::title::

# Pseudocode 

::left::

Pseudocode is a high-level description of the system's logic and functionality, written in a way that is easy to understand. It should include the main processes and interactions of the system, and can be used to guide the development of the actual code.

You need to write some basic pseudocode for things like: 
- Main program flow
- Important functions (search, place order, update item, etc.)

::right::

```
# Main program flow

WHILE TRUE
  display_menu()
  choice <- get_user_input()
  
  IF CHOICE IS 1
      search_items()
  ELSE IF CHOICE IS 2
      place_order()
  ELSE IF choice IS 3
      update_item()
  ELSE
      BREAK
```

---
layout: top-title
color: green-light
transition: fade
zoom: 1.2
class: ns-c-tight
---
::title::

# Object Descriptions

::content::

Object descriptions should include the key classes and their objects in your system, their attributes and methods. This helps to clarify the structure of your system and how different components interact with each other.

| Class Name | Attributes | Methods |
| --- | --- | --- |
| User | username, password, address | login(), update_address() |
| Order | order_details, order_status | place_order(), cancel_order() |

---
layout: top-title
color: green-light
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# You need to submit...

::content::

***S Standard***:

- Annotated mockups
- Data Dictionary
- IPO Chart

***Top Marks***:

- Pseudocode
- Object Descriptions