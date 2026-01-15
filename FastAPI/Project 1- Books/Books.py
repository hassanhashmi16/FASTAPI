from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "isbn": "9780061120084"},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "isbn": "9780451524935"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Classic", "isbn": "9780743273565"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance", "isbn": "9780141439518"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "isbn": "9780547928227"}
]


@app.get("/api-endpoint")
async def read_all_books():
    return BOOKS



@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

