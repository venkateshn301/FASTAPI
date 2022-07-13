from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional
from uuid import UUID


app = FastAPI()

class Book(BaseModel):
    id:UUID
    title: str = Field(min_length=1) # Data validation
    author: str = Field(min_length=1,max_length=100)
    description: Optional[str] = Field(title="Description of the book",min_length = 1,max_length=100)
    rating : int = Field(gt=-1,lt=101)


Books = []

@app.get("/")
async def read_all_books():
    if len(Books)<=0:
        create_books_no_api()
    return Books

@app.post("/createbook")
async def create_book(book:Book):
    Books.append(book)
    return book

#How to add books to book list when BOOKS list is empty

def create_books_no_api():
    book1 = Book(id="7adfeeec-6a3f-437a-8d19-2743c4edb9f4",
    title = "Computers",
    author = "Charless",
    description= "Description1",
    rating= 90)
    book2 = Book(id="7adfeeec-6a3f-437a-8d19-2743c4edb9f5",
    title = "Maths",
    author = "Venkat",
    description= "Description1",
    rating= 99)
    book3 = Book(id="7adfeeec-6a3f-437a-8d19-2743c4edb9f6",
    title = "Python",
    author = "GVANR",
    description= "Description1",
    rating= 100)

    Books.append(book1)
    Books.append(book2)
    Books.append(book3)

# Get books by passing UUID
@app.get("/books/book_id")
async  def read_book_by_id(book_id:UUID):
    for x in Books:
        if x.id == book_id:
            return x
    return {"Message":"UUID not matched"}

# update book by passing id
@app.put("/{book_id}")
async  def update_book(book_id:UUID,book:Book):
    count =0
    for x in Books:
        count += 1
        if x.id == book_id:
            Books[count-1] = book
        return Books[count-1]

# Delete book
@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter =0
    for x in Books:
        counter +=1
        if x.id == book_id:
            del Books[counter -1]
            return f'Deleted book id is {x.id}'