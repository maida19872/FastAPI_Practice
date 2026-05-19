from fastapi import FastAPI
from questions.q1 import router 
from questions.q2 import router as student_router
from questions.q3 import router as recipe_router

app = FastAPI() 

app.include_router(router, prefix="/q1", tags=["Books"])
app.include_router(student_router, prefix="/q2", tags=["Students"])
app.include_router(recipe_router, prefix="/q3", tags=["Recipes"])

