from fastapi import FastAPI
from fastapi import Body

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

@app.post("/books/create_book/")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    return BOOKS

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

@app.get("/books/read_books_from_author/{author}")
async def read_books_from_author(author : str):
    books_to_be_returned = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_be_returned.append(book)
            return books_to_be_returned
@app.get("/books/read_books_from_author_using_query_params/")
async def read_books_from_author_using_query_params(author : str):
    books = []
    # for i in range(len(BOOKS)):
    #     if BOOKS[i].get('author').casefold() == author.casefold():
    #         books.append(BOOKS[i])
    # return books

    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books.append(book)
    return books