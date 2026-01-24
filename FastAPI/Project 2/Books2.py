from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
app = FastAPI()

class Book:
    id: int
    title : str
    author : str
    desc : str
    rating : int

    def __init__(self , id , title , author , desc , rating):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID iss not needed on create" , default=None)
    title : str = Field(min_length=1)
    author : str = Field(min_length=2)
    desc : str = Field(min_length=3)
    rating : int = Field(gt=0 , lt =6)

    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" :"Book title",
                "author" : "Author name",
                "desc" : "Description",
                "rating" : "5"
            }
        }
    }
BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book about core CS concepts", 5),
    Book(2, "Python for Humans", "Jane Doe", "A beginner-friendly guide to Python programming", 4),
    Book(3, "FastAPI in Action", "Sebastian Ramirez", "Build high-performance APIs with FastAPI", 5),
    Book(4, "Clean Code Explained", "Robert C. Martin", "Practical techniques for writing clean, readable code", 5),
    Book(5, "The Bug Hunter", "Alex Morgan", "A deep dive into debugging and problem solving", 4),
    Book(6, "Algorithms Made Easy", "Sarah Lin", "Simplified explanations of common algorithms", 4),
    Book(7, "The Dev Mindset", "Chris Walker", "How developers think, learn, and grow", 3),
    Book(8, "Databases Demystified", "Emily Stone", "Understanding SQL and NoSQL databases", 4),
    Book(9, "System Design Basics", "Rahul Mehta", "An introduction to scalable system design", 5),
    Book(10, "Async Programming with Python", "Nina Patel", "Mastering concurrency and async patterns", 4),
]


@app.get("/book")
async def read_all_books():
    return BOOKS

@app.get("/books/get-books-by-rating")
async def read_book(book_rating : int):
    books_to_be_returned = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_be_returned.append(book)
    return books_to_be_returned

@app.get("/books/{book_id}")
async def read_book_by_id(book_id : int):
    for book in BOOKS:
        if book.id == book_id:
            return book



@app.post("/create-book")
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id((new_book)))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) > 0 else 0
    return book