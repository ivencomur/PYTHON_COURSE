class Recipe:
    # Class variable to track ALL ingredients across ALL recipes
    all_ingredients = []
    
    def __init__(self, name):
        #Initialize new recipe with a name
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        # recipes name after input
        return self.name
    
    def set_name(self, name):
         # recipes name after input
        self.name = name
    
    def get_cooking_time(self):
        # To return the cooking time
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        # To set cooking time
        self.cooking_time = cooking_time

    def add_ingredients(self, *ingredients):
        #Add multiple ingredients
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
    
    def get_ingredients(self):
        # Return list of ingredients
        return self.ingredients
    
    def update_all_ingredients(self):
        # Add this recipe's ingredients to the class-wide ingredient list
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def calculate_difficulty(self):
        # Calculate recipe difficulty upon cooking time and ingredients
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    
    def get_difficulty(self):
        # Show difficulty, calculating it if needed
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        #Search for ingredient in recipe
        return ingredient in self.ingredients
    
    def __str__(self):
        # Return a formatted string of recipe
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
    
def recipe_search(data, search_term):
    # Search for recipes containing particular (specific) ingredient
    print(f"\nRecipes containing '{search_term}':")
    print("="*50)
    
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Main code starts here
print("\n" + "="*50)
print("Creating Recipe Objects")
print("="*50)

# Create Tea recipe
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Water")
tea.set_cooking_time(5)
print(tea)

# Create Coffee recipe
coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
print(coffee)

# Create Cake recipe
cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
print(cake)

# Create Banana Smoothie recipe
banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
print(banana_smoothie)

# Bundle all recipes into a list
recipes_list = [tea, coffee, cake, banana_smoothie]

print("\n" + "="*50)
print("Searching for recipes by ingredient")
print("="*50)

# Search for recipes containing Water
recipe_search(recipes_list, "Water")

# Search for recipes containing Sugar
recipe_search(recipes_list, "Sugar")

# Search for recipes containing Bananas
recipe_search(recipes_list, "Bananas")
