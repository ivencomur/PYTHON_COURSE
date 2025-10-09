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
    
def take_recipe():
    # Collect recipe information from user and return as dictionary 
    name = input("Enter recipe name: ").strip()
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients_input = input("Enter ingredients (separated by commas): ").strip()
    
    # Convert comma-separated string into a clean list
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    
    # Calculate difficulty using our helper function
    difficulty = calc_difficulty(cooking_time, ingredients)
    
    # Package everything into a dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe


# Main code begins here
filename = input("Enter the filename to store recipes (e.g., 'recipes.bin'): ")

try:
    # 'rb' = read binary mode
    file = open(filename, 'rb')  
    data = pickle.load(file)
    
except FileNotFoundError:
    # File doesn't exist, then new data structure
    print("File not found. Creating a new recipe file.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
except:
    # For other unexpected error
    print("An unexpected error occurred. Creating new data.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }
    
else:
    # File was opened successfully, then close it
    file.close()
    
finally:
    # extract the data into variables, always running
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

#Second part: Colecting recipes
# Ask how many recipes to enter
n = int(input("\nHow many recipes would you like to enter? "))

# Collect recipes
for i in range(n):
    print(f"\n--- Recipe {i + 1} ---")
    recipe = take_recipe()
    
    # Add new ingredients to all_ingredients list
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    # Add recipe to recipes_list
    recipes_list.append(recipe)

print("\nAll recipes collected successfully!")


# Update the data dictionary with new recipes and ingredients
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

# Save everything to the file
# 'wb' = write binary mode
file = open(filename, 'wb')  
pickle.dump(data, file)
file.close()

print(f"\nRecipes saved successfully to {filename}!")