---
layout: cover
color: red
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Streamlit GUI Basics

---
layout: top-title
color: red
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

# Streamlit GUI - Getting Started

::content::

**Streamlit** is a Python library for "rapid application development". We are using it for GUI components of the SAC, because it creates user interfaces the simplest and quickest possible. Later we will also look at the CustomTKinter library which is more powerful but also more complex to use.

Streamlit is not built into Python, so we need to install it. To do this we use pip (or uv pip) to install the library. You can do this in your terminal with the following command:

```bash
pip install streamlit
or
uv pip install streamlit
```

Some of you have already done this, but should update to the latest version by running:

```bash
pip install --upgrade streamlit
or 
uv pip install --upgrade streamlit
```

---
layout: top-title-two-cols
color: red
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

# Streamlit GUI - Running your first Streamlit app

::left::

Streamlit by convention is imported as `st` and all Streamlit functions are accessed through this alias. To create a Streamlit app, you need to write a Python script that uses Streamlit functions to define the layout and behavior of your app.

```python
import streamlit as st
st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")
``` 

**Note:** We are already adding some style to our app by using the `st.title()` function to create a title and the `st.write()` function to add some text. 


::right::

To run a Streamlit app, you need to have created and saved a Python file (e.g. `app.py`). Once you have your code ready, you can run the app using the following command in your terminal:

```bash
streamlit run app.py
```

---
layout: top-title
color: green
transition: fade
zoom: 1.4
class: ns-c-tight
---

::title::

# Streamlit GUI - Simple Interactivity

::content::

Streamlit allows you to easily add interactivity to your app using widgets. For example, you can add a button that changes the text when clicked:

```python

import streamlit as st

st.title("Interactive Streamlit App")

if st.button("Click me!"):
    st.write("Button clicked!")
else:
    st.write("Button not clicked yet.")
```

**Note:** `st.button()` has two functions. It creates the button in the app, and it returns the state of the button (True if clicked, False if not). 

