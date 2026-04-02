---
layout: cover
color: green
transition: fade
zoom: 1
hideInToc: false
class: ns-c-tight
---

# Sorting and Searching Algorithms

---
layout: top-title
color: green
transition: fade
zoom: 1.1
class: ns-c-tight
---

::title::

# Sorting and Searching Algorithms

::content::

The study design lists two sorting and two search algorithms for study:

- Searching: Linear Search, Binary Search
- Sorting: Selection Sort, Quick Sort

For each algorithm, we need to understand:
- How the algorithm works (the logic behind it)
- How efficient it is (time complexity)
- When to use it (best use cases)

---
layout: top-title
color: green
transition: fade
zoom: 1.4
class: ns-c-tight
---

::title::

# Searching and Sorting: Overview

::content::

When demonstrating the algorithms, we usually use an array of integers. This is for clarity - we can sort anything that can be compared (like strings, floats, complex data structures, files, etc.) but integers are the simplest to demonstrate. **The algorithm doesn't change, regardless of the data type.**

Similarly, we describe the collection as an **"array"** but it could be a list, a linked list, a file, or any other collection. The algorithm's logic is the sam as long as we can access and modify the elements in some way.

---
layout: top-title-two-cols
color: green
transition: fade
zoom: 0.87
class: ns-c-tight
---

::title::

# Searching Algorithms

::left::

### Linear Search

Linear search is the simplest of the algorithms we use.

- Check each item in the list one by one
- If the item matches the target, return its index in the list
- If we reach the end of the list without finding the target, return -1 (to indicate not found)

::right::

### Binary Search

Binary search is more efficient than linear search but **requires the list to be sorted.**

- Start with two pointer variables, one at the beginning of the list and one at the end. (Usually called `left` & `right` or `lo` & `hi`)
- Find the middle element of the list (`mid`)
- Compare the middle element with the target:
  - If they match, return the index of the middle element - **FOUND!**
  - If the middle element is less than the target, move the left pointer to `mid + 1` (it isn't in the left half, so ignore that)
  - If the middle element is greater than the target, move the right pointer to `mid - 1` (if it isn't in the right half, so ignore that)
- Repeat the process until the target is found or the pointers cross each other (which means the target is not in the list)

---
layout: top-title-two-cols
color: green
transition: fade
zoom: 0.9
class: ns-c-tight
---

::title::

# Sorting Algorithms

::left::

## Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the beginning (or end) of the sorted portion.

- Start with the first element of the list and assume it is the smallest.
- Compare this element with the rest of the list to find the actual smallest element.
- Swap the smallest element with the first element of the list.
- Move to the next element and repeat the process. Repeat for the remaining unsorted portion of the list until the entire list is sorted.

::right::

## Quick Sort

Quick sort is a more efficient sorting algorithm that uses a divide-and-conquer approach. It works by selecting a "pivot" element from the list and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

- Choose a pivot element from the list (commonly the last element).
- Partition the list into two sub-arrays:
  - Elements less than the pivot go to the left
  - Elements greater than the pivot go to the right
  - Apply the same process to the new sub-arrays recursively until the sub-arrays are 0 or 1 element
  - Once no more partitioning is needed, the list is sorted.

---
layout: top-title
color: green
transition: fade
zoom: 1
class: ns-c-tight
---

::title::

# Comparison of Algorithms

::content::

| Algorithm | Time Complexity | Use it when... | Don't use it when... |
|-----------|-----------------|----------------|---------------------|
| Linear Search | O(n) | The list is unsorted or small | The list is large and sorted |
| Binary Search | O(log n) | The list is sorted and large | The list is unsorted or small |
| Selection Sort | O(n^2) | The list is small and simplicity is more important than efficiency | The list is large or efficiency is important |
| Quick Sort | O(n log n) on average, O(n^2) worst case | The list is large and efficiency is important | The list is small or already mostly sorted (because of the worst-case scenario) |

---
