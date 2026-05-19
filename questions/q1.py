# Question 1 — Book Management System
# Create a FastAPI application for a Book Management System using Python lists/dictionaries for storage.

# Your API should include:
# Add a new book
# Get all books
# Get a single book using ID
# Update a book
# Delete a book

# Requirements:
# Use FastAPI decorators properly
# Use path parameters where needed
# Use Pydantic models
# Add type hints
# Return proper messages if a book is not found

from fastapi import APIRouter   
from pydantic import BaseModel

router=APIRouter()
books = []

class Book(BaseModel):
    id:int
    title:str

@router.post("/books")
def add_book(book:Book):
    books.append(book)
    return book

@router.get("/books")
def get_all_books():
    return books

@router.get("/books/{id}")
def get_book(id:int):
    for book in books:
        if book.id == id:
            return book
    return {"message": "Book not found"}

@router.put("/books/{id}")
def update_book(id:int, updated_book:Book):
    for book in books:
        if book.id == id:
            book.title = updated_book.title
            return book
    return {"message": "Book not found"}

@router.delete("/books/{id}")
def delete_book(id:int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return book
    return {"message": "Book not found"}