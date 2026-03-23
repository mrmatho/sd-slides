---
layout: cover
color: blue
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Reading and Writing XML Files

---
src: ./u3o1_tracking.md
hide: false
---

---
layout: top-title-two-cols
color: blue
zoom: 1.2
class: ns-c-tight
---

::title::
# Reading and Writing XML Files

::left::

**XML Files** (eXtensible Markup Language) are a widely used format for storing and transporting data. XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. XML files consist of elements, which are defined by tags, and can contain attributes and nested elements.

::right::

XML Files look like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<orders>
    <order id="1">
        <customer>Ahmed</customer>
        <item>Book</item>
        <quantity>2</quantity>
    </order>
    <order id="2">
        <customer>Bob</customer>
        <item>Pen</item>
        <quantity>5</quantity>
    </order>
    <order id="3">
        <customer>Carlotta</customer>
        <item>Notebook</item>
        <quantity>3</quantity>
    </order>
</orders>
```

---
layout: top-title-two-cols
color: blue
zoom: 1
class: ns-c-tight
---

::title::

# Reading XML Files using ElementTree

::left::

To read XML files in Python, we can use the `xml.etree.ElementTree` module, which provides a simple and efficient way to parse and navigate XML documents. The `ElementTree` class allows us to access elements and attributes in the XML structure and to iterate through the elements to extract the data we need.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<orders>
    <order id="1">
        <customer>Ahmed</customer>
        <item>Book</item>
        <quantity>2</quantity>
    </order>
    <order id="2">
        <customer>Bob</customer>
        <item>Pen</item>
        <quantity>5</quantity>
    </order>
    ... more orders ...
</orders>
```
::right::

## Implementing in Python

```python
import xml.etree.ElementTree as ET

# Create an ElementTree object by parsing the XML file
tree =  ET.parse('orders.xml')

# Get the overall (root) element of the XML document
root = tree.getroot()

# loop through each 'order' element in the XML document.
for order in root.findall('order'):
    # Print each order's customer name and item
    customer = order.find('customer').text
    item = order.find('item').text
    print(f'Customer: {customer}, Item: {item}')
```

- If we wanted all the elements (including things other than orders) we could use `root.iter()` instead of `root.findall('order')`.


