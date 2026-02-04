---
layout: intro
color: blue
transition: fade
class: text-center
zoom: 1
hideInToc: false
lineNumbers: true
selectable: true
---

# Introduction to Testing

---
layout: top-title
color: purple
zoom: 1.4
class: ns-c-tight
---

::title::

# Prior Knowledge

::content::

## On your mini-whiteboard

You have created a program that takes an age as an input and outputs whether the person is an adult or not.

- How would you test this program?
- Describe your whole process for testing this program.

---
layout: top-title
color: blue-light
zoom: 1.1
class: ns-c-tight
---

::title::

# Bridge: Testing in the Study Design

::content::

Take a look through the Study Design for Unit 3 & 4. 

- Where is testing mentioned?
- What do you need to know about testing this year?

---
layout: top-title
color: blue-light
zoom: 1.02
class: ns-c-tight
---

::title::

# Testing

::content::

Whenever we test, we have to adopt a ==testing mindset==. 

This means we need to think about how to break our code and test our ==boundaries== and our ==edge cases==.

- **Boundaries** are the points where we change from one state to another.
  - When testing for whether an age makes someone an adult, the boundary is 18. We test for 17 (not an adult), 18 (adult), and 19 (adult). **Boundaries are the most common source of bugs** when coding.
- **Edge cases** are scenarios that occur at the extreme ends of input ranges or under unusual conditions. They often reveal hidden bugs in our code.
  - In our age example, edge cases could include negative ages, extremely high ages, or non-integer inputs.
  - **In your first SAC, you will not be expected to validate input, so you don't need to worry about edge cases.**

***In your notes, write your own definition and examples of boundary testing and edge case testing.***

---
layout: top-title
color: blue-light
zoom: 1.3
---

::title::
# Recording Tests
::content::

When we write tests, we need to record the results of our tests. This is important for several reasons:

1. **Documentation**: It helps us keep track of what we have tested and the outcomes, which is useful for future reference.
2. **Debugging**: If a test fails, having a record of the results can help us identify what went wrong and how to fix it.
3. **Regression Testing**: When we make changes to our code, we want to re-rerun the same tests to ensure that our changes haven't introduced new bugs. Having a record of previous test results allows us to compare and identify any regressions.

---
layout: top-title
color: blue-light
---
::title::

# Test Tables

::content::

Test tables are the method that the Study Design uses to record test results. They are a structured way to organize and document the inputs, expected outputs, and actual outputs of our tests.

**Test tables should include the following columns:**

1. **Test Case**: A brief description of the test case. Sometimes called "Feature Tested" or just "Test"
2. **Test Data**: The specific input values used for the test. Also called "Input"
3. **Expected Result**: The expected output or behavior based on the test data. Also called "Expected Output". This is what we expect to happen if our code is working correctly. **Good testing writes the expected result before running the test!**
4. **Actual Result**: The actual output or behavior observed when the test is executed. Also called "Actual Output". This is what actually happens when we run the test.
  - If the test fails, the actual result will differ from the expected result.
  - You can include multiple actual results if you run the test multiple times.

---
layout: top-title
color: blue-light
zoom: 0.95
---
::title::

# Test Table Example

::content::

| Test Case | Test Data | Expected Result | Actual Result |
|-----------|-----------|-----------------|---------------|
| Valid Age | Age: 19 | "Adult" | |
| Valid Age | Age: 18 | "Adult" |  |
| Invalid Age | Age: 17 | "Not an Adult" | |
| Unrealistic Age | Age: -5 | "Invalid Age" | |
| Very High Age | Age: 90 | "Adult" |  |
| Unrealistic High Age | Age: 150 | "Invalid Age" | |
| Non-integer Age | Age: 10.5 | "Invalid Age" | |
| Non-numeric Age | Age: "twenty" | "Invalid Age" | |

---
layout: top-title
color: blue-light
zoom: 1.1
class: ns-c-tight
---
::title::

# Testing Strategy

::content::

When testing, we need to be systematic and thorough. A good testing strategy:

- Identifies the boundaries and edge cases of the problem.
- Covers each logic branch in the code (e.g., if statements, loops).
- Has test cases that give useful feedback whether they pass or fail.

To do this:
- Each test is specific: it is there to test one thing at a time. ==Many small test cases > one big test case==
- Each test is independent: it should not rely on the results of other tests.
- Each test is repeatable: it should give the same results every time it is run with the same input.
---
layout: top-title
color: gray
zoom: 1.1
class: ns-c-tight
---
::title::

# Test-Driven Development (TDD)

::content::

Test-Driven Development (TDD) is a software development process where you write tests before writing the actual code. The TDD cycle consists of three main steps:

1. **Write a Test**: Start by writing a test for a specific functionality or feature that you want to implement. 
2. **Run the Test**: Run the test to see it fail.
3. **Write Code**: Write the code necessary to make the test pass.
4. **Refactor**: Once the test passes, you can refactor your code to improve its structure and readability without changing its behavior.

<Admonition type="info">

*TDD is not part of the study design*, but it is a powerful approach to solving problems you might want to use in your SAC. If you identify the tests before you start writing the code, it helps you ensure you understand the problem you are trying to solve. 

**You might just use some of this approach**. If you are having trouble identifying the logic - writing test cases can help understand the problem.

</Admonition>

---
layout: top-title
color: green-light
zoom: 1.5
class: ns-c-tight
---

::title::

# Practicing Testing

::content::

Regardless of where you got to in the Practice SAC, **lets write the test cases for it.** 

Make sure you:

- Identify the boundaries and edge cases (where relevant).
- Identify each logic branch in the code
- Write specific, repeatable test cases that will help you identify exactly what is working and what is not working in your code.

---
layout: top-title
color: blue-light
zoom: 1.1
class: ns-c-tight
---

::title::

# Automated Testing

::content::

The study design lists **automated testing** as an area you need to be aware of - particularly as an application of AI in software development.

We've already had a go at some automated testing using pytest in our first programming exercises. They have the advantage of:

- Being fast to run
- Being repeatable and consistent
- Providing detailed feedback on which tests passed and which failed
- Being able to be integrated into a development workflow (e.g., run tests automatically when code is changed)

---
layout: top-title
color: blue-light
zoom: 1.3
class: ns-c-tight
---
::title::

# AI in Automated Testing

::content::

LLMs (like ChatGPT, Github Copilot, Claude or Gemini) can be used to generate test cases - either based on the description of the problem, or the code itself. 

This can be a powerful way to quickly generate a large number of test cases, but it is important to review the generated test cases to ensure they are relevant and accurate (as with any AI output).

<Admonition color="blue" title="What do I need to remember?">

*AI can be a powerful tool for improving ==efficiency== in testing and potentially even ==effectiveness==, but only if used under the close supervision of a human tester/developer.*

</Admonition>

---
layout: top-title
color: purple
zoom: 1.3
class: ns-c-tight
---

::title::

# Reflect

::content::

**In your notes, write 4-5 key points you want to remember about testing**

Make sure you include a description of testing tables, testing strategies and the application of AI to testing. 

**Write 2 questions you should be able to answer when you are revising this topic.**