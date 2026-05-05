---
layout: cover
color: blue
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Context and Data Flow Diagrams

---
src: ./u3o1_tracking.md
hide: false
---

---
layout: top-title-two-cols
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Context Diagrams

::left::

- **Use Case Diagrams** are focused on identifying the ways users interact with the system
- **Context Diagrams** are focused on the data that flows between the system and its external entites (eg. users, external systems, etc.)
- A context diagram shows all the input and output data flows for a system, and the sources and destinations of system data.

::right::

- **External Entities** are like actors, but they represent the source and destination of data rather than the users of the system. They are represented as rectangles.
- **Data Flows** are represented as arrows, and they show the flow of data between the system and the external entities. The direction of the arrow indicates the direction of data flow.
- The **System** is represented as a circle or oval in the center of the diagram

---
layout: top-title
color: blue
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Context Diagrams - Conventions

::content::

<img src="/img/context_example.png" alt="Context Diagram Example" style="width: 400px; float:right; height: auto;"/>

- System as a circle
- External Entity as a rectangle
- Data Flow as an arrow
  - Name of data on each arrow, in variable form (eg. "customer_name", "order_details", etc.)
  - Each data flow gets its own arrow

---
layout: top-title
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

## Check for understanding - what does this show?

::content::

<img src="/img/customer_context.png" alt="Context Diagram Example - Customer" style="width:550px; float:right; height: auto;"/>

On your mini-whiteboard, describe what can be inferred about the system from this context diagram.

<v-clicks>

- **Customer input** (sent to the system): 
  - username and password
  - address details
- **System output** (sent to the customer): 
  - order details
  - order confirmation, etc.

</v-clicks>

---
layout: top-title
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Data Flow Diagrams

::content::

A **Data Flow Diagram (DFD)** is the next level of detail after a context diagramn. It shows the internal processes of the system, and how data flows between these processes and the external entities.

As well as the external entities and data flows shown in a context diagram, a DFD also includes:
- **Processes**: These are represented as circles and they represent the internal processes of the system **that transform data**. Each process should have a unique name that describes its function (eg. "Process Order", "Validate Payment", etc.)
- **Data Stores**: These are represented as open rectangles, and they represent where **data is stored** within the system (eg. databases, files, etc.). Each data store should have a unique name that describes the type of data it stores (eg. "Customer Database", "Order Records", etc.)

---
layout: top-title
color: blue
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Data Flow Diagrams - Example

::content::

<img src="/img/customer_dfd.png" alt="Data Flow Diagram Example" style="width: 500px; float:right; height: auto;"/>

- All the data flows from the context diagram are still present, but now we can see the internal processes and data stores of the system.
- The `username`, `password` data flow now connects to a login process. This receives `username` and `password_hash` from the authentication system for verification. 
- Place order receives `address_details` and returns a receipt. It creates a `new_order`
- The `shipping_notification` data flow comes from the Shipment Notification process, which receives the `shipped_order` data flow from the Orders Database data store.

==Note:== Numbering of processes do not need to follow a logical order, but we use numbering to help us identify processes and create level 1 and level 2 DFDs. 