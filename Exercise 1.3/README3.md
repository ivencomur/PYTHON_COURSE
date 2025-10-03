# Exercise 1.3 — Operators & Functions in Python

**Course:** CareerFoundry — Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.3, which introduces core programming concepts: conditional statements, loops, and functions. The exercise culminates in building a functional recipe management program that collects user input, processes data, calculates recipe difficulty, and displays formatted output.

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Implementation Guide](#implementation-guide)
- [Program Features](#program-features)
- [Code Structure](#code-structure)
- [Key Concepts](#key-concepts)
- [Technical Challenges](#technical-challenges)
- [Testing](#testing)
- [Deliverables](#deliverables)
- [AI Assistance Declaration](#ai-assistance-declaration)
- [Resources](#resources)

---

## Learning Objectives

- Transition from interactive shell to script file development
- Implement conditional logic using if/elif/else statements
- Use comparison and boolean operators for decision-making
- Create and utilize for and while loops for iteration
- Write reusable functions with parameters and return values
- Understand variable scope (local vs. global)
- Process user input with string manipulation methods
- Calculate derived attributes from existing data
- Format output for user-friendly display

---

## Project Structure

```
Exercise-1.3/
│
├── README.md                    # This documentation
├── Exercise_1.3.py              # Main recipe management program
├── LEARNING_JOURNAL3.html       # Detailed learning reflections
│
└── screenshots/
    ├── Step1-Initial-Lists.png
    ├── Step2-Take-Recipe-Function.png
    ├── Step3-N-Input.png
    ├── Step4-Collection-Loop.png
    ├── Step5-Display-Difficulty.png
    ├── Step6-Complete-Code.png
    └── Step7-Terminal-Output.png
```

---

## Implementation Guide

### Step 1: Initialize Global Data Storage

Two empty lists are created at the module level to store program data:

```python
recipes_list = []        # Stores all recipe dictionaries
ingredients_list = []    # Tracks all unique ingredients
```

These global variables are accessible throughout the program, allowing data persistence across function calls.

---

### Step 2: Define Recipe Input Function

The `take_recipe()` function encapsulates the logic for collecting recipe information:

```python
def take_recipe():
    name = input("Enter the recipe name: ").strip()
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients (separated by commas): ").strip().split(',')
    
    ingredients = [ingredient.strip() for ingredient in ingredients]
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe
```

**Key techniques:**
- `.strip()` removes leading/trailing whitespace
- `.split(',')` converts comma-separated string to list
- List comprehension cleans each ingredient
- Dictionary structure organizes related data
- `return` statement provides output to caller

---

### Step 3: Collect Multiple Recipes

The main program loop collects n recipes from the user:

```python
n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    print(f"Recipe {i + 1}:")
    recipe = take_recipe()
    
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)
```

**Loop structure:**
- Outer loop: Iterates n times (once per recipe)
- Inner loop: Checks each ingredient in current recipe
- Membership test: `not in` prevents duplicates
- Data accumulation: Builds lists incrementally

---

### Step 4: Calculate and Display Difficulty

Difficulty is determined by cooking time and ingredient count:

```python
for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {difficulty}")
```

**Logic breakdown:**
- **Easy:** Quick (<10 min) AND simple (<4 ingredients)
- **Medium:** Quick (<10 min) AND complex (≥4 ingredients)
- **Intermediate:** Slow (≥10 min) AND simple (<4 ingredients)
- **Hard:** Slow (≥10 min) AND complex (≥4 ingredients)

---

### Step 5: Display All Ingredients

```python
ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)
```

The `.sort()` method arranges ingredients alphabetically for easy reference.

---

## Program Features

### User Input Processing
- Collects recipe name, cooking time, and ingredients
- Handles comma-separated ingredient lists
- Cleans whitespace from all inputs
- Validates cooking time as integer

### Data Management
- Stores recipes as dictionaries for clear structure
- Maintains master list of unique ingredients
- Prevents duplicate ingredients across recipes
- Supports any number of recipes

### Difficulty Calculation
- Evaluates cooking time and ingredient count
- Assigns appropriate difficulty level
- Uses compound boolean expressions
- Covers all possible combinations

### Output Formatting
- Displays recipes with clear labels
- Shows ingredients as comma-separated list
- Includes calculated difficulty level
- Alphabetizes ingredient master list

---

## Code Structure

### Global Variables
Variables declared at module level, accessible everywhere:
- `recipes_list`: Collection of all recipe dictionaries
- `ingredients_list`: Running list of unique ingredients

### Functions
Reusable code blocks with defined purposes:
- `take_recipe()`: Collects and returns one recipe dictionary

### Main Program Logic
Sequential execution flow:
1. Ask for number of recipes
2. Loop to collect recipes
3. Loop to display recipes with difficulty
4. Display sorted ingredients

---

## Key Concepts

### Conditional Statements
- `if` checks first condition
- `elif` checks additional conditions if previous failed
- `else` handles all remaining cases
- Indentation defines code blocks

### Loops
- `for` iterates specific number of times or through sequences
- `while` continues until condition becomes false
- `range()` generates numeric sequences
- Nested loops process hierarchical data

### Functions
- `def` defines function
- Parameters receive input values
- `return` sends output back to caller
- Local variables exist only within function
- DRY principle: Don't Repeat Yourself

### String Methods
- `.strip()`: Remove whitespace
- `.split()`: Break string into list
- `.join()`: Combine list into string
- f-strings: Format strings with variables

### List Operations
- `.append()`: Add item to end
- `.sort()`: Arrange alphabetically
- `in`: Check membership
- `len()`: Get item count

---

## Technical Challenges

### Indentation Error
**Problem:** Program asked for recipe count but didn't prompt for details.

**Cause:** Inconsistent indentation (5 spaces instead of 4) broke code block structure.

**Solution:** Ensured all indentation used exactly 4 spaces throughout file.

**Lesson:** Python requires precise, consistent indentation to define code blocks.

---

### Understanding Nested Loops
**Challenge:** Tracking which loop controlled which code block.

**Solution:** Used descriptive variable names (`recipe` vs `ingredient`) and visualized execution: outer loop runs once, inner loop completes all iterations, then outer loop continues.

---

### List Membership Testing
**Challenge:** Checking if ingredient already exists before adding.

**Solution:** Used `if ingredient not in ingredients_list` pattern. The `in` operator efficiently searches entire list and returns boolean result.

---

## Testing

### Test Data Used

**Recipe 1: Tea**
- Cooking time: 5 minutes
- Ingredients: Tea Leaves, Sugar, Water
- Expected difficulty: Easy

**Recipe 2: Omelette**
- Cooking time: 15 minutes
- Ingredients: Eggs, Milk, Cheese, Onions
- Expected difficulty: Hard

**Recipe 3: Pasta**
- Cooking time: 12 minutes
- Ingredients: Pasta, Tomatoes, Salt
- Expected difficulty: Intermediate

### Verification Points
- Function returns correct dictionary structure
- Duplicate ingredients not added to master list
- Difficulty calculation matches all four conditions
- Ingredient list displays alphabetically
- Program handles any number of recipes

---

## Deliverables

- ✅ `Exercise_1.3.py` - Functional recipe management program
- ✅ Seven screenshots documenting development process
- ✅ `LEARNING_JOURNAL3.html` - Comprehensive learning documentation
- ✅ `README3.md` - Technical documentation (this file)
- ✅ Updated GitHub repository with organized structure

---

## AI Assistance Declaration

This exercise was completed through independent, self-directed learning. AI assistance was utilized to resolve technical challenges related to:

### Technical Problem-Solving
- **Version compatibility issues:** Ensuring code examples worked with current Python 3.9.x syntax and conventions
- **Deprecated syntax resolution:** Updating outdated code patterns to current Python best practices
- **Error debugging:** Understanding Python error messages and indentation requirements
- **Alternative approaches:** Learning multiple valid solutions when original examples didn't execute correctly

### Learning Context
This exercise was completed independently due to working asynchronously with limited mentor availability. AI tools served as a reference for clarifying Python syntax, debugging code errors, and validating solutions against current language standards. All code was written, tested, and debugged hands-on through iterative problem-solving.

### Implementation Approach
All solutions underwent direct testing and validation. Core logic, program structure, and problem-solving approaches remained under complete learner control. AI assistance accelerated the learning process by providing immediate feedback on syntax errors and suggesting current best practices when course materials referenced older Python versions.

---

## Resources

### Python Documentation
- [Python 3.9 Official Documentation](https://docs.python.org/3.9/)
- [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

### Learning Resources
- [Real Python - Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Real Python - For Loops](https://realpython.com/python-for-loop/)
- [Real Python - Functions](https://realpython.com/defining-your-own-python-function/)

---

## Summary

Exercise 1.3 introduced fundamental programming concepts that form the foundation of application development. The recipe management program demonstrates how combining simple concepts—functions, loops, and conditionals—creates functional, useful applications. These skills transfer directly to larger projects including web applications, data processing, and automation scripts.

The transition from shell-based experimentation to script file development represents a significant milestone in Python proficiency. Understanding control flow, data manipulation, and code organization provides the tools necessary for building increasingly complex programs.

---

**Repository:** [GitHub Link]  
**Contact:** Ivan Cortes  
**Previous:** Exercise 1.2 | **Next:** Exercise 1.4

---

*Documentation created to support future learners navigating Python fundamentals.*