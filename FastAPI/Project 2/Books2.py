from typing import Optional

from fastapi import FastAPI , Path , Query , HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title : str
    author : str
    desc : str
    rating : int
    published_date : int

    def __init__(self , id , title , author , desc , rating , published_date):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID iss not needed on create" , default=None)
    title : str = Field(min_length=1)
    author : str = Field(min_length=2)
    desc : str = Field(min_length=3)
    rating : int = Field(gt=0 , lt =6)
    published_date : int = Field(gt= 0 , lt=2030)

    model_config = {
        "json_schema_extra" : {
            "example" : {
                "title" :"Book title",
                "author" : "Author name",
                "desc" : "Description",
                "rating" : "5" ,
                "published_date" : "2000"
            }
        }
    }
BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book about core CS concepts", 5 , 2003),
    Book(2, "Python for Humans", "Jane Doe", "A beginner-friendly guide to Python programming", 4 , 2003),
    Book(3, "FastAPI in Action", "Sebastian Ramirez", "Build high-performance APIs with FastAPI", 5 , 2002),
    Book(4, "Clean Code Explained", "Robert C. Martin", "Practical techniques for writing clean, readable code", 5 , 2004),
    Book(5, "The Bug Hunter", "Alex Morgan", "A deep dive into debugging and problem solving", 4 , 2005),
    Book(6, "Algorithms Made Easy", "Sarah Lin", "Simplified explanations of common algorithms", 4 , 2020),
    Book(7, "The Dev Mindset", "Chris Walker", "How developers think, learn, and grow", 3 , 2012),
    Book(8, "Databases Demystified", "Emily Stone", "Understanding SQL and NoSQL databases", 4 , 2004),
    Book(9, "System Design Basics", "Rahul Mehta", "An introduction to scalable system design", 5 , 2009),
    Book(10, "Async Programming with Python", "Nina Patel", "Mastering concurrency and async patterns", 4 , 2025),
]


@app.get("/book", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/get-books-by-rating")
async def read_book(book_rating : int = Query(gt = 0, lt=6)):
    books_to_be_returned = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_be_returned.append(book)
    return books_to_be_returned

@app.get("/books/get-books-by-published-date" , status_code=status.HTTP_200_OK)
async def read_book(published_date : int = Query(gt= 0 , lt=2030)):
    books_to_be_returned = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_be_returned.append(book)
    return books_to_be_returned


@app.get("/books/{book_id}")
async def read_book_by_id(book_id : int = Path(gt =0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404 , detail="Book not found" )




@app.post("/create-book" , status_code=status.HTTP_201_CREATED)
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id((new_book)))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) > 0 else 0
    return book

@app.put("/books/update_book" , status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not Found")

@app.delete("/books/delete_book/{book_id}" , status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id : int=Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not Found")