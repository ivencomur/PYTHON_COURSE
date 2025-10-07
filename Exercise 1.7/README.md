# Exercise 1.7 – Object-Relational Mapping in Python

**Course:** CareerFoundry – Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025  
**Python Version:** 3.13.5 (adapted from course materials targeting Python 3.8.x/3.9.x)

---

## Overview

Exercise 1.7 represents the culmination of Achievement 1, introducing Object-Relational Mapping (ORM) through SQLAlchemy. This exercise refactors the MySQL-based Recipe application from Exercise 1.6, replacing raw SQL queries with ORM patterns for cleaner, more maintainable code.

**Key Achievement:** Building a complete CRUD application using SQLAlchemy's ORM instead of direct SQL queries, demonstrating modern Python database interaction patterns.

---

## Technical Stack

- **Python:** 3.13.5
- **Database:** MySQL 8.0
- **ORM Framework:** SQLAlchemy 2.0.43
- **Database Connector:** mysqlclient 2.2.7
- **Virtual Environment:** `cf-python-ex17`

**Note on Version Adaptation:** Course materials targeted Python 3.8.x/3.9.x with older SQLAlchemy versions. All code has been adapted and tested for Python 3.13.5 with current library versions, addressing deprecated imports and syntax changes.

---

## What is ORM?

**Object-Relational Mapping (ORM)** translates between two worlds:
- **Python world:** Objects, classes, methods
- **Database world:** Tables, rows, SQL queries

