# Exercise 1.6 – Databases in Python

**Course:** CareerFoundry – Python for Web Developers (Full-Stack)  
**Author:** Ivan Cortes  
**Date:** October 2025

---

## Overview

This document provides a complete walkthrough of Exercise 1.6, which introduces MySQL database integration with Python. The exercise transforms the recipe management application from file-based storage (Exercise 1.4) to a MySQL database system, implementing full CRUD (Create, Read, Update, Delete) operations through a command-line interface.

---

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Project Structure](#project-structure)
- [Implementation Guide](#implementation-guide)
- [Program Features](#program-features)
- [Code Structure](#code-structure)
- [Key Concepts](#key-concepts)
- [Technical Challenges](#technical-challenges)
- [Security Considerations](#security-considerations)
- [Testing](#testing)
- [Deliverables](#deliverables)
- [AI Assistance Declaration](#ai-assistance-declaration)
- [Resources](#resources)

---

## Learning Objectives

- Install and configure MySQL Server on local system
- Create MySQL users and grant appropriate permissions
- Connect Python applications to MySQL databases using mysql-connector-python
- Design and create relational database tables with appropriate data types
- Implement CRUD operations using SQL queries from Python
- Build parameterized SQL queries to prevent SQL injection attacks
- Implement comprehensive error handling for user input validation
- Understand data type conversions between Python and MySQL
- Create interactive command-line applications with menu-driven interfaces
- Commit database transactions appropriately

---

## Project Structure

```
Exercise-1.6/
│
├── README.md                    # This documentation
├── recipe_mysql.py              # Complete database application
├── LEARNING_JOURNAL6.html       # Learning reflections
│
└── screenshots/
    ├── 01-part1-database-setup.png
    ├── 02-correcting-installation-errors.png
    ├── 03-creating-sql-database.png
    ├── 04-connect-database.png
    ├── 05-part2-main-menu.png
    ├── 06-calculate-difficulty-create-recipe.png
    ├── 07-07A-part4-search-recipe.png
    ├── 08-part5-update-recipe.png
    ├── 09-part6-delete-recipe.png
    ├── 10-full-code.png
    ├── 11-creating-test-recipes.png
    ├── 12-searching-by-ingredient.png
    ├── 13-updating-recipes.png
    ├── 14-deleting-recipe.png
    └── 15-exit-program.png
```

---

## Implementation Guide

### Part 1: MySQL Setup and Database Creation

#### MySQL Server Installation

**Windows 11:**
1. Downloaded MySQL Community Server installer
2. Selected "Developer Default" installation type
3. Configured MySQL Server with strong password encryption
4. Set root password: `password`
5. Started MySQL Server as Windows service

**User Creation:**
```sql
CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'cf-python'@'localhost';
FLUSH PRIVILEGES;
```

#### Python Database Connection

```python
import mysql.connector

# Establish connection to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
```

**Key points:**
- Connection object (conn) maintains session with MySQL server
- Cursor object (cursor) executes SQL commands and retrieves results
- IF NOT EXISTS prevents errors on subsequent runs

#### Table Structure

```python
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')
```

**Column specifications:**
- id: Auto-incrementing primary key for unique recipe identification
- name: Recipe name limited to 50 characters
- ingredients: Comma-separated string (MySQL doesn't natively support Python lists)
- cooking_time: Integer representing minutes
- difficulty: Calculated value stored as string (Easy, Medium, Intermediate, Hard)

---

### Part 2: Helper Function

```python
def calculate_difficulty(cooking_time, ingredients):
    """Calculate recipe difficulty based on time and ingredient count"""
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"
```

Same logic from Exercises 1.3-1.5, ensuring consistency across implementations.

---

### Part 3: Create Recipe Function

```python
def create_recipe(conn, cursor):
    """Collect recipe data and insert into database"""
    name = input("Enter recipe name: ")
    
    # Error handling for numeric input
    try:
        cooking_time = int(input("Enter cooking time (minutes): "))
    except ValueError:
        print("Error: Please enter a valid number for cooking time.")
        return
    
    try:
        num_ingredients = int(input("How many ingredients? "))
    except ValueError:
        print("Error: Please enter a valid number for ingredient count.")
        return
    
    # Collect ingredients
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # Convert list to comma-separated string
    ingredients_str = ", ".join(ingredients)
    
    # Parameterized query prevents SQL injection
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    
    print(f"\nRecipe '{name}' added successfully!")
```

**Key techniques:**
- Try-except blocks catch ValueError when users enter non-numeric data
- Early return on error prevents incomplete data insertion
- ", ".join() converts Python list to MySQL-compatible string
- Parameterized queries using %s placeholders prevent SQL injection
- conn.commit() makes changes permanent

---

### Part 4: Search Recipe Function

```python
def search_recipe(conn, cursor):
    """Search for recipes containing specific ingredient"""
    # Retrieve all ingredients from database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    # Build unique ingredient list
    all_ingredients = []
    for row in results:
        ingredients_list = row[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display numbered ingredient list
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # Handle user selection with error checking
    try:
        choice = int(input("\nEnter ingredient number to search: "))
        search_ingredient = all_ingredients[choice - 1]
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    except IndexError:
        print("Error: That number is not in the list.")
        return
    
    # Search using parameterized query with LIKE operator
    sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
    cursor.execute(sql, ('%' + search_ingredient + '%',))
    results = cursor.fetchall()
    
    # Display results
    print(f"\nRecipes with {search_ingredient}:")
    for row in results:
        print(f"\nID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Ingredients: {row[2]}")
        print(f"Cooking Time: {row[3]} minutes")
        print(f"Difficulty: {row[4]}")
```

**Important security fix:**
- Original code used f-string formatting: `f"... WHERE ingredients LIKE '%{search_ingredient}%'"`
- Security vulnerability: Allows SQL injection attacks
- Fixed version: Uses parameterized query with proper escaping

**enumerate() usage:**
- Starts numbering at 1 for user-friendly display
- Provides both index and value during iteration

---

### Part 5: Update Recipe Function

```python
def update_recipe(conn, cursor):
    """Modify existing recipe in database"""
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    print("\nAll Recipes:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    # Get recipe selection
    try:
        recipe_id = int(input("\nEnter recipe ID to update: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Get field to update
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        new_name = input("Enter new name: ")
        sql = "UPDATE Recipes SET name = %s WHERE id = %s"
        cursor.execute(sql, (new_name, recipe_id))
        
    elif choice == "2":
        try:
            new_time = int(input("Enter new cooking time: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        
        # Retrieve ingredients to recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients_list = ingredients_str.split(", ")
        new_difficulty = calculate_difficulty(new_time, ingredients_list)
        
        sql = "UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (new_time, new_difficulty, recipe_id))
        
    elif choice == "3":
        try:
            num_ingredients = int(input("How many ingredients? "))
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        
        ingredients = []
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        
        # Retrieve cooking time to recalculate difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        new_difficulty = calculate_difficulty(cooking_time, ingredients)
        
        sql = "UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (ingredients_str, new_difficulty, recipe_id))
    
    conn.commit()
    print("\nRecipe updated successfully!")
```

**Critical logic:**
- When cooking_time or ingredients change, difficulty must be recalculated
- Requires retrieving the unchanged value from database
- Updates both modified field and difficulty in single transaction

---

### Part 6: Delete Recipe Function

```python
def delete_recipe(conn, cursor):
    """Remove recipe from database"""
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    print("\nAll Recipes:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    # Get recipe to delete
    try:
        recipe_id = int(input("\nEnter recipe ID to delete: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Execute deletion
    sql = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(sql, (recipe_id,))
    conn.commit()
    
    print("\nRecipe deleted successfully!")
```

**DELETE operation:**
- Permanently removes row from table
- Uses WHERE clause to target specific recipe by ID
- Parameterized query prevents SQL injection

---

### Part 7: Main Menu Implementation

```python
def main_menu(conn, cursor):
    """Display menu and route to appropriate function"""
    while True:
        print("\n" + "="*40)
        print("RECIPE APP - MAIN MENU")
        print("="*40)
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
    
    # Removed redundant conn.commit() - each function commits its own changes
    conn.close()

# Run the application
main_menu(conn, cursor)
```

**Program flow:**
- Infinite loop displays menu until user exits
- Each function handles its own commit operation
- Connection closed only on exit
- Simple input validation for menu choices

---

## Program Features

### Data Persistence
- All recipes stored permanently in MySQL database
- Data survives program termination
- Supports concurrent access (multiple programs can use same database)

### CRUD Operations
- **Create:** Add new recipes with calculated difficulty
- **Read:** Search recipes by ingredient
- **Update:** Modify recipe name, time, or ingredients
- **Delete:** Remove unwanted recipes

### Error Handling
- Validates all numeric inputs (cooking time, ingredient count, menu choices)
- Catches ValueError for type conversion errors
- Catches IndexError for out-of-range selections
- Provides user-friendly error messages
- Prevents program crashes on invalid input

### Security
- Parameterized queries prevent SQL injection attacks
- No direct string interpolation in SQL statements
- User input properly escaped before database insertion

---

## Code Structure

### Imports
- mysql.connector: MySQL database connectivity

### Database Initialization
- Connection establishment
- Database creation
- Table creation

### Functions
- calculate_difficulty(cooking_time, ingredients): Returns difficulty string
- create_recipe(conn, cursor): Inserts new recipe
- search_recipe(conn, cursor): Searches by ingredient
- update_recipe(conn, cursor): Modifies existing recipe
- delete_recipe(conn, cursor): Removes recipe

### Main Program
- main_menu(conn, cursor): Menu loop and function routing
- Final execution call

---

## Key Concepts

### Relational Databases
- Organize data in tables with rows and columns
- Each row represents one record (recipe)
- Each column represents one attribute (name, cooking_time, etc.)
- Primary keys uniquely identify rows

### MySQL Data Types
- **INT:** Whole numbers (cooking_time, id)
- **VARCHAR(n):** Variable-length strings up to n characters
- **AUTO_INCREMENT:** Automatically assigns sequential numbers
- **PRIMARY KEY:** Uniquely identifies each row

### SQL Operations

**CREATE:** Define table structure
```sql
CREATE TABLE IF NOT EXISTS Recipes (...)
```

**INSERT:** Add new rows
```sql
INSERT INTO Recipes (...) VALUES (...)
```

**SELECT:** Retrieve data
```sql
SELECT * FROM Recipes WHERE ingredients LIKE '%Water%'
```

**UPDATE:** Modify existing rows
```sql
UPDATE Recipes SET cooking_time = 7 WHERE id = 1
```

**DELETE:** Remove rows
```sql
DELETE FROM Recipes WHERE id = 4
```

### Parameterized Queries

**Unsafe (SQL Injection vulnerability):**
```python
sql = f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
```

**Safe (Parameterized):**
```python
sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
cursor.execute(sql, ('%' + search_ingredient + '%',))
```

### Data Type Conversions

**Python → MySQL:**
- Python list → SQL VARCHAR (using ", ".join())
- Python int → SQL INT (automatic)
- Python str → SQL VARCHAR (automatic)

**MySQL → Python:**
- SQL VARCHAR → Python string (automatic)
- SQL INT → Python int (automatic)
- Comma-separated string → Python list (using .split(", "))

### Database Transactions
- Changes are temporary until commit() is called
- commit() makes changes permanent
- Each CRUD function commits its own changes
- Connection must be closed with close() before program ends

---

## Technical Challenges

### Challenge 1: Python Version Mismatch
**Problem:** Initial environment had Python 3.13 and Python 3.9 installed. python command pointed to 3.13, but pip pointed to 3.9, causing module not found errors.

**Resolution:** Used py -3.9 launcher to explicitly target Python 3.9 for both script execution and package installation.

**Lesson:** Virtual environments must use consistent Python versions. Always verify which python and which pip match.

---

### Challenge 2: SQL Injection Vulnerability
**Problem:** Original search function used f-string formatting in SQL query:
```python
sql = f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
```

**Risk:** Malicious input like `'; DROP TABLE Recipes; --` could delete entire database.

**Fix:** Implemented parameterized query:
```python
sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
cursor.execute(sql, ('%' + search_ingredient + '%',))
```

**Lesson:** Never concatenate user input directly into SQL strings. Always use parameterized queries.

---

### Challenge 3: Missing Error Handling
**Problem:** Code used int(input(...)) without validation. Non-numeric input crashed the program.

**Fix:** Wrapped conversions in try-except blocks:
```python
try:
    cooking_time = int(input("Enter cooking time (minutes): "))
except ValueError:
    print("Error: Please enter a valid number.")
    return
```

**Lesson:** User input is unpredictable. Always validate and handle conversion errors gracefully.

---

### Challenge 4: List to String Conversion
**Problem:** MySQL doesn't support Python list data type.

**Solution:** Convert lists to comma-separated strings:
- **Storing:** `ingredients_str = ", ".join(ingredients)`
- **Retrieving:** `ingredients_list = ingredients_str.split(", ")`

**Lesson:** Understand data type limitations between programming languages and databases.

---

### Challenge 5: Difficulty Recalculation on Updates
**Problem:** When updating cooking_time, difficulty becomes outdated. When updating ingredients, difficulty also needs recalculation.

**Solution:** Retrieve unchanged value from database, recalculate difficulty, update both fields:
```python
# Updating cooking_time
cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
ingredients_str = cursor.fetchone()[0]
ingredients_list = ingredients_str.split(", ")
new_difficulty = calculate_difficulty(new_time, ingredients_list)
```

**Lesson:** Derived values (like difficulty) must be recalculated when their dependencies change.

---

## Security Considerations

### SQL Injection Prevention
Always use parameterized queries:
```python
# Good
cursor.execute("SELECT * FROM Recipes WHERE id = %s", (user_id,))

# Bad - NEVER do this
cursor.execute(f"SELECT * FROM Recipes WHERE id = {user_id}")
```

### Input Validation
Validate all user input before processing:
- Type checking (int conversion with try-except)
- Range checking (list indices)
- Format validation (where applicable)

### Database Credentials
Current setup uses hardcoded credentials for learning purposes:
```python
user='cf-python'
passwd='password'
```

**Production best practices:**
- Store credentials in environment variables
- Use configuration files outside version control
- Implement proper authentication mechanisms

---

## Testing

### Test Data

Four recipes created during testing:

**Recipe 1: Tea**
- Cooking time: 5 minutes
- Ingredients: Tea Leaves, Sugar, Water
- Expected difficulty: Easy
- Result: ✓ Created successfully

**Recipe 2: Coffee**
- Cooking time: 5 minutes
- Ingredients: Coffee Powder, Sugar, Water
- Expected difficulty: Easy
- Result: ✓ Created successfully

**Recipe 3: Omelette**
- Cooking time: 15 minutes
- Ingredients: Eggs, Milk, Cheese, Onions
- Expected difficulty: Hard
- Result: ✓ Created successfully

**Recipe 4: Pasta**
- Cooking time: 12 minutes
- Ingredients: Pasta, Tomato Sauce, Salt
- Expected difficulty: Intermediate
- Result: ✓ Created successfully

### Operation Tests

**Create Function:**
- ✓ Accepts valid input
- ✓ Handles non-numeric cooking time gracefully
- ✓ Handles non-numeric ingredient count gracefully
- ✓ Calculates difficulty correctly
- ✓ Commits changes to database

**Search Function:**
- ✓ Displays all unique ingredients
- ✓ Finds recipes containing "Water" (Tea, Coffee)
- ✓ Handles invalid ingredient number
- ✓ Handles non-numeric input
- ✓ Uses parameterized query (SQL injection prevented)

**Update Function:**
- ✓ Displays all recipes for selection
- ✓ Updates recipe name successfully
- ✓ Updates cooking time and recalculates difficulty
- ✓ Updates ingredients and recalculates difficulty
- ✓ Handles invalid input gracefully

**Delete Function:**
- ✓ Displays all recipes for selection
- ✓ Removes specified recipe from database
- ✓ Handles invalid recipe ID
- ✓ Commits deletion permanently

**Program Flow:**
- ✓ Menu displays correctly
- ✓ Functions execute based on user choice
- ✓ Returns to menu after each operation
- ✓ Exits cleanly when user selects option 5
- ✓ Closes database connection on exit

---

## Deliverables

- ✅ MySQL Server installed and configured
- ✅ User cf-python created with appropriate permissions
- ✅ recipe_mysql.py - Complete database application with security fixes
- ✅ 15 screenshots documenting code sections and testing
- ✅ LEARNING_JOURNAL6.html - Comprehensive learning documentation
- ✅ README.md - Technical documentation (this file)
- ✅ Updated index.html with Exercise 1.6 link
- ✅ Updated GitHub repository with organized structure

---

## AI Assistance Declaration



### Self-Directed Problem-Solving Approach

Due to limited availability of school support during critical phases, I had to become more resilient in independent problem-solving through:

**Primary Learning Methods:**
- Extensive reading of current Python and MySQL documentation
- Careful review of deprecation notices and migration guides
- Systematic testing of updated syntax and methods
- Pattern recognition from previous exercises to adapt new concepts
- Intuitive debugging based on error messages and stack traces

**AI-Assisted Learning:**

When documentation and experimentation were insufficient, AI tools provided:

- **Security code review:** Identified SQL injection vulnerability in original search function using f-strings; explained parameterized query syntax and why string formatting in SQL creates security risks
- **Version compatibility:** Bridged gaps between course materials (often referencing Python 3.8.x/MySQL 5.x) and current stable versions (Python 3.9.x/MySQL 8.x)
- **Error handling guidance:** Demonstrated try-except patterns for ValueError and IndexError for comprehensive error handling examples (not included in materials but in official documentation)
- **Environment troubleshooting:** Diagnosed Python version mismatch between python and pip commands; provided resolution using py -3.9 launcher
- **Code optimization:** Identified redundant conn.commit() in main_menu function; explained transaction management principles

### Implementation Reality

All code was typed manually, executed directly, and debugged hands-on. Security vulnerabilities were corrected following AI guidance while developing understanding of underlying principles. The checkpoint-based learning approach enabled progressive mastery of interconnected database concepts (connections, cursors, SQL syntax, transactions, parameterized queries) despite gaps in formal instruction.

### Reflection

Navigating challenges like older course materials and limited mentor availability became a valuable opportunity for growth. It showed me that while mentorship is a fantastic accelerator, I can build deep knowledge through persistent self-study and resourceful problem-solving—skills that I know are essential for success in a real-world development environment.
---

## Resources

### MySQL Documentation
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
- [MySQL SQL Statements](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

### Python Database Programming
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [PEP 249 – Python Database API Specification](https://www.python.org/dev/peps/pep-0249/)

### Security Resources
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Bobby Tables: A guide to preventing SQL injection](https://bobby-tables.com/)

### Learning Resources
- [Real Python - Introduction to MySQL](https://realpython.com/python-mysql/)
- [Real Python - Preventing SQL Injection](https://realpython.com/prevent-python-sql-injection/)

---

## Summary

Exercise 1.6 introduced relational database management, representing a significant advancement in data persistence capabilities. By transitioning from file-based storage (Exercise 1.4's pickle files) to MySQL databases, the recipe application gained professional-grade data management, concurrent access support, and structured query capabilities.

The exercise demonstrated how Python applications integrate with database systems through connectors, how to structure SQL queries safely using parameterization, and how to implement comprehensive error handling for user-facing applications. Understanding CRUD operations, transaction management, and SQL injection prevention provides foundational skills applicable to all database-driven applications.

This exercise completes Achievement 1's technical foundations: environment setup (1.1), data structures (1.2), control flow (1.3), file handling (1.4), object-oriented programming (1.5), and now database integration (1.6). These skills collectively enable development of complete, production-ready Python applications with persistent data storage.

---

**Repository:** https://github.com/ivencomur/PYTHON_COURSE  
**Contact:** Ivan Cortes  
**Previous:** Exercise 1.5 | **Next:** Achievement 1 Final Task

---

*Documentation created to support future learners understanding database integration with Python.*