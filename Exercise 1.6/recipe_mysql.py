import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

cursor = conn.cursor()

# Create and use database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Create Recipes table
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

# Function to calculate difficulty
def calculate_difficulty(cooking_time, ingredients):
    num_ingredients = len(ingredients)
    
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

# Function to create a recipe
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    
    ingredients = []
    num_ingredients = int(input("How many ingredients? "))
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)
    
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    
    print(f"\nRecipe '{name}' added successfully!")

# Function to search recipes
def search_recipe(conn, cursor):
    # Get all ingredients from database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    all_ingredients = []
    for row in results:
        ingredients_list = row[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display ingredients
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    choice = int(input("\nEnter ingredient number to search: "))
    search_ingredient = all_ingredients[choice - 1]
    
    # Search for recipes
    sql = f"SELECT * FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    print(f"\nRecipes with {search_ingredient}:")
    for row in results:
        print(f"\nID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Ingredients: {row[2]}")
        print(f"Cooking Time: {row[3]} minutes")
        print(f"Difficulty: {row[4]}")

# Function to update a recipe
def update_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    print("\nAll Recipes:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    recipe_id = int(input("\nEnter recipe ID to update: "))
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
        new_time = int(input("Enter new cooking time: "))
        # Get ingredients to recalculate difficulty
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients_str = cursor.fetchone()[0]
        ingredients_list = ingredients_str.split(", ")
        new_difficulty = calculate_difficulty(new_time, ingredients_list)
        
        sql = "UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (new_time, new_difficulty, recipe_id))
    elif choice == "3":
        num_ingredients = int(input("How many ingredients? "))
        ingredients = []
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        # Get cooking time to recalculate difficulty
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        new_difficulty = calculate_difficulty(cooking_time, ingredients)
        
        sql = "UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s"
        cursor.execute(sql, (ingredients_str, new_difficulty, recipe_id))
    
    conn.commit()
    print("\nRecipe updated successfully!")

# Function to delete a recipe
def delete_recipe(conn, cursor):
    # Display all recipes
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    
    print("\nAll Recipes:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")
    
    recipe_id = int(input("\nEnter recipe ID to delete: "))
    
    sql = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(sql, (recipe_id,))
    conn.commit()
    
    print("\nRecipe deleted successfully!")

# Main menu
def main_menu(conn, cursor):
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
    
    conn.commit()
    conn.close()

# Run the app
main_menu(conn, cursor)