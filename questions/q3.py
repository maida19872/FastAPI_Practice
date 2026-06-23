# Question 3 — Recipe Management API
# Create a FastAPI project for recipes.

# Each recipe should contain:
# id
# recipe_name
# ingredients
# cooking_time

# Tasks:
# Create CRUD APIs
# Create a GET API that returns only recipes containing "tomato" in ingredients
# Use query parameters for filtering recipes
# Use response models
# Handle invalid data types properly

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
recipes = []

class Recipe(BaseModel):
    id: int
    recipe_name: str
    ingredients: list
    cooking_time: int

@app.post("/add_recipes")
def create_recipe(recipe: Recipe):
    recipes.append(recipe)
    return recipe

@app.get("/recipes_by_ingredient")
def get_recipes(ingredient: str = None):
    if ingredient:
        return [recipe for recipe in recipes if ingredient in recipe.ingredients]
    return recipes

@app.get("/recipes_by_id/{id}")
def get_recipe(id: int):
    for recipe in recipes:
        if recipe.id == id:
            return recipe
    return {"message": "Recipe not found"}

@app.put("/recipes_updated/{id}")
def update_recipe(id: int, updated_recipe: Recipe):
    for recipe in recipes:
        if recipe.id == id:
            recipe.recipe_name = updated_recipe.recipe_name
            recipe.ingredients = updated_recipe.ingredients
            recipe.cooking_time = updated_recipe.cooking_time
            return recipe
    return {"message": "Recipe not found"}

@app.delete("/delete_recipe_by_id/{id}")
def delete_recipe(id: int):
    for recipe in recipes:
        if recipe.id == id:
            recipes.remove(recipe)
            return {"message": "Recipe deleted successfully"}
    return {"message": "Recipe not found"}