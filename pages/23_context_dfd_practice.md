---
layout: cover
color: purple
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Context Diagrams, Use Case Diagrams and Data Flow Diagrams Practice

---
layout: top-title
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Scenario

::content::

A secondary school uses a software system to manage its library. Students can search the book catalogue, borrow available books, and return books they have on loan. Librarians can add new books to the catalogue, register new student members, and process borrowing and return transactions. 

When a student borrows a book, the system checks their membership details and the book's availability before recording the loan. If the book is unavailable, the system can send a request to the inter-library loan system. The system stores a catalogue of all books, a record of all registered members, and a history of all loan transactions.

## Our steps

- Identify the entites/actors
- Choose which diagram is easiest to start with
  - Use Case Diagram: Focus on interactions between users and the system
  - Context Diagram: Identify any inputs and outputs
  - Data Flow Diagram: Connect inputs and outputs to processes. Identify how those processes link to others, and where data is stored and retrieved from

---
layout: top-title
color: purple
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Identify the entities/actors

::content::

A secondary school uses a software system to manage its library. <span v-mark.highlight.yellow>Students</span> can search the book catalogue, borrow available books, and return books they have on loan. <span v-mark.highlight.red> Librarians</span> can add new books to the catalogue, register new student members, and process borrowing and return transactions. 

When a student borrows a book, the system checks their membership details and the book's availability before recording the loan. If the book is unavailable, the system can send a request to the <span v-mark.highlight.green>inter-library loan system</span>. The system stores a catalogue of all books, a record of all registered members, and a history of all loan transactions.

<v-clicks>

- Student
- Librarian
- Inter-library loan system

</v-clicks>

---
layout: top-title
color: purple
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Use Case Diagram

::content::

How do these actors (Student, Librarian, Inter-library loan system) interact with the system? 

A secondary school uses a software system to manage its library. Students can search the book catalogue, borrow available books, and return books they have on loan. Librarians can add new books to the catalogue, register new student members, and process borrowing and return transactions. 

When a student borrows a book, the system checks their membership details and the book's availability before recording the loan. If the book is unavailable, the system can send a request to the inter-library loan system. The system stores a catalogue of all books, a record of all registered members, and a history of all loan transactions.

<v-clicks>

- Student: Search book catalogue, Borrow book, Return book
- Librarian: Add new book, Register new member, Process loan, Process return, Request inter-library loan
- Inter-library loan system: Request inter-library loan

</v-clicks>

---
layout: top-title
color: purple
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Context Diagram - What are the inputs and outputs?

::content::

A secondary school uses a software system to manage its library. Students can search the book catalogue, borrow available books, and return books they have on loan. Librarians can add new books to the catalogue, register new student members, and process borrowing and return transactions. 

When a student borrows a book, the system checks their membership details and the book's availability before recording the loan. If the book is unavailable, the system can send a request to the inter-library loan system. The system stores a catalogue of all books, a record of all registered members, and a history of all loan transactions.

---
layout: top-title
color: purple
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# Data Flow Diagram - How do the processes link together?

::content::

A secondary school uses a software system to manage its library. Students can search the book catalogue, borrow available books, and return books they have on loan. Librarians can add new books to the catalogue, register new student members, and process borrowing and return transactions. 

When a student borrows a book, the system checks their membership details and the book's availability before recording the loan. If the book is unavailable, the system can send a request to the inter-library loan system. The system stores a catalogue of all books, a record of all registered members, and a history of all loan transactions.

---
layout: top-title
color: purple
transition: fade
zoom: 1.2
class: ns-c-tight
---

::title::

# On your own - Scenario

A local sports club uses a system to manage player registrations and training session bookings. Players can register with the club, view available training sessions, and book or cancel a spot in a session. 

Coaches can add new training sessions and view a list of players who have booked into their sessions. 

Club administrators can update player details and produce membership reports. 

When a player books a session, the system checks their registration status and the session's available capacity before confirming the booking. The system stores player registration details, a list of training sessions, and a record of all bookings.

