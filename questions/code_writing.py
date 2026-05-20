Question 1.
# Create a GET API /users that returns:
# {"message": "Users API"}
@app.get("/users")
def get_users():
    return {"message": "Users API"}

Question 2.
# Create a path parameter called id in:
# /products/{id}
@app.get("/products/{id}")
def get_products(id:int):
    return {"id": id}

Question 3.
# Write a query parameter called limit with default value 5.
@app.get("/items")
def get_items(limit:int=5):
    return{"limit":limit}

Question 4.
# Create a Pydantic model named Student having:
# name (str)
# age (int)
from pydantic import BaseModel
class Student(BaseModel):
    name:str
    age:int

Question 5.
# Write a POST API /students that receives a Student model.
@app.post("/students")
def create_student(student:Student):
    return student


Question 6.
# Write code to append a new dictionary into:
# students = []
students = []
@app.post("/students")
def add_student(student:dict):
    students.append(student)
    return student

Question 7.
# Write a DELETE API that deletes a product using product ID.
@app.delete("/product/{product_id}")
def delete_product(product_id:int):
    return {"message": f"Product with ID {product_id} has been deleted successfully."}
    

Question 8.
# Write a GET API that returns only recipes whose ingredients contain "tomato".
@app.get("/recipes")
def get_recipes():
    recipes = [
        {"name": "Pasta", "ingredients": ["tomato", "basil", "garlic"]},
        {"name": "Salad", "ingredients": ["lettuce", "cucumber", "tomato"]},
        {"name": "Soup", "ingredients": ["carrot", "onion", "celery"]}
    ]
    tomato_recipes = [recipe for recipe in recipes if "tomato" in recipe["ingredients"]]
    return tomato_recipes


Question 9.
# Write a PUT API route for updating a user using user_id.
@app.put("/users/{user_id} ")
def update_user(user_id:int, user:dict):
    return{"user_id": user_id, "user": user}

Question 10.
# Write a response model in this API:
# @app.get("/books", response_model=__________)
@app.get("/books", response_model=list[dict]) 
