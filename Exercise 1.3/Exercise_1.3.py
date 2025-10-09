recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the recipe name: ").strip()
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter ingredients (separated by commas): ").strip().split(',')
    
    # No spaces in names
    ingredients = [ingredient.strip() for ingredient in ingredients]
    
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }    
    return recipe

n = int(input("How many recipes would you like to enter? "))

# Blank space for easy reading
print("\n")

# Collect the recipes
for i in range(n):
    print(f"Recipe {i + 1}:")
    recipe = take_recipe()
    
    # Check each ingredient and add new ones
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)
    print("\n")


# Showing items which have difficulty
print("="*50)
print("RECIPE LIST")
print("="*50)

# Roam through dictionary(ies)
for recipe in recipes_list:
    # Calculate difficulty
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    # Displaying the recipe
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time (min): {recipe['cooking_time']}")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {difficulty}")

# Display all ingredients alphabetically
print("\n")
print("="*50)
print("INGREDIENTS AVAILABLE ACROSS ALL RECIPES")
print("="*50)

ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)