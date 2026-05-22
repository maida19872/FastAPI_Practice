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

from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()
books = []

class Book(BaseModel):
    id:int
    title:str
    author_name:str

@app.post("/add_a_new_book")
def add_book(book:Book):
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }


@app.get("/get_all_books")
def get_all_books():
    return {
        "message": "Books retrieved successfully",
        "books": books
    }

@app.get("/get_book/{id}")
def get_book(id:int):
    for book in books:
        if book.id == id:
            return book
    return {"message": "Book not found"}

@app.put("/update_book/{id}")
def update_book(id:int, updated_book:Book):
    for book in books:
        if book.id == id:
            book.title = updated_book.title
            return {"message": "Book updated successfully", "book": book}
    return {"message": "Book not found"}

@app.delete("/remove_book/{id}")
def delete_book(id:int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return {"message": "Book removed successfully", "book": book}
    return {"message": "Book not found"}

@app.get("/get_books_by_author/{author_name}")
def get_book_by_author_name(author_name: str):
    author_books = []
    for book in books:
        if book.author_name == author_name:
            author_books.append(book)
    if author_books:
        return {"message": "Books found","books": author_books}
    return {"message": "Book not found"}