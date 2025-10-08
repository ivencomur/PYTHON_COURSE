import pickle

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

def search_ingredient(data):
    """Search for recipes by ingredient"""
    # Grab the list of all ingredients from data dictionary
    all_ingredients = data['all_ingredients']
    
    # Show the user all ingredients with a number next to each one
    print("\nAvailable ingredients:")
    print("-" * 30)
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}: {ingredient}")
    print("-" * 30)
    
    try:
        # Ask user to pick a number
        choice = int(input("\nEnter the number of the ingredient you want to search for: "))
        # Use that number to grab the ingredient from the list
        ingredient_searched = all_ingredients[choice]
        
    except ValueError:
        # In case they typed text instead of a number
        print("Error: Please enter a valid number.")
        return  # Exit the function early
        
    except IndexError:
        # In case they typed a number that's too big (like 99 when there's only 10 items)
        print("Error: That number is not in the list.")
        return  # Exit the function early
        
    except:
        # Something else (strange) happened
        print("An unexpected error occurred.")
        return  # Yes, this exits the function early
        
    else:
        # Everything worked, now find recipes with a certain ingredient from input
        print(f"\nRecipes containing '{ingredient_searched}':")
        print("=" * 50)
        
        found_recipes = False
        
        # Loop through every recipe in the known data
        for recipe in data['recipes_list']:
            # Check if the ingredient we're looking for is in this particular recipe
            if ingredient_searched in recipe['ingredients']:
                # Show this recipe
                display_recipe(recipe)  
                found_recipes = True  
        
        # If no recipes found with this ingredient
        if not found_recipes:
            print(f"No recipes found with {ingredient_searched}.")


# Main code starts here
filename = input("Enter the filename where your recipes are stored: ")

try:
    # Try to open the file and load the pickled data
    # 'rb' = read binary
    file = open(filename, 'rb')
    # Turn the pickle back into a dictionary  
    data = pickle.load(file)  
    
except FileNotFoundError:
    # File doesn't exist
    print(f"Error: File '{filename}' not found. Make sure you've run recipe_input.py first!")
    
except:
    # Something else is wrong
    print("An unexpected error occurred while trying to read the file.")
    
else:
    # File loaded successfully! Now let's search
    file.close()
    # Call our search function  
    search_ingredient(data)