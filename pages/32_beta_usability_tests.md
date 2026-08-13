---
layout: top-title
color: orange
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---
::title::

# Beta Testing - Usability Tests

::content::

Beta testing is a phase in software development where a product is released to a limited audience for real-world exposure. Usability tests are conducted during this phase to evaluate how user-friendly and intuitive the software is.

The *Applied Computing: Software Development* course combines beta testing and usability testing as once concept. We will conduct usability tests to gather feedback from users on the usability of our software.

---
layout: top-title-two-cols
color: orange
---

::title::

# Building a Usability Test Plan

::left::

## Test Scenarios

A usability test plan needs to first identify important scenarios for testing. These should cover both the most common or critical tasks, as well as identifying tasks that might be more complicated to complete.

<div class="note">

For a social media app, common tasks might include creating a post, liking a post, and following a user. More complicated tasks might include changing privacy settings or reporting inappropriate content.

</div>

::right::

## Test Users

Test users should (as much as possible) represent the target audience of the software. The usability test plan should identify any specific characteristics of test users, such as age-profile, technical expertise, or accessibility needs.

Our ability to gather specific users will be limited, but we can identify our best-case scenario as part of the documentation of the usability test plan.

---
layout: top-title-two-cols
color: orange
class: ns-c-tight
---

::title::

# Writing the Usability Beta Tests

::left::

A usability test plan should include a set of tasks for the test users to complete. Each task should be clearly defined and include any necessary instructions or context.

They should not identify any specific user interface elements, approaches or solutions. The goal is to evaluate whether the user can complete the task successfully, and how easily they can do so.

::right::

## Usability Test Script Sample

### Task 1: Change Preferred Name

1. Open the application and log in with username "testuser" and password "password123".
2. Change the preferred name in the user profile to "Tester".
3. Write a new post with the title "Usability Test" and the content "This is a test post for usability testing."

<div class="note">

**Important:** The test plan needs to provide any input data the user should use, so that any pause or confusion is about the program itself, and not about what the user should do. The test plan must **not** provide hints or guidance on **how** to complete the tasks.

</div>

---
layout: top-title
color: orange
---

::title::

# Recording Usability Test Results

::content::

## Methods of recording usability test results include

- **Observation**: The test facilitator observes the user as they complete the tasks, taking notes on any difficulties or confusion encountered.
- **Screen Recording**: The user's screen is recorded during the test, allowing for later review and analysis of their interactions with the software.
- **Participant Recording**: The user is asked to think aloud as they complete the tasks, providing insight into their thought process and decision-making.
- **Post-Test Questionnaire**: After completing the tasks, the user is asked to complete a questionnaire to provide feedback on their experience, including any difficulties encountered and suggestions for improvement.

---
layout: top-title
color: orange
zoom: 0.85
class: ns-c-tight
---

::title::

# What do I do with the results?

::content::

**The results of your usability tests need to be:**

- Documented
- Analyzed
- Used to recommend modifications to the software solution.
- Used to evaluate the proposed modifications.

| Result | Interpretation | Recommendation |
| ------ | -------------- | ---------------- |
| User was able to write a post successfully without hesitation | This feature is usable and intuitive | No changes needed |
| User clicked on "Profile" to change their preferred name, instead of settings | The navigation to change preferred name is not intuitive | Add a direct link to change profile details like preferred name in the profile section |
| When hurrying, user left a spelling mistake in their post title. They were forced to delete and re-write the post | The software does not provide an easy way to edit posts, or check them before | Consider adding an "Edit Post" feature to allow users to correct mistakes, or give a preview of the post before the final submission |

---
layout: top-title
color: orange
zoom: 0.8
---

::title::

# Beta Test Plan: Criteria 9 (VCAA Criteria)

::content::

| Criteria | Very Low | Low | Medium | High | Very High |
| ---------- | ---------- | ----- | -------- | ------ | ----------- |
| **Preparation of the beta testing plan and test scenarios.** | Lists components of the software solution to be used in testing | Prepares a beta testing plan that targets the appearance of the software solution. | Prepares a beta testing plan that targets the functionality of the software solution. | Prepares a beta testing plan that targets the functional and nonfunctional requirements of the software solution. | Prepares a beta testing plan that includes test scenarios that target relevant characteristics of user experience. |
| | | Outlines potential users to participate in the beta testing. | Explains why potential users have been selected to participate in beta testing. | Documents how beta test results will be collected | Clear and concise |
| **Conduction of beta testing.** | Conducts beta testing with one potential user. | Conducts beta testing and lists results using one data collection method. | Conducts beta testing and collects results by using two data collection methods. | Conducts beta testing with multiple potential users and collects results using three or more data collection methods. | Prepares the data collected for the documenting of the results of the beta tests. |

---
layout: top-title
color: orange
zoom: 0.8
class: ns-c-tight
---

::title::

# Beta Test Plan: Criteria 9 (Continued)

::content::

| Criteria | Very Low | Low | Medium | High | Very High |
| ---------- | ---------- | ----- | -------- | ------ | ----------- |
| **Documents the results of the beta tests.** | Lists results of the beta tests. | Outlines the results of the beta tests. | Describes the results of the beta tests in a brief. | Documents the results of the beta tests in a report. | Documents and explains a complete set of results of the beta tests in a detailed report. Clear and concise. |
| **Documents the recommended modifications to the software solution based on the results of the beta testing.** | Identifies minor modifications to the software solution. | Outlines the  modifications to the software solution. | Recommends and documents the modifications to the software solution. | Explains the purpose of the modifications to the software solution. | Evaluates the modifications to the software solution based on the results of the beta testing. |

<div class="note">

**What you need to submit:** (In one or multiple documents, as appropriate)

- Beta (Usability) Testing Plan
- Documented Results
- Test Results Report, including description and evaluation of modifications

</div>
