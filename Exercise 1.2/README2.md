# Exercise 1.2 — Data Structures in Python

**Course:** CareerFoundry — Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.2. The exercise focuses on using Python's fundamental data structures—specifically dictionaries and lists—to model and store data for a recipe application. The primary goal is to make informed decisions about which data structure is appropriate for a given task and to practice manipulating nested data.

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Implementation Steps](#implementation-steps)
- [Data Structure Justification](#data-structure-justification)
- [Recipes Created](#recipes-created)
- [Key Concepts](#key-concepts)
- [Deliverables](#deliverables)
- [AI Assistance Declaration](#ai-assistance-declaration)
- [Resources](#resources)
- [Summary](#summary)

---

## Learning Objectives

- Understand the properties and use cases for Python dictionaries
- Understand the properties and use cases for Python lists
- Model real-world objects (recipes) using a combination of data structures
- Create and manipulate nested data structures (a list of dictionaries)
- Justify design decisions when choosing between different data types
- Utilize the IPython interactive shell for rapid prototyping and testing

---

## Project Structure

This exercise is self-contained within the Exercise 1.2 directory. All work was performed within the IPython shell, with documentation and screenshots as the primary deliverables.

```
Exercise-1.2/
│
├── README.md                    # This documentation
├── LEARNING_JOURNAL2.html       # Learning reflections
│
└── screenshots/
    ├── 01-recipe-dict.png
    ├── 02-all-recipes-list.png
    └── 03-nested-access.png
```

---

## Implementation Steps

1. **Activate Environment:** The `cf-python-base` virtual environment was activated to ensure a consistent workspace.

2. **Launch IPython:** The IPython interactive shell was launched to begin coding.

3. **Create First Recipe:** A dictionary named `recipe_1` was created to store the first recipe's name, cooking_time, and ingredients.

4. **Create Recipe Container:** An empty list named `all_recipes` was initialized to hold all recipe dictionaries.

5. **Add More Recipes:** Four additional recipes were created as dictionaries and appended to the `all_recipes` list.

6. **Access Nested Data:** Practiced accessing the ingredients list from specific recipes within the `all_recipes` list to confirm the data structure was working correctly.

7. **Document and Submit:** The design decisions were documented in this README, a learning journal was created, and screenshots were captured to evidence the work.

---

## Data Structure Justification

### Recipe Structure: Dictionary

A dictionary was chosen to store individual recipes because it provides a clear, self-documenting structure through its key-value pairs.

**Advantages:**
- **Readability:** Accessing data with `recipe['name']` is more explicit than `recipe[0]`
- **Flexibility:** Dictionaries allow values of mixed types (strings, integers, lists), which is perfect for representing a recipe's diverse attributes
- **Extensibility:** New attributes like `difficulty` or `servings` can be easily added later without breaking the existing structure

**Example:**
```python
recipe_1 = {
    'name': 'Tea',
    'cooking_time': 5,
    'ingredients': ['Tea Leaves', 'Sugar', 'Water']
}
```

---

### Recipe Collection: List

A list was chosen to store the collection of all recipes because it is an ordered and mutable data type.

**Advantages:**
- **Mutability:** The app will need to add, and potentially remove, recipes, making a mutable list essential
- **Ordering:** Lists maintain the insertion order, which can be useful for displaying recipes chronologically
- **Iteration:** Lists are simple to iterate over, which is a common requirement for displaying all recipes

**Example:**
```python
all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]
```

---

### Alternative Considerations

**Why Not Tuples for Recipes?**
- Tuples are immutable, meaning they cannot be modified after creation
- Recipe data may need to be updated (e.g., correcting cooking times, adding ingredients)
- Immutability would require creating new tuple objects for any modifications

**Why Not a Dictionary for the Recipe Collection?**
- Dictionaries require unique keys for each entry
- Recipes don't have natural unique identifiers at this stage
- Lists provide simpler access via numeric indices for this use case

---

## Recipes Created

1. **Tea** — 5 min — Tea Leaves, Sugar, Water
2. **Coffee** — 5 min — Coffee Powder, Sugar, Water
3. **Pasta** — 15 min — Pasta, Tomato Sauce, Cheese
4. **Scrambled Eggs** — 10 min — Eggs, Milk, Butter, Salt
5. **Oatmeal** — 7 min — Oats, Milk, Honey, Berries

---

## Key Concepts

### Data Modeling

The core concept of this exercise is **data modeling**—the process of translating real-world requirements into a programmatic structure. The list of dictionaries pattern is a fundamental concept in software development, commonly used for representing collections of objects, such as:

- A list of users in an application
- A collection of products in an e-commerce system
- Multiple recipes in a cooking app

### Nested Data Structures

Accessing nested data requires understanding multiple levels of data structure:

```python
# Access the name of the first recipe
all_recipes[0]['name']  # Returns: 'Tea'

# Access the ingredients of the third recipe
all_recipes[2]['ingredients']  # Returns: ['Pasta', 'Tomato Sauce', 'Cheese']

# Access the second ingredient of the first recipe
all_recipes[0]['ingredients'][1]  # Returns: 'Sugar'
```

### IPython Interactive Development

IPython provides several advantages for exploratory programming:

- Immediate feedback on code execution
- Built-in help and documentation (`?` and `??` operators)
- Command history and tab completion
- Easy testing of code snippets before committing to scripts

---

## Deliverables

- ✅ `all_recipes` list created successfully in an IPython session
- ✅ `README.md` (this file) documenting the data structure justification
- ✅ `LEARNING_JOURNAL2.html` detailing the process and insights
- ✅ Screenshots evidencing each step of the process
- ✅ GitHub repository updated with the new folder structure and deliverables

---

## AI Assistance Declaration

This exercise was completed through independent, self-directed learning. AI assistance was utilized to resolve technical challenges related to:

### Technical Problem-Solving
- **Syntax verification:** Confirming correct Python dictionary and list syntax for current Python 3.9.x standards
- **Data structure selection:** Validating the choice of dictionaries vs tuples vs lists for different use cases
- **Nested data access:** Understanding the correct syntax for accessing elements in nested structures
- **Best practices:** Learning current conventions for structuring and naming data in Python

### Learning Context
This exercise was completed independently while working asynchronously through the course. AI tools served as a technical reference for validating syntax and data structure choices, similar to consulting official Python documentation or programming references when uncertain about implementation details.

### Implementation Approach
All data structures were created and tested hands-on in the IPython shell. Design decisions for choosing dictionaries and lists were made based on understanding of data structure properties and project requirements. AI assistance confirmed that chosen approaches aligned with current Python best practices, but all code implementation and testing was performed directly.

---

## Resources

### Python Documentation
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Learning Resources
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)
- [Real Python - Lists and Tuples](https://realpython.com/python-lists-tuples/)

---

## Summary

This exercise provided a practical foundation in Python's core data structures. By modeling a real-world object (recipes), the exercise demonstrated not just how to use lists and dictionaries, but why one is chosen over the other based on the specific needs of the application. This foundational skill—choosing the right data structure for the task—is critical for building more complex applications and understanding how data should be organized and accessed efficiently.

The list of dictionaries pattern used here will recur throughout the Recipe App project and is a common paradigm in data-driven applications across web development, data analysis, and software engineering.

---

**Repository:** [GitHub Link]  
**Contact:** Ivan Cortes  
**Previous:** Exercise 1.1 | **Next:** Exercise 1.3

---

*Documentation created to support future learners understanding Python data structures.*