**Without ORM (Exercise 1.6 approach):**
```python
cursor.execute("INSERT INTO Recipes (name, cooking_time, ingredients) VALUES (%s, %s, %s)", 
               (name, cooking_time, ingredients_str))
conn.commit()
With ORM (Exercise 1.7 approach):
pythonrecipe = Recipe(name=name, cooking_time=cooking_time, ingredients=ingredients_str)
session.add(recipe)
session.commit()
Benefits:

Write Python instead of SQL
Database-agnostic code (works with MySQL, PostgreSQL, SQLite)
Type safety and IDE autocomplete
Automatic SQL generation
Cleaner, more readable code


Application Structure
Database Model
Table: final_recipes
ColumnTypeConstraintsidIntegerPrimary Key, Auto-incrementnameString(50)Recipe nameingredientsString(255)Comma-separated ingredient listcooking_timeIntegerMinutesdifficultyString(20)Easy/Medium/Intermediate/Hard
Recipe Class (ORM Model)
pythonclass Recipe(Base):
    __tablename__ = "final_recipes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
Methods:

__repr__() - Short representation for debugging
__str__() - Formatted display for users
calculate_difficulty() - Determines recipe complexity
return_ingredients_as_list() - Converts string to list


CRUD Operations
CREATE - Adding Recipes
pythondef create_recipe():
    recipe_entry = Recipe(name=name, cooking_time=cooking_time, ingredients=ingredients_str)
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
ORM Pattern: Create object → Call methods → Add to session → Commit
READ - Viewing Recipes
pythondef view_all_recipes():
    recipes = session.query(Recipe).all()
    for recipe in recipes:
        print(recipe)
ORM Pattern: session.query(Recipe).all() replaces SELECT * FROM Recipes
SEARCH - Filtering by Ingredient
pythondef search_by_ingredients():
    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    recipes = session.query(Recipe).filter(*conditions).all()
ORM Pattern: .filter() with .like() replaces SQL WHERE and LIKE clauses
UPDATE - Editing Recipes
pythondef edit_recipe():
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    recipe_to_edit.name = new_name
    recipe_to_edit.calculate_difficulty()
    session.commit()
ORM Pattern: Retrieve object → Modify attributes → Commit (no UPDATE SQL needed)
DELETE - Removing Recipes
pythondef delete_recipe():
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    session.delete(recipe_to_delete)
    session.commit()
ORM Pattern: Retrieve object → Delete object → Commit

Key Concepts Learned
1. Declarative Base
pythonBase = declarative_base()
Foundation for all ORM models. Classes inherit from Base to become database-mapped.
2. Engine and Session
pythonengine = create_engine("mysql://user:password@localhost/database")
Session = sessionmaker(bind=engine)
session = Session()

Engine: Database connection manager
Session: Transaction handler (replaces cursor from Exercise 1.6)

3. Column Definitions
pythonid = Column(Integer, primary_key=True, autoincrement=True)
name = Column(String(50))
Python syntax that SQLAlchemy converts to SQL CREATE TABLE statements.
4. Special Methods

__repr__() - Quick debug view: <Recipe ID: 1 - Tea>
__str__() - Full formatted display with all details

5. Query Methods

.all() - Returns list of all matching objects
.first() - Returns first matching object
.filter() - Adds WHERE conditions
.count() - Returns number of rows


Exercise 1.6 vs Exercise 1.7 Comparison
AspectExercise 1.6 (Raw SQL)Exercise 1.7 (ORM)Connectionconn = mysql.connector.connect(...)engine = create_engine(...)Cursor/Sessioncursor = conn.cursor()session = Session()Createcursor.execute("INSERT INTO...")session.add(recipe)Readcursor.execute("SELECT * FROM...")session.query(Recipe).all()Updatecursor.execute("UPDATE... WHERE...")recipe.name = "Tea"; session.commit()Deletecursor.execute("DELETE FROM... WHERE...")session.delete(recipe)Commitconn.commit()session.commit()Data TypeTuplesPython objects

Screenshots Reference
Setup and Configuration

Screenshot 01: SQLAlchemy & Python incompatibility and update installation
Screenshot 02: Python ex 17 update running
Screenshot 03: Imports & Engine setup

Code Structure

Screenshot 04: Complete Recipe Class
Screenshot 05: Table & Session Creation
Screenshot 06: All CRUD Functions
Screenshot 07: Main Menu implementation
Screenshot 08: Delete Recipe function
Screenshot 09: Full Code overview

Testing Process

Screenshot 10: Test 1 - Creating recipes
Screenshot 11: View All Recipes test
Screenshot 12: Find By Ingredient test
Screenshot 13: Update Recipe test
Screenshot 14: Delete Recipe test
Screenshot 15: Exit test


Challenges Encountered and Solutions
Python Version Mismatch
Problem: Course materials for Python 3.8.x/3.9.x; system running Python 3.13.5
Solution: Created dedicated virtual environment (cf-python-ex17) with Python 3.13.5, ensuring pip and python commands matched
SQLAlchemy Import Deprecations
Problem: Course used declarative_base from older SQLAlchemy versions
Solution: Verified current import path: from sqlalchemy.ext.declarative import declarative_base still works in SQLAlchemy 2.0.43
Indentation Errors in Class Methods
Problem: calculate_difficulty() and return_ingredients_as_list() initially placed outside Recipe class
Solution: Proper indentation (4 spaces) to place methods inside class scope, aligned with __repr__ and __str__
Understanding ORM Concepts
Challenge: Grasping the abstraction layer between Python objects and SQL tables
Solution: Systematic comparison of Exercise 1.6 (raw SQL) vs Exercise 1.7 (ORM) patterns, visualizing how SQLAlchemy translates Python to SQL

Testing Verification
Test Recipes Created:

Tea - 5 minutes, Easy - Tea Leaves, Sugar, Water (later updated to 3 minutes)
Coffee - 5 minutes, Easy - Coffee Powder, Sugar, Water
Cake - 50 minutes, Hard - Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
Banana Smoothie - 5 minutes, Medium - Bananas, Milk, Peanut Butter, Sugar, Ice Cubes (later deleted)

Operations Tested:

✓ CREATE: All 4 recipes added successfully with automatic difficulty calculation
✓ READ: All recipes displayed with correct formatting
✓ SEARCH: Correct filtering by Water (2 results), Sugar (4 results), Eggs (1 result)
✓ UPDATE: Tea cooking time modified, difficulty recalculated
✓ DELETE: Banana Smoothie removed with confirmation, 3 recipes remain
✓ EXIT: Session and engine closed properly


Installation Instructions
Prerequisites

Python 3.13.5 (or 3.9+)
MySQL Server 8.0 running
MySQL user cf-python with password password and database task_database

Setup Steps

Create virtual environment:

bashpython -m venv cf-python-ex17
source cf-python-ex17/Scripts/activate  # Windows Git Bash
# or
source cf-python-ex17/bin/activate      # macOS/Linux

Install dependencies:

bashpip install sqlalchemy mysqlclient

Verify installations:

bashpython -c "import sqlalchemy; print(sqlalchemy.__version__)"

Ensure MySQL is running:

Windows: Services → MySQL80 → Running
macOS: System Preferences → MySQL → Green dot
Linux: sudo systemctl status mysql


Run application:

bashpython recipe_app.py

File Structure
Exercise 1.7/
├── recipe_app.py           # Main application file
├── README.md              # This file
├── LEARNING_JOURNAL7.html # Learning reflection
└── screenshots/           # 15 verification screenshots
    ├── 01_Alquemy_&_Python_Incompatibility_and_update_instalation.png
    ├── 02_Python_ex_17_update_running.png
    ├── 03_Imports_&_Engine.png
    ├── 04_Complete_Recipe_Class.png
    ├── 05-Table_&_Session_Creation.png
    ├── 06_All_CRUD_Functions.png
    ├── 07_Main_Menu.png
    ├── 08_Delete_Recipe.png
    ├── 09_Full_Code.png
    ├── 10_Test_1.png
    ├── 11_View_All_Recipes_TST.png
    ├── 12_Find_By_Ingredient_TST.png
    ├── 13_Update_Recipe_TST.png
    ├── 14_Delete_Recipe.png
    └── 15_Exit_TST.png

AI Assistance Declaration
Learning Context
This exercise was completed while working through course materials that required adaptation from Python 3.8.x/SQLAlchemy 1.x to Python 3.13.5/SQLAlchemy 2.0.43. The learning process involved systematic problem-solving to bridge version gaps and understand ORM concepts.
Technical Challenges Addressed

Version compatibility: Adapting deprecated code patterns to current Python/SQLAlchemy standards
ORM conceptual understanding: Grasping abstraction layers between Python objects and SQL
Debugging: Resolving indentation errors and scope issues in class definitions
Testing methodology: Systematic verification of all CRUD operations

Independent Work

Created Python 3.13.5 virtual environment and managed dependencies
Debugged code systematically, fixing indentation and structural errors
Executed complete testing suite with 4 recipes and all CRUD operations
Captured 15 screenshots documenting the entire process
Generated comprehensive technical documentation

Approach
AI tools served as a technical reference for version adaptation and concept clarification, similar to consulting documentation when working with updated library versions. All implementation, testing, and debugging was performed hands-on, with focus on understanding underlying ORM principles rather than just completing the exercise.

Key Takeaways
Technical Understanding

ORM provides powerful abstraction over SQL, trading direct control for developer productivity
SQLAlchemy's declarative approach makes database schemas readable as Python classes
Session management parallels transaction handling in raw SQL but with cleaner syntax
Query chaining (.filter().all()) offers intuitive, composable database operations

Professional Skills

Adapting deprecated code to current standards is a critical developer skill
Version management through virtual environments prevents dependency conflicts
Systematic testing catches errors early and validates functionality
Clear documentation preserves knowledge for future reference

Achievement 1 Completion
Exercise 1.7 synthesizes all prior concepts:

Environment setup (1.1)
Data structures (1.2)
Functions and control flow (1.3)
File handling and error management (1.4)
Object-oriented programming (1.5)
Database interaction (1.6)
ORM patterns (1.7)

Status: Achievement 1 complete. Ready for Achievement 2: Django Web Development.