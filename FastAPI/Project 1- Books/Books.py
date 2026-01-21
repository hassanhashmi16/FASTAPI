from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "isbn": "9780061120084"},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Romance", "isbn": "9780451524935"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Classic", "isbn": "9780743273565"},
    {"title": "Pride and Prejudice", "author": "George Orwell", "year": 1813, "genre": "Romance", "isbn": "9780141439518"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "isbn": "9780547928227"}
]


@app.get("/api-endpoint")
async def read_all_books():
    return BOOKS



@app.get("/books/title/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book



@app.get("/book/")
async def read_all_books(genre: str):
    books_to_be_returned = []
    for book in BOOKS:
        if book.get('genre').casefold() == genre.casefold():
            books_to_be_returned.append(book)
    return books_to_be_returned

@app.get("/books/author/{book_author}/")
async def read_author_category_by_query(book_author: str , genre : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('genre').casefold() == genre.casefold():
            books_to_return.append(book)

    return books_to_return