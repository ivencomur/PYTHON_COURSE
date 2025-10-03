Exercise 1.2 — Data Structures in Python
Course: CareerFoundry — Python for Web Developers (Full-Stack)

Author: Ivan Cortes

Date: October 2025

Overview
This document provides a complete walkthrough of Exercise 1.2. The exercise focuses on using Python's fundamental data structures—specifically dictionaries and lists—to model and store data for a recipe application. The primary goal is to make informed decisions about which data structure is appropriate for a given task and to practice manipulating nested data.

Table of Contents
Learning Objectives

Project Structure

Implementation Steps

Data Structure Justification

Recipes Created

Key Concepts

Deliverables

Summary

Learning Objectives
Understand the properties and use cases for Python dictionaries.

Understand the properties and use cases for Python lists.

Model real-world objects (recipes) using a combination of data structures.

Create and manipulate nested data structures (a list of dictionaries).

Justify design decisions when choosing between different data types.

Utilize the IPython interactive shell for rapid prototyping and testing.

Project Structure
This exercise is self-contained within the Exercise 1.2 directory. All work was performed within the IPython shell, with documentation and screenshots as the primary deliverables.

Exercise-1.2/
│
├── README.md # This documentation
└── screenshots/
├── 01-recipe-dict.png
├── 02-all-recipes-list.png
└── 03-nested-access.png

Implementation Steps
Activate Environment: The cf-python-base virtual environment was activated to ensure a consistent workspace.

Launch IPython: The IPython interactive shell was launched to begin coding.

Create First Recipe: A dictionary named recipe_1 was created to store the first recipe's name, cooking_time, and ingredients.

Create Recipe Container: An empty list named all_recipes was initialized to hold all recipe dictionaries.

Add More Recipes: Four additional recipes were created as dictionaries and appended to the all_recipes list.

Access Nested Data: Practiced accessing the ingredients list from specific recipes within the all_recipes list to confirm the data structure was working correctly.

Document and Submit: The design decisions were documented in this README, a learning journal was created, and screenshots were captured to evidence the work.

Data Structure Justification
Recipe Structure: Dictionary
A dictionary was chosen to store individual recipes because it provides a clear, self-documenting structure through its key-value pairs.

Readability: Accessing data with recipe['name'] is more explicit than recipe[0].

Flexibility: Dictionaries allow values of mixed types (strings, integers, lists), which is perfect for representing a recipe's diverse attributes.

Extensibility: New attributes like difficulty or servings can be easily added later without breaking the existing structure.

Recipe Collection: List
A list was chosen to store the collection of all recipes because it is an ordered and mutable data type.

Mutability: The app will need to add, and potentially remove, recipes, making a mutable list essential.

Ordering: Lists maintain the insertion order, which can be useful for displaying recipes chronologically.

Iteration: Lists are simple to iterate over, which is a common requirement for displaying all recipes.

Recipes Created
Tea — 5 min — Tea Leaves, Sugar, Water

Coffee — 5 min — Coffee Powder, Sugar, Water

Pasta — 15 min — Pasta, Tomato Sauce, Cheese

Scrambled Eggs — 10 min — Eggs, Milk, Butter, Salt

Oatmeal — 7 min — Oats, Milk, Honey, Berries

Key Concepts
The core concept of this exercise is data modeling—the process of translating real-world requirements into a programmatic structure. The list of dictionaries pattern is a fundamental concept in software development, commonly used for representing collections of objects, such as a list of users, products, or in this case, recipes.

Deliverables
[x] all_recipes list created successfully in an IPython session.

[x] README.md (this file) documenting the data structure justification.

[x] A comprehensive Learning Journal detailing the process and insights.

[x] Screenshots evidencing each step of the process.

[x] GitHub repository updated with the new folder structure and deliverables.

Summary
This exercise provided a practical foundation in Python's core data structures. By modeling a real-world object, I gained a deeper understanding of not just how to use lists and dictionaries, but why one is chosen over the other based on the specific needs of the application. This foundational skill is critical for building more complex applications.
