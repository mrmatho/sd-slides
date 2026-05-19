---
layout: cover
color: yellow
transition: fade
zoom: 1
class: ns-c-tight
hideInToc: false
---

# Software Requirements Specification (SRS)

---
layout: top-title
color: yellow
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# What is a Software Requirements Specification (SRS)?

::content::

<SpeechBubble position="c" color="orange" shape="round">

A Software Requirements Specification (SRS) is a comprehensive document that describes the software system to be developed. 

</SpeechBubble>

Our Software Requirements Specifications include:

- **Functional Requirements**: What the system should do (features, use cases, etc.)
- **Non-Functional Requirements**: Performance, security, usability, etc.
- **Constraints**: Limitations on design, implementation, or deployment.
- **Scope**: What is included and excluded from the project.
- **User Characteristics**: Who the users are and their needs.
- **Technical Environment**: Hardware, software, and network requirements.
- **Analytical Tools**: The UCD, context diagrams and DFDs that help understand how your system will work.

---
layout: top-title
color: yellow
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Why is an SRS important?

::content::

- **Problem Solving** Breaks down the problem into smaller, manageable parts, making it easier to understand and implement.
- **Clarity**: Provides a clear and detailed description of the software requirements, reducing misunderstandings between stakeholders and developers.
- **Planning**: Helps in project planning, resource allocation, and scheduling by outlining the scope and requirements of the project.
- **Testing**: Serves as a basis for creating test cases and validating that the software meets the specified requirements.
- **Reference Point**: Acts as a reference document throughout the software development lifecycle, ensuring that the project stays on track and meets its goals.

---
layout: top-title
color: yellow
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# SRS in the SAT

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

In the SAT, the SRS is worth 10 marks and is part of Criterion 3: Software Development, not including the marks already allocated to use of analytical tools (in Criterion 2).

</SpeechBubble>

According to the criteria, you will be assessed on documenting...:

- Functional and non-functional requirements
- Constraints that impact the development of the software solution
- How the analytical tools inform the SRS
- The limits of the project's scope
- The technical environment

as well as:
- Documented evidence of how you have thought critically and creatively about data you collected to inform your SRS

---
layout: top-title-two-cols
color: yellow
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Functional and Non-Functional Requirements

::left::

<SpeechBubble position="c" color="orange-light" shape="round">

**Functional Requirements** describe what the system should do, such as specific features, use cases, or user interactions.

</SpeechBubble>

Functional requirements will be informed heavily by your use case and data flow diagrams. 

For example, if your use case diagram includes a "User Login" use case, then a functional requirement might be "The system shall allow users to log in using their email and password."

::right::

<SpeechBubble position="c" color="red-light" shape="round">

**Non-Functional Requirements** describe how the system should perform, such as performance, security, usability, etc.

</SpeechBubble>

Non-functional requirements are more likely to come from your data collection and user research. 

For example, if your user research indicates that users need to access the system on mobile devices, a non-functional requirement might be "The system shall be responsive and accessible on mobile devices."

---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# What makes a good requirement

::content::

***A good requirement should be:***
- **Clear**: It should be easy to understand and unambiguous.
- **Concise**: It should be brief and to the point, without unnecessary details.
- **Testable**: It should be possible to verify that the requirement has been met through testing.
- **Feasible**: It should be realistic and achievable within the constraints of the project.
- **Prioritised**: It should be clear which requirements are essential and which are optional.

<v-click>

## Which of these is not a good requirement? Why?

1. The system shall allow users to log in using their email and password. 
2. The system shall be user-friendly and fast. 
3. The system shall be responsive and accessible on mobile devices.
4. The system will include a feature that allows users to share their progress on social media platforms.

</v-click>

---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# Constraints

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

**Constraints** are limitations that impact the development of the software solution. We categorise constraints as: 

- Economic
- Technical
- Legal
- Social

</SpeechBubble>

Whenever you discuss constraints, be sure to clearly identify the type of constraint. 

---
layout: top-title-two-cols
color: yellow
class: ns-c-tight
---

::title::

# Constraint Types

::left::

<SpeechBubble position="l" color="orange-light" shape="round">

**Economic Constraints** refer to limitations related to budget, funding, or financial resources. **Time** is also an economic constraint. For example, "The project cannot spend any money on external software libraries"

</SpeechBubble>

<SpeechBubble position="l" color="red-light" shape="round">

**Technical Constraints** refer to limitations related to technology, such as hardware, software, or technical expertise. For example, "The system must be developed using Python and Django."

</SpeechBubble>

Constraints need to be described clearly and specifically. They should be directly related to the project and as detailed as possible. For example, instead of saying "The project has a limited budget," you could say "The project has a budget of $10,000 for software development and testing." 

::right::

<SpeechBubble position="r" color="green-light" shape="round">

**Legal Constraints** refer to limitations related to laws, regulations, or industry standards. For example, "The system must comply with The Privacy Act 1988 by ensuring that user data is stored securely and not shared with third parties without consent."

</SpeechBubble>



<SpeechBubble position="r" color="blue-light" shape="round">

**Social Constraints** refer to limitations related to societal norms, cultural expectations, or user preferences. For example, "The system must be designed to be inclusive and accessible to users with disabilities."

</SpeechBubble>



---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# Scope

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

**Scope** defines what is included and excluded from the project. It helps to set boundaries and manage expectations for stakeholders and developers. 

</SpeechBubble>

Scope may include a definition of a set of release cycles, where each release cycle includes a set of features or requirements that will be implemented and delivered together.

Scope is generally focused especially on the features not included, to avoid any misconceptions about what the software solution will do. For example, "The system will not include a feature for users to reset their passwords."

---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# Technical Environment

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

**Technical Environment** describes the hardware, software, and network requirements for the software solution. It may include details about the programming languages, frameworks, libraries, databases, and other tools that will be used in the development and deployment of the software solution. 

Technical environment should clearly distinguish between the development environment (tools and technologies used to build the software) and the deployment environment (the hardware and software environment where the software will be deployed and used).

</SpeechBubble>

You won't be held to assumptions made in your discussion of the technical environment, but you do need to be realistic and clear.

---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# User Characteristics

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

**User Characteristics** describe who the users of the software solution are and their needs. This may include demographic information, user personas, user goals, and user preferences.

</SpeechBubble>

- User characteristics are about a "target user", rather than just describing users in general.
- Some things included in user characteristics might be close to stereotypes, but they need to be based on data collected, rather than just personla feelings. 
- User characteristics should be directly relevant to the design and development of the software solution. For example, if your software solution is a mobile app for teenagers, your user characteristics might include information about their age range, interests, and technology usage habits.

---
layout: top-title
color: yellow
class: ns-c-tight
---

::title::

# Summary

::content::

<SpeechBubble position="c" color="orange-light" shape="round">

The SRS is a comprehensive document that describes the software system to be developed, including **functional and non-functional requirements**, **constraints**, **scope**, **user characteristics**, and **technical environment**.

</SpeechBubble>

The SRS is important for problem-solving, clarity, planning, testing, and as a reference point throughout the software development lifecycle.