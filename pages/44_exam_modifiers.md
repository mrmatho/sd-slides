---
layout: cover
color: blue-light
hideInToc: false
---

# Exam Review: Access Modifiers, Scope & Constants

---
layout: top-title
color: blue-light
zoom: 0.9
class: ns-c-tight
---

::title::

# Access Modifiers

::content::

Access modifiers control **which parts of a program can see and use** an attribute or method of a class.

| Modifier | Symbol (class diagram) | Who can access it? |
| --- | :---: | --- |
| **Public** | `+` | Any code, inside or outside the class |
| **Protected** | `#` | The class itself **and its subclasses** (child classes) |
| **Private** | `-` | **Only** the class itself |

<Admonition title="Why use them?" color="yellow-light">

Access modifiers support **encapsulation**. They hide an object's internal data so it can only be changed through controlled methods, which protects the **integrity** of the data.

</Admonition>

---
layout: top-title-two-cols
color: blue-light
zoom: 1.1
class: ns-c-tight
---

::title::

# Access Modifiers in Python

::left::

Python does **not enforce** access modifiers. It uses **naming conventions** instead:

- `name` is **public**
- `_name` (one underscore) is **protected**: a signal to other programmers to leave it alone
- `__name` (two underscores) is **private**: Python renames it (*name mangling*) so it is hard to reach from outside the class

<SpeechBubble position="l" color="sky-light" shape="round">

Other languages, such as Java and C#, use the keywords `public`, `protected` and `private`, and the compiler enforces them.

</SpeechBubble>

::right::

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._branch = "Heathmont"  # protected
        self.__balance = balance    # private

    def deposit(self, amount):      # public method
        if amount > 0:
            self.__balance += amount

    def get_balance(self):          # public method
        return self.__balance


account = BankAccount("Sam", 100)
account.deposit(50)
print(account.get_balance())  # 150
print(account.__balance)      # AttributeError
```

---
layout: top-title-two-cols
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Access Modifiers in Class Diagrams

::left::

In the exam, you may need to **read or complete** a class diagram that uses access modifier symbols.

- Attributes are usually **private** (`-`)
- Methods that other objects call are usually **public** (`+`)
- Attributes or methods that subclasses need are **protected** (`#`)

::right::

```text
┌──────────────────────────────┐
│         BankAccount          │
├──────────────────────────────┤
│ + owner : String             │
│ # branch : String            │
│ - balance : Floating Point   │
├──────────────────────────────┤
│ + deposit(amount) : Boolean  │
│ + getBalance() : Floating Pt │
│ - logTransaction() : None    │
└──────────────────────────────┘
```

---
layout: top-title-two-cols
color: blue-light
zoom: 1.1
class: ns-c-tight
---

::title::

# Local and Global Variables

::left::

**Scope** is the part of a program where a variable can be used.

**Local variable**

- Declared **inside** a function or method
- Only exists while that function runs
- Cannot be used outside it

**Global variable**

- Declared **outside** all functions
- Can be read from **anywhere** in the program
- In Python, a function must use the `global` keyword to **change** it

::right::

```python
total_sales = 0   # global variable

def add_sale(amount):
    global total_sales
    gst = amount * 0.1      # local variable
    total_sales += amount + gst

add_sale(100)
print(total_sales)  # 110.0
print(gst)          # NameError: gst is local
```

---
layout: top-title-two-cols
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Local vs Global: Why It Matters

::left::

**Advantages of local variables**

- Each function is **self-contained**, so it is easier to test and debug
- The same name can be reused in different functions without clashing
- Memory is released when the function ends

::right::

**Disadvantages of global variables**

- **Any** part of the program can change them, so errors are hard to trace
- Functions that depend on them are harder to reuse and test
- Two developers may accidentally use the same name

<Admonition title="Good practice" color="yellow-light">

Pass values into functions as **parameters** and send results back with **return**, rather than relying on global variables.

</Admonition>

---
layout: top-title-two-cols
color: blue-light
zoom: 1
class: ns-c-tight
---

::title::

# Constants

::left::

A **constant** is a named value that is set once and **does not change** while the program runs.

- Python has no true constant, so the convention is to use **UPPER_CASE** names
- Constants are often declared **globally**, because they are safe to share: nobody should change them

**Why use constants?**

- **Readability:** `GST_RATE` explains itself; `0.1` does not
- **Maintainability:** change the value in **one place** and every use updates
- **Fewer errors:** no mistyped "magic numbers" scattered through the code

::right::

```python
GST_RATE = 0.1        # constant
MAX_LOGIN_ATTEMPTS = 3

def add_gst(amount):
    return amount * (1 + GST_RATE)

def is_locked(attempts):
    return attempts >= MAX_LOGIN_ATTEMPTS
```

---
layout: top-title
color: blue-light
zoom: 1.2
class: ns-c-tight
---

::title::

# Exam Tips

::content::

- Use the **formal terms**: *public*, *protected*, *private*, *scope*, *local*, *global*, *constant*
- When asked to **explain** why an attribute should be private, link it to **encapsulation** and **data integrity**, and refer to the case study (e.g. *"so the account balance can only be changed through `deposit()`, which validates the amount"*)
- Know the difference between **protected** and **private**: protected attributes are also available to **subclasses**
- When asked to **justify** a constant or a local variable, compare it with the alternative (a hard-coded value, or a global variable) and state the limitation of that alternative
- A constant is **not** the same as a global variable: a global variable can be changed, a constant should never be

---
layout: top-title-two-cols
color: blue-light
zoom: 0.9
class: ns-c-tight
---

::title::

# Check for Understanding

::left::

1. A `Shape` class has an attribute `colour` that its subclasses `Circle` and `Square` need to use, but other classes should not. Which access modifier should `colour` have?

2. What symbol shows a **private** attribute in a class diagram?

3. In the code below, is `discount` a local or global variable? What happens when the last line runs?

    ```python
    def apply_discount(price):
        discount = price * 0.2
        return price - discount 

    print(discount)
    ```

4. Explain one reason why a constant such as `MAX_SEATS = 40` is better than typing `40` throughout a program.

5. Explain why a `Student` class should make its `__grade` attribute private rather than public.

::right::

<!-- Answers: 1-protected, 2-minus, 3-local/NameError, 4-maintainability, 5-encapsulation -->

<v-click>

<SpeechBubble position="r" color="green-light" shape="round">

**Answers:**

1. **Protected** (`#` / `_colour`): available to the class and its subclasses only
2. **`-`** (minus sign)
3. **Local**: `discount` only exists inside `apply_discount()`, so `print(discount)` causes a `NameError`
4. If the number of seats changes, it only needs to be updated **in one place**; the name also explains what `40` means, improving **readability**
5. **Encapsulation**: the grade can only be changed through controlled methods (e.g. `set_grade()`) that **validate** the value, so invalid grades such as `150` can't be stored. This protects **data integrity**

</SpeechBubble>

</v-click>
