---
layout: cover
color: purple
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# OOP Principles

---
layout: top-title
color: purple-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# The Four Principles of OOP

::content::

Object-Oriented Programming is built on four key ideas. We'll explore each one using the same example — a program that models **animals** (a Dog and a Cat). By the end, you'll see how all four principles work together in a single program.

<br>

| Principle | One-liner |
|---|---|
| **Generalisation** | Spot what's *shared* and put it in one place |
| **Abstraction** | Use things without needing to know how they work inside |
| **Encapsulation** | Keep data protected; control how it's changed |
| **Inheritance** | Let new classes *reuse and extend* an existing class |

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Generalisation — Spotting What's Shared

::left::

### The idea

Look at a dog and a cat. They're different animals, but they share a lot:
- Both have a **name** and an **age**
- Both **eat** and **sleep**
- Both **make a sound** (even if the sound is different)

<SpeechBubble position="l" color="purple-light" shape="round">

**Generalisation** means we identify these shared features and put them into **one common class** — the `Animal` class — instead of repeating them everywhere.

</SpeechBubble>

> Think of it like a template. You write the shared stuff once, and every animal gets it automatically.

::right::

### In code

```python
# Animal is the "general" blueprint
class Animal:
    def __init__(self, name, age):
        self.name = name  # shared attribute
        self.age = age    # shared attribute

    def eat(self):        # shared method
        print(f"{self.name} is eating.")

    def sleep(self):      # shared method
        print(f"{self.name} is sleeping.")
```

`Animal` captures everything all animals have in common. We only write it once.

> We did this already with our `Person` and `Car` examples last week - we just didn't call it "generalisation" at the time. 

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Abstraction — Using Without Knowing the Details

::left::

### The idea

When you press a car's horn, you don't need to know *how* the electrical circuit works — you just press and it beeps.

<SpeechBubble position="l" color="sky-light" shape="round">

**Abstraction** means you can *use* something without knowing (or caring) how it works inside. The details are hidden away; you just interact with a simple interface.

</SpeechBubble>

In our Animal example:
- We call `animal.make_sound()` on any animal
- We don't need to know *how* the sound is produced — we just know it will happen

> The *caller* sees a simple button. The complexity is locked away inside.

::right::

### In code

```python
# From the outside, we just call make_sound()
# We don't know (or care) what's inside

class Animal:
    def make_sound(self):
        # Details hidden inside the class
        print("...")

# Using the method — simple and clean
my_animal = Animal("Generic", 3)
my_animal.make_sound()  # Just call it!
```

> This is like how we used the `csv` classes last week - we didn't need to know how they worked internally, we just used their methods.

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Encapsulation — Protecting What's Inside

::left::

### The idea

Imagine a medicine capsule. The medicine is sealed inside — you can't just reach in and change it. You only interact with it in a controlled way (swallow it).

<SpeechBubble position="l" color="orange-light" shape="round">

**Encapsulation** means keeping an object's internal data **private** and only allowing access through safe, controlled methods.

</SpeechBubble>

In our Animal example:
- `_health` is private (the `_` prefix is a signal: "don't touch this directly")
- To read it, use `get_health()`
- To change it, use `take_damage()` — which checks the value is sensible before applying it

> This prevents accidental (or bad) changes to important data.

::right::

### In code

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._health = 100  # private — don't access directly

    def get_health(self):
        return self._health  # controlled read

    def take_damage(self, amount):
        if amount > 0:           # validate before changing
            self._health -= amount
            if self._health < 0:
                self._health = 0

# Good — uses the safe method
my_animal.take_damage(10)
print(my_animal.get_health())  # 90

# Bad — bypasses encapsulation (avoid this!)
# my_animal._health = -999
```

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Inheritance — Building on What Already Exists

::left::

### The idea

A dog *is* an animal. It has everything an animal has, plus its own unique traits (it wags its tail, it barks).

<SpeechBubble position="l" color="green-light" shape="round">

**Inheritance** lets a new class (the *child*) automatically get all the attributes and methods of an existing class (the *parent*), and then add or override what it needs.

</SpeechBubble>

- `Dog` inherits `name`, `age`, `_health`, `eat()`, `sleep()`, `get_health()`, `take_damage()` — for free
- `Dog` then *overrides* `make_sound()` to bark instead of the default

> Like a child inheriting their parents' eye colour, but having their own personality on top.

::right::

### In code

```python
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # run Animal's __init__
        self.breed = breed           # Dog's own extra attribute

    def make_sound(self):            # override the parent method
        print(f"{self.name} says: Woof!")

class Cat(Animal):  # Cat also inherits from Animal
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):            # different override
        print(f"{self.name} says: Meow!")

dog = Dog("Rex", 4, "Labrador")
cat = Cat("Whiskers", 2)

dog.make_sound()   # Rex says: Woof!
cat.make_sound()   # Whiskers says: Meow!
dog.eat()          # Rex is eating.  (inherited!)
```

---
layout: top-title-two-cols
color: purple-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Putting It All Together (1/3) — The Animal Base Class

::left::

The `Animal` class demonstrates **Generalisation** and **Encapsulation** working together.

- All shared attributes (`name`, `age`, `_health`) live here — written once
- `_health` is private — only readable/changeable via controlled methods
- `make_sound()` defines the shared interface (Abstraction)

::right::

```python
# === GENERALISATION: shared blueprint for all animals ===
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._health = 100  # ENCAPSULATION: private data

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):  # ABSTRACTION: simple interface
        print("...")

    def get_health(self):          # ENCAPSULATION: controlled read
        return self._health

    def take_damage(self, amount): # ENCAPSULATION: controlled write
        if amount > 0:
            self._health = max(0, self._health - amount)
```

---
layout: top-title-two-cols
color: purple-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Putting It All Together (2/3) — Subclasses

::left::

`Dog` and `Cat` both **inherit** from `Animal` — they get everything for free and only define what's different.

- `super().__init__()` runs the parent's setup
- Each class **overrides** `make_sound()` with its own behaviour
- The caller doesn't need to know which animal it has — just call `make_sound()` (Abstraction)

::right::

```python
# === INHERITANCE: Dog and Cat reuse everything from Animal ===
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # inherit Animal's setup
        self.breed = breed           # Dog's own extra attribute

    def make_sound(self):  # ABSTRACTION: same interface, different behaviour
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):  # different override
        print(f"{self.name} says: Meow!")
```

---
layout: top-title-two-cols
color: purple-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Putting It All Together (3/3) — Using the Classes

::left::

Now we create objects and call methods. Notice:

- `dog.eat()` is **inherited** — we never wrote it in `Dog`
- `dog.take_damage()` uses **encapsulation** — no direct access to `_health`
- Both animals respond to `make_sound()` — **abstraction** in action

::right::

```python
# --- Demo ---
dog = Dog("Rex", 4, "Labrador")
cat = Cat("Whiskers", 2)

dog.make_sound()        # Rex says: Woof!
cat.make_sound()        # Whiskers says: Meow!
dog.eat()               # Rex is eating.  (inherited!)

dog.take_damage(30)
print(dog.get_health()) # 70
```

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 0.9
class: ns-c-tight
---

::title::

# Summary — The Four Principles

::left::

<SpeechBubble position="l" color="purple-light" shape="round">

### Generalisation
Extract shared features into a common class.
- **What:** `Animal` holds everything all animals share
- **Why:** Write it once, reuse everywhere
- **Metaphor:** A template form everyone fills in

</SpeechBubble>

<br>

<SpeechBubble position="l" color="sky-light" shape="round">

### Abstraction
Use things without knowing how they work inside.
- **What:** Call `make_sound()` — don't worry about the internals
- **Why:** Simpler, cleaner code for the caller
- **Metaphor:** Pressing a car horn — no electrical knowledge needed

</SpeechBubble>

::right::

<SpeechBubble position="l" color="orange-light" shape="round">

### Encapsulation
Protect internal data; control how it's accessed.
- **What:** `_health` is private; changed only via `take_damage()`
- **Why:** Prevents bad or accidental changes
- **Metaphor:** Medicine in a sealed capsule

</SpeechBubble>

<br>

<SpeechBubble position="l" color="green-light" shape="round">

### Inheritance
Build new classes on top of existing ones.
- **What:** `Dog` and `Cat` extend `Animal`
- **Why:** Reuse code, add specialisation
- **Metaphor:** A child inheriting family traits — then adding their own

</SpeechBubble>

---
layout: top-title-two-cols
color: purple-light
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Check for Understanding

::left::

**Match each scenario to the OOP principle it best demonstrates:**

1. A `BankAccount` class stores `_balance` as a private variable and only lets you change it through `deposit()` and `withdraw()` methods, and view it using `get_balance()`.

2. A `Vehicle` class captures the `speed`, `fuel` and `move()` behaviour that all vehicles share.

3. You call `payment.process()` on a payment object. You don't know whether it's BPAY, credit card or PayPal underneath — it just works.

4. A `SavingsAccount` class extends `BankAccount`, using all its methods and adding an `apply_interest()` method.

::right::

**Principles:**

- A. Abstraction
- B. Encapsulation
- C. Generalisation
- D. Inheritance

<br>

<!-- Answers: 1-B, 2-C, 3-A, 4-D -->

<v-click>

**Answers:**
1. **B. Encapsulation** (`_balance` is protected)
2. **C. Generalisation** (shared features in one class)
3. **A. Abstraction** (caller doesn't see the internals)
4. **D. Inheritance** (`SavingsAccount` extends `BankAccount`)

</v-click>

---
layout: top-title-two-cols
color: purple
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Challenge Task — Inheritance

::left::

### Context: Weather Balloons

You are building software to track scientific weather balloons.

Create a parent class called `Balloon` with shared attributes and methods:
- `id_code`
- `altitude`
- `status`
- `launch()`
- `report_status()`

Then create **two child classes**:
- `DataBalloon` (adds `sensor_type`)
- `CameraBalloon` (adds `camera_resolution`)

::right::

### Your task

1. Use **inheritance** so both child classes reuse the `Balloon` setup.
2. Override `report_status()` in each child class with a customised message.
3. Create at least **one object** of each child class.
4. Call `launch()` and `report_status()` for each object.

<SpeechBubble position="l" color="green-light" shape="round">

Use the same method name across classes (`report_status`) but show different behaviour in each child class.

</SpeechBubble>

**Extension:** Add a third child class of your choice (for example `RelayBalloon`) with one extra attribute.
