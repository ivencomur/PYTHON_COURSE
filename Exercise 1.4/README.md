# Exercise 1.4 – File Handling in Python

**Course:** CareerFoundry – Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.4, which introduces file handling and error management in Python. The exercise builds upon the recipe management concepts from Exercise 1.3 by adding data persistence through binary file storage. This is accomplished through two complementary programs: one for storing recipes and another for retrieving and searching them.

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

- Implement file handling using Python's built-in `open()` function
- Understand the difference between text files and binary files
- Use the `pickle` module to serialize and deserialize complex data structures
- Implement robust error handling with try-except-else-finally blocks
- Handle specific exceptions: FileNotFoundError, ValueError, IndexError
- Create programs that communicate through shared data files
- Build user-friendly applications that handle errors gracefully
- Navigate file system directories using the `os` module
- Understand data persistence and its role in application development

---

## Project Structure
Exercise-1.4/
│
├── README.md                    # This documentation
├── recipe_input.py              # Recipe collection and storage program
├── recipe_search.py             # Recipe retrieval and search program
├── recipes.bin                  # Binary data file (generated)
├── LEARNING_JOURNAL4.html       # Detailed learning reflections
│
└── screenshots/
├── 01_code_recipe_creation.png
├── 02_Import_Pickle_and_calc_difficulty.png
├── 03_take_recipe_function.png
├── 04_build_main_code_A.png
├── 05_collecting_recipes.png
├── 06_Saving_data_to_file.png
├── 07_Full_code-screenshot.png
├── 08_Test_recipe.png
├── 09_Create_Recipe_search_Import_Pickle.png
├── 10_Create_Display_Recipe_Function.png
├── 11_Search_Ingredient_Function.png
├── 12_Bring_Main_Code_Into_Search.png
├── 13_Complete_Recipe_Search_Code.png
├── 14_Testing_Recipe_Search.png
└── 15_Full_Search_Code.png

---

## Implementation Guide

### Part 1: recipe_input.py

#### Step 1: Import Pickle and Define Helper Functions
```python
import pickle

def calc_difficulty(cooking_time, ingredients):
    """Calculate recipe difficulty based on time and ingredient count"""
    if cooking_time < 10 and len(ingredients) < 4:
        return 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
        return 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
        return 'Intermediate'
    else:
        return 'Hard'
This function encapsulates the difficulty calculation logic from Exercise 1.3, making it reusable and maintainable.

Step 2: Create Recipe Collection Function
pythondef take_recipe():
    """Collect recipe information from user and return as dictionary"""
    name = input("Enter recipe name: ").strip()
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients_input = input("Enter ingredients (separated by commas): ").strip()
    
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe
Key difference from Exercise 1.3: The difficulty is now calculated and stored immediately within the recipe dictionary, ensuring it's preserved when saved to file.

Step 3: Implement File Loading with Error Handling
pythonfilename = input("Enter the filename to store recipes (e.g., 'recipes.bin'): ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    
except FileNotFoundError:
    print("File not found. Creating a new recipe file.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
except:
    print("An unexpected error occurred. Creating new data.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
else:
    file.close()
    
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
Error handling flow:

try: Attempt to open and load existing file
except FileNotFoundError: Handle missing file scenario
except: Catch any other unexpected errors
else: Close file only if successfully opened
finally: Extract data regardless of what happened above


Step 4: Collect and Process Recipes
pythonn = int(input("\nHow many recipes would you like to enter? "))

for i in range(n):
    print(f"\n--- Recipe {i + 1} ---")
    recipe = take_recipe()
    
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)

print("\nAll recipes collected successfully!")
This loop mirrors Exercise 1.3's collection logic while building the master ingredient list.

Step 5: Save Data to Binary File
pythondata = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

file = open(filename, 'wb')
pickle.dump(data, file)
file.close()

print(f"\nRecipes saved successfully to {filename}!")
Pickle workflow:

Package data into dictionary
Open file in write-binary mode ('wb')
Use pickle.dump() to serialize and write data
Close file to ensure data is saved


Part 2: recipe_search.py
Step 1: Create Display Function
pythonimport pickle

def display_recipe(recipe):
    """Display a single recipe with all its details"""
    print("\n" + "="*50)
    print(f"Recipe: {recipe['name']}")
    print("="*50)
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    print("="*50)
This function provides consistent, readable recipe output formatting.

Step 2: Implement Search Function with Error Handling
pythondef search_ingredient(data):
    """Search for recipes by ingredient"""
    all_ingredients = data['all_ingredients']
    
    print("\nAvailable ingredients:")
    print("-" * 30)
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    print("-" * 30)
    
    try:
        choice = int(input("\nEnter the number of the ingredient you want to search for: "))
        ingredient_searched = all_ingredients[choice]
        
    except ValueError:
        print("Error: Please enter a valid number.")
        return
        
    except IndexError:
        print("Error: That number is not in the list.")
        return
        
    except:
        print("An unexpected error occurred.")
        return
        
    else:
        print(f"\nRecipes containing '{ingredient_searched}':")
        print("=" * 50)
        
        found_recipes = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found_recipes = True
        
        if not found_recipes:
            print(f"No recipes found with {ingredient_searched}.")
enumerate() usage: Provides both index number and ingredient name, allowing users to select by number rather than typing ingredient names.

Step 3: Implement Main Program Logic
pythonfilename = input("Enter the filename where your recipes are stored: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
    
except FileNotFoundError:
    print(f"Error: File '{filename}' not found. Make sure you've run recipe_input.py first!")
    
except:
    print("An unexpected error occurred while trying to read the file.")
    
else:
    file.close()
    search_ingredient(data)
This structure ensures the file is only read if it exists and is properly formatted.

Program Features
recipe_input.py Features

Loads existing recipe data or creates new data structure
Collects multiple recipes from user input
Calculates and stores recipe difficulty
Maintains master list of unique ingredients
Saves all data to binary file using pickle
Handles missing files gracefully

recipe_search.py Features

Loads recipe data from binary file
Displays numbered list of available ingredients
Allows user to search by ingredient number
Shows all recipes containing selected ingredient
Handles user input errors (invalid numbers, out-of-range values)
Provides helpful error messages


Code Structure
recipe_input.py Components
Imports:

pickle - For data serialization

Functions:

calc_difficulty(cooking_time, ingredients) - Returns difficulty level
take_recipe() - Collects and returns recipe dictionary

Main Logic:

File loading with try-except-else-finally
Recipe collection loop
Ingredient aggregation
Data serialization and file writing


recipe_search.py Components
Imports:

pickle - For data deserialization

Functions:

display_recipe(recipe) - Formats and displays single recipe
search_ingredient(data) - Handles ingredient search with error handling

Main Logic:

File loading with try-except-else
Call to search function if loading successful


Key Concepts
Binary Files vs Text Files
Text Files:

Human-readable format
Store simple string data
Examples: .txt, .csv, .json

Binary Files:

Machine-readable format
Store complex data structures
More efficient for Python objects
Examples: .bin, .pkl, .dat


The Pickle Module
Pickle serializes (converts) Python objects into byte streams that can be saved to files and later deserialized (converted back) to their original form.
Advantages:

Preserves complex data structures (dictionaries, lists, nested objects)
Maintains data types (no need to parse strings back to integers)
Simple API (dump() and load())

Limitations:

Binary format is not human-readable
Pickle files are Python-specific (not cross-language compatible)
Security concern: Only unpickle data from trusted sources


Error Handling Flow
pythontry:
    # Code that might raise an exception
except SpecificError:
    # Handle specific error type
except AnotherError:
    # Handle another specific error type
except:
    # Catch any other errors
else:
    # Runs only if try block succeeded
finally:
    # Always runs, regardless of errors
When to use each block:

try: Always required - contains risky code
except: Handle known failure scenarios
else: Clean-up operations that shouldn't run if errors occurred
finally: Operations that must run regardless (like extracting data)


Common Exception Types
FileNotFoundError:

Raised when attempting to open a non-existent file
Solution: Create new file or prompt user for correct filename

ValueError:

Raised when function receives correct type but inappropriate value
Example: int("hello") - string can't be converted to integer
Solution: Validate input or use try-except

IndexError:

Raised when accessing list index that doesn't exist
Example: my_list[99] when list has only 10 items
Solution: Check list length or use try-except


The enumerate() Function
enumerate() returns both index and value when iterating:
pythoningredients = ['Eggs', 'Milk', 'Cheese']

for index, ingredient in enumerate(ingredients):
    print(f"{index}: {ingredient}")

# Output:
# 0: Eggs
# 1: Milk
# 2: Cheese
This allows users to select items by number rather than typing exact names.

Technical Challenges
Indentation Errors
Problem: Function definitions were indented incorrectly, causing Python to interpret nested functions unintentionally.
Cause: Inconsistent spacing - some lines had 4 spaces, others had different amounts.
Solution: Ensured all function definitions (def statements) start at the left margin with zero indentation. Code inside functions uses exactly 4 spaces.
Lesson: Python's significant whitespace requires precise, consistent indentation throughout entire files.

Directory Navigation Issues
Problem: "File not found" error despite file existing in project folder.
Cause: Terminal working directory didn't match file location.
Solution: Used cd "Exercise 1.4" to navigate into correct directory before running programs.
Lesson: Python looks for files relative to current working directory. Always verify location with pwd and ls commands.

Understanding try-except-else-finally Flow
Challenge: Confusion about when each block executes and in what order.
Solution: Learned the execution flow:

try always executes first
If error occurs, jump to matching except
If no errors, else executes
finally always executes last, regardless of errors

Practical application: Use else for operations that should only run on success (like closing files). Use finally for operations that must always run (like extracting data).

Markdown Artifacts in Python Files
Problem: Syntax errors from ```python code fence markers appearing in Python file.
Cause: Accidentally copied markdown formatting when pasting code examples.
Solution: Removed all markdown syntax. Python files should contain only Python code and comments.
Lesson: Be careful when copying code from formatted documents - remove any non-code formatting.

Testing
Test Data Used
Recipe 1: Tea

Cooking time: 5 minutes
Ingredients: Tea Leaves, Sugar, Water
Expected difficulty: Easy
Test result: ✓ Saved and retrieved correctly

Recipe 2: Omelette

Cooking time: 15 minutes
Ingredients: Eggs, Milk, Cheese, Onions
Expected difficulty: Hard
Test result: ✓ Found when searching for "Eggs"

Recipe 3: Pasta

Cooking time: 12 minutes
Ingredients: Pasta, Tomatoes, Salt
Expected difficulty: Intermediate
Test result: ✓ Found when searching for "Pasta"


Error Handling Tests
Test 1: Wrong filename (recipe_input.py)

Input: Non-existent file
Expected: Create new data structure
Result: ✓ Program created new file

Test 2: Invalid ingredient number (recipe_search.py)

Input: "hello" instead of number
Expected: ValueError caught, helpful message displayed
Result: ✓ "Error: Please enter a valid number."

Test 3: Out-of-range number (recipe_search.py)

Input: 999 when only 10 ingredients exist
Expected: IndexError caught, helpful message displayed
Result: ✓ "Error: That number is not in the list."


Verification Points

Binary file created successfully after first run
Subsequent runs load existing data correctly
Ingredient list contains no duplicates
Search finds all matching recipes
No recipes displayed when ingredient not found
Programs handle all error scenarios gracefully


Deliverables

✅ recipe_input.py - Functional recipe storage program
✅ recipe_search.py - Functional recipe search program
✅ recipes.bin - Binary data file with test recipes
✅ 15 screenshots documenting complete development process
✅ LEARNING_JOURNAL4.html - Comprehensive learning documentation
✅ README4.md - Technical documentation (this file)
✅ Updated index.html with Exercise 1.4 link
✅ Updated GitHub repository with organized structure


AI Assistance Declaration
This exercise was completed through a guided, step-by-step tutorial approach with AI assistance. Given the complexity of file handling and error management concepts, AI was used as an interactive learning partner to understand and implement the requirements.
Technical Problem-Solving

Structured learning path: AI provided a checkpoint-based tutorial that broke down complex concepts (pickle, binary files, try-except blocks) into digestible steps with verification at each stage
Indentation debugging: When indentation errors occurred (similar to Exercise 1.3), AI helped identify exactly where spacing was incorrect and explained why it mattered
Error handling concepts: AI explained the flow of try-except-else-finally blocks with clear examples and student-friendly terminology
Directory navigation: When "file not found" errors appeared, AI helped troubleshoot that the working directory was incorrect and how to navigate properly
Code review: AI caught markdown formatting accidentally copied into Python files and other syntax issues before they became larger problems
Concept clarification: AI rephrased technical concepts using plain language when formal explanations were confusing

Learning Context
This exercise was completed using AI as an interactive tutor, stopping at checkpoints to confirm understanding before proceeding. All code was typed, tested, and debugged directly. When errors occurred (indentation issues, file path problems), solutions were implemented hands-on with AI providing guidance on what to look for and why errors happened. This checkpoint-based approach ensured comprehension of each concept before building upon it.
Implementation Approach
The guided tutorial approach with AI allowed progressive understanding of interconnected concepts (binary files, pickles, multiple exception types, file modes) while maintaining independent troubleshooting ability. This mirrors how developers learn new frameworks or tools - through structured tutorials with checkpoints and hands-on practice. All actual coding, testing, file creation, and debugging was performed directly, with AI serving as an interactive reference similar to technical documentation or programming forums.
What Was Done Independently

Typed all code manually (no copy-paste of complete solutions)
Fixed indentation errors by understanding Python's spacing rules
Debugged file path issues by learning terminal navigation
Tested both programs with sample data and error scenarios
Organized files and screenshots for submission
Created comprehensive learning journal and documentation


Resources
Python Documentation

Python 3.9 Official Documentation
File Handling
Pickle Module
Errors and Exceptions
os Module

Learning Resources

Real Python - Reading and Writing Files
Real Python - Python Pickle Module
Real Python - Python Exceptions


Summary
Exercise 1.4 introduced the critical concept of data persistence - the ability to save program data permanently and retrieve it later. This transforms the recipe management program from a one-time execution tool into a practical application capable of building a recipe collection over time.
The exercise demonstrated how file handling and error management work together to create robust, user-friendly applications. By implementing try-except blocks, the programs handle errors gracefully rather than crashing, providing helpful feedback to guide users toward successful interactions.
The combination of pickle serialization and binary file storage provides a straightforward approach to persisting complex Python data structures. While databases will eventually replace this approach in production applications, understanding file-based persistence establishes foundational concepts applicable to all data storage mechanisms.
This exercise completes the core Python fundamentals needed for the Achievement 1 final task: variables and data types (1.1), data structures (1.2), control flow (1.3), and now file handling and error management (1.4). These skills form the foundation for building complete, production-ready applications.

Repository: [https://github.com/ivencomur/PYTHON_COURSE]
Contact: Ivan Cortes
Previous: Exercise 1.3 | Next: Achievement 1 Final Task

Documentation created to support future learners understanding file handling and error management in Python.