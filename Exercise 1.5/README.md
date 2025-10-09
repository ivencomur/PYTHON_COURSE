# Exercise 1.5 – Object-Oriented Programming in Python

**Course:** CareerFoundry – Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.5, which introduces Object-Oriented Programming (OOP) principles in Python. The exercise transforms the recipe management application from a procedural, dictionary-based approach to an object-oriented architecture using custom classes and methods.

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Implementation Guide](#implementation-guide)
- [Key Concepts](#key-concepts)
- [Technical Challenges](#technical-challenges)
- [Deliverables](#deliverables)
- [AI Assistance Declaration](#ai-assistance-declaration)
- [Resources](#resources)

---

## Learning Objectives

- Understand core Object-Oriented Programming principles
- Define custom classes with data and procedural attributes
- Implement initialization methods and special methods
- Create getter and setter methods for controlled attribute access
- Utilize variable-length arguments in method definitions
- Distinguish between class variables and instance variables
- Build methods that interact with object state
- Implement object string representation for display purposes
- Create multiple instances from a single class blueprint
- Pass objects as function arguments

---

## Project Structure
Exercise-1.5/
│
├── README.md                    # This documentation
├── recipe_oop.py                # OOP implementation of recipe system
├── LEARNING_JOURNAL5.html       # Learning reflections
│
└── screenshots/
├── 01_creation_file_recipe_oop.png
├── 02_Add_getter&setter_methodes.png
├── 03_Add_Ingredients.png
├── 04_Calculate_Difficulty.png
├── 05_Search_Meth_&String_Show.png
├── 06_Recipe_Search.png
├── 07_Recipe_earch_Outside_Class.png
├── 08_Main_Code_A.png
├── 09_Create_Moe_Receipts.png
├── 10_REcipe_List&_Searches.png
├── 11_Test_Result.png
└── 12_Full_Code.png

---

## Implementation Guide

### Part 1: Class Definition

#### Step 1: Define the Recipe Class
```python
class Recipe:
    # Class variable shared across all instances
    all_ingredients = []
    
    def __init__(self, name):
        """Initialize a new recipe with a name"""
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None
Key components:

all_ingredients: Class variable tracking all ingredients across all recipes
__init__(): Initialization method called when creating new instances
self: Reference to the current instance
Instance variables: name, ingredients, cooking_time, difficulty


Step 2: Implement Getter and Setter Methods
pythondef get_name(self):
    """Return the recipe's name"""
    return self.name

def set_name(self, name):
    """Set the recipe's name"""
    self.name = name

def get_cooking_time(self):
    """Return the cooking time"""
    return self.cooking_time

def set_cooking_time(self, cooking_time):
    """Set the cooking time"""
    self.cooking_time = cooking_time
Purpose: Provide controlled access to object attributes following encapsulation principles.

Step 3: Implement Ingredient Management
pythondef add_ingredients(self, *ingredients):
    """Add multiple ingredients to the recipe"""
    for ingredient in ingredients:
        self.ingredients.append(ingredient)
    self.update_all_ingredients()

def get_ingredients(self):
    """Return the list of ingredients"""
    return self.ingredients

def update_all_ingredients(self):
    """Add this recipe's ingredients to the class-wide ingredient list"""
    for ingredient in self.ingredients:
        if ingredient not in Recipe.all_ingredients:
            Recipe.all_ingredients.append(ingredient)
Variable-length arguments: The *ingredients syntax allows methods to accept any number of arguments.

Step 4: Implement Difficulty Calculation
pythondef calculate_difficulty(self):
    """Calculate recipe difficulty based on cooking time and ingredients"""
    if self.cooking_time < 10 and len(self.ingredients) < 4:
        self.difficulty = "Easy"
    elif self.cooking_time < 10 and len(self.ingredients) >= 4:
        self.difficulty = "Medium"
    elif self.cooking_time >= 10 and len(self.ingredients) < 4:
        self.difficulty = "Intermediate"
    else:
        self.difficulty = "Hard"

def get_difficulty(self):
    """Return difficulty, calculating it first if needed"""
    if self.difficulty is None:
        self.calculate_difficulty()
    return self.difficulty
Logic:

Easy: < 10 minutes, < 4 ingredients
Medium: < 10 minutes, ≥ 4 ingredients
Intermediate: ≥ 10 minutes, < 4 ingredients
Hard: ≥ 10 minutes, ≥ 4 ingredients


Step 5: Implement Search and String Representation
pythondef search_ingredient(self, ingredient):
    """Search for an ingredient in this recipe"""
    return ingredient in self.ingredients

def __str__(self):
    """Return a formatted string representation of the recipe"""
    output = f"\n{'='*50}\n"
    output += f"Recipe: {self.name}\n"
    output += f"{'='*50}\n"
    output += f"Cooking Time: {self.cooking_time} minutes\n"
    output += f"Difficulty: {self.get_difficulty()}\n"
    output += f"Ingredients:\n"
    for ingredient in self.ingredients:
        output += f"  - {ingredient}\n"
    output += f"{'='*50}"
    return output
Special method: __str__() defines how objects are converted to strings when printed.

Part 2: Standalone Search Function
pythondef recipe_search(data, search_term):
    """Search for recipes containing a specific ingredient"""
    print(f"\nRecipes containing '{search_term}':")
    print("="*50)
    
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
Note: This function exists outside the Recipe class as a utility function that operates on Recipe objects.

Part 3: Main Program Execution
python# Create Recipe objects
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", 
                     "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
print(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", 
                                "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)

# Create list and perform searches
recipes_list = [tea, coffee, cake, banana_smoothie]

recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")

Key Concepts
Classes and Objects
Class: A blueprint defining structure and behavior
Object: A specific instance created from a class blueprint
pythonclass Recipe:  # Blueprint
    pass

tea = Recipe("Tea")     # Instance/Object
coffee = Recipe("Coffee")  # Another instance/object

The self Parameter
self represents the current instance within methods. It enables Python to distinguish which object's data to access.
pythondef get_name(self):
    return self.name  # Returns THIS object's name

tea.get_name()  # self = tea, returns tea's name
coffee.get_name()  # self = coffee, returns coffee's name

Special Methods
Methods with double underscores have special meanings in Python:

__init__(): Called automatically when creating new objects
__str__(): Called automatically when converting objects to strings
__repr__(): Called for object representation (not used in this exercise)


Class Variables vs Instance Variables
pythonclass Recipe:
    all_ingredients = []  # Class variable (shared by all instances)
    
    def __init__(self, name):
        self.name = name  # Instance variable (unique to each object)
Class variables are accessed via Recipe.all_ingredients
Instance variables are accessed via self.name or object.name

Variable-Length Arguments
pythondef add_ingredients(self, *ingredients):
    # *ingredients packs all arguments into a tuple
Enables flexible method calls:
pythontea.add_ingredients("Water")  # One argument
cake.add_ingredients("Sugar", "Butter", "Eggs")  # Three arguments

Method Chaining
Methods can call other methods within the same class:
pythondef add_ingredients(self, *ingredients):
    # ... add ingredients ...
    self.update_all_ingredients()  # Calls another method

def get_difficulty(self):
    if self.difficulty is None:
        self.calculate_difficulty()  # Calls another method
    return self.difficulty

Technical Challenges
Understanding the self Parameter
Challenge: The purpose and usage of self was initially unclear.
Resolution: Understood that self is a reference to the current instance. When tea.get_name() executes, self equals tea. This mechanism enables instance-specific data access.

Function Placement and Indentation
Challenge: Initially indented recipe_search() as if it were a class method.
Resolution: Moved function to zero indentation (left margin). While it operates on Recipe objects, it exists as a standalone utility function outside the class definition.

Class Variables vs Instance Variables
Challenge: Confusion between when to use self.ingredients versus Recipe.all_ingredients.
Resolution:

Instance variables (self.ingredients) are unique to each object
Class variables (Recipe.all_ingredients) are shared across all instances
Use class variables for aggregate data tracking across all objects


Variable-Length Arguments Syntax
Challenge: The *ingredients parameter notation seemed unusual.
Resolution: The asterisk operator enables functions to accept arbitrary argument counts. Python packs all arguments into a tuple, enabling iteration within the method body.

Deliverables

✅ recipe_oop.py - Complete OOP implementation
✅ 12 screenshots documenting development process
✅ LEARNING_JOURNAL5.html - Comprehensive learning documentation
✅ README5.md - Technical documentation (this file)
✅ Updated index.html with Exercise 1.5 navigation
✅ Updated GitHub repository with organized structure


AI Assistance Declaration
This exercise was completed through structured, checkpoint-based guidance with AI assistance. Object-Oriented Programming introduced fundamentally new programming paradigms requiring systematic explanation and implementation support.
Technical Problem-Solving

Conceptual clarification: AI explained abstract OOP concepts (classes, objects, self, special methods) through analogies and concrete examples
Structured tutorial: Checkpoint-based approach decomposed complex implementation into manageable steps with verification at each stage
Syntax guidance: AI explained special method syntax (__init__, __str__) and variable-length argument notation (*args)
Code organization: AI demonstrated proper indentation patterns distinguishing class methods from standalone functions
Debugging support: AI assisted in identifying and resolving indentation errors and method placement issues

Learning Context
This exercise was completed using AI as an interactive programming tutor, with checkpoints confirming understanding before proceeding. All code was typed manually, executed directly, and debugged hands-on. When errors occurred, solutions were implemented following AI guidance while developing understanding of underlying principles.
Implementation Approach
The checkpoint-based tutorial enabled progressive understanding of interconnected OOP concepts while maintaining hands-on implementation throughout. AI served as an interactive reference resource, similar to technical documentation or programming forums, while all actual coding, testing, and debugging was completed independently.

Resources
Python Documentation

Python 3.9 Official Documentation
Python Classes
Data Model and Special Methods

Learning Resources

Real Python - Object-Oriented Programming in Python
Real Python - Python Classes and Objects


Summary
Exercise 1.5 introduced Object-Oriented Programming, representing a fundamental paradigm shift from procedural programming. By transforming recipes from dictionaries into custom objects with their own methods, the code became more organized, maintainable, and aligned with professional software development practices.
The Recipe class encapsulates related data and functionality, following core OOP principles of encapsulation and abstraction. Understanding classes, objects, the self parameter, and special methods provides the foundation for working with Python frameworks like Django, where OOP is fundamental to application architecture.
This exercise completes the core Python fundamentals for Achievement 1: data types (1.1), data structures (1.2), control flow (1.3), file handling (1.4), and object-oriented programming (1.5). These skills collectively enable development of complete, professional-grade Python applications.

Repository: [https://github.com/ivencomur/PYTHON_COURSE/tree/Exercise-1.5]
Contact: Ivan Cortes
Previous: Exercise 1.4 | Next: Achievement 1 Final Task

Documentation created to support future learners understanding Object-Oriented Programming in Python.