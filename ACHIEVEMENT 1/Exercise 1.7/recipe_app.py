from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql://cf-python:password@localhost/task_database")
Base = declarative_base()


class Recipe(Base):
    __tablename__ = "final_recipes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}>"
    
    def __str__(self):
        return f"""
{'='*50}
Recipe: {self.name}
{'='*50}
Cooking Time: {self.cooking_time} minutes
Difficulty: {self.difficulty}
Ingredients: {self.ingredients}
{'='*50}
"""
    
    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(", ")
        num_ingredients = len(ingredients_list)
        
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return self.ingredients.split(", ")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def create_recipe():
    name = input("Enter recipe name: ")
    
    try:
        cooking_time = int(input("Enter cooking time (minutes): "))
    except ValueError:
        print("Error: Cooking time must be a number.")
        return
    
    try:
        num_ingredients = int(input("How many ingredients? "))
    except ValueError:
        print("Error: Must be a number.")
        return
    
    ingredients = []
    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    
    ingredients_str = ", ".join(ingredients)
    
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients_str
    )
    
    recipe_entry.calculate_difficulty()
    
    session.add(recipe_entry)
    session.commit()
    
    print(f"\n✓ Recipe '{name}' added successfully!")


def view_all_recipes():
    recipes = session.query(Recipe).all()
    
    if not recipes:
        print("\nNo recipes found in database.")
        return
    
    print(f"\n{'='*60}")
    print(f"ALL RECIPES ({len(recipes)} total)")
    print(f"{'='*60}\n")
    
    for recipe in recipes:
        print(recipe)


def search_by_ingredients():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("\nNo recipes in database.")
        return
    
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    try:
        choices = input("\nEnter ingredient numbers (space-separated): ").split()
        choice_indices = [int(choice) - 1 for choice in choices]
    except ValueError:
        print("Error: Invalid input.")
        return
    
    search_ingredients = []
    try:
        for index in choice_indices:
            search_ingredients.append(all_ingredients[index])
    except IndexError:
        print("Error: Invalid ingredient number.")
        return
    
    conditions = []
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    recipes = session.query(Recipe).filter(*conditions).all()
    
    if recipes:
        print(f"\n{'='*60}")
        print(f"FOUND {len(recipes)} RECIPE(S)")
        print(f"{'='*60}\n")
        for recipe in recipes:
            print(recipe)
    else:
        print("\nNo recipes found with those ingredients.")


def edit_recipe():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("\nNo recipes to edit.")
        return
    
    recipes = session.query(Recipe).all()
    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")
    
    try:
        recipe_id = int(input("\nEnter recipe ID to edit: "))
    except ValueError:
        print("Error: ID must be a number.")
        return
    
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    if not recipe_to_edit:
        print("Error: Recipe not found.")
        return
    
    print(f"\nEditing: {recipe_to_edit.name}")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Cooking Time: {recipe_to_edit.cooking_time}")
    print(f"3. Ingredients: {recipe_to_edit.ingredients}")
    
    choice = input("\nWhich field to update (1-3)? ")
    
    if choice == "1":
        new_name = input("Enter new name: ")
        recipe_to_edit.name = new_name
    
    elif choice == "2":
        try:
            new_time = int(input("Enter new cooking time: "))
            recipe_to_edit.cooking_time = new_time
            recipe_to_edit.calculate_difficulty()
        except ValueError:
            print("Error: Must be a number.")
            return
    
    elif choice == "3":
        try:
            num_ingredients = int(input("How many ingredients? "))
        except ValueError:
            print("Error: Must be a number.")
            return
        
        ingredients = []
        for i in range(num_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ")
            ingredients.append(ingredient)
        
        recipe_to_edit.ingredients = ", ".join(ingredients)
        recipe_to_edit.calculate_difficulty()
    
    else:
        print("Invalid choice.")
        return
    
    session.commit()
    print(f"\n✓ Recipe updated successfully!")


def delete_recipe():
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("\nNo recipes to delete.")
        return
    
    recipes = session.query(Recipe).all()
    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"{recipe.id}. {recipe.name}")
    
    try:
        recipe_id = int(input("\nEnter recipe ID to delete: "))
    except ValueError:
        print("Error: ID must be a number.")
        return
    
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    if not recipe_to_delete:
        print("Error: Recipe not found.")
        return
    
    print(f"\nAre you sure you want to delete '{recipe_to_delete.name}'?")
    confirm = input("Type 'yes' to confirm: ")
    
    if confirm.lower() == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print(f"\n✓ Recipe '{recipe_to_delete.name}' deleted successfully!")
    else:
        print("\nDeletion cancelled.")


def main_menu():
    while True:
        print("\n" + "="*60)
        print("RECIPE APP - MAIN MENU")
        print("="*60)
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("6. Exit")
        print("="*60)
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print("\nClosing session...")
            session.close()
            engine.dispose()
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()