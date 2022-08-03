from fastapi import FastAPI,HTTPException,Request,status,Form,Header
from pydantic import BaseModel,Field
from typing import Optional
from uuid import UUID
from starlette.responses import JSONResponse

app = FastAPI()

class NegativeNumberException(Exception):
    def __int__(self,books_to_return):
        self.books_to_Return = books_to_return


class Book(BaseModel):
    id:UUID
    title: str = Field(min_length=1) # Data validation
    author: str = Field(min_length=1,max_length=100)
    description: Optional[str] = Field(title="Description of the book",min_length = 1,max_length=100)
    rating : int = Field(gt=-1,lt=101)

    class Config:
        schema_extra = {
                        "example":{"id":"12345678-1234-1234-1234-123456789abc",
                                   "title":"computer s pro",
                                   "author":"vekat",
                                   "description":" A very nice book",
                                   "rating":75 }}


Books = []

#custom HTTP exceptions

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request:Request,
                                            exception:NegativeNumberException):
    return JSONResponse(status_code=418,
                        content={"message":f"Hey why do you want {exception.books_to_Return}"
                                            f"books? You need to read more!"})


@app.get("/ReadAllBook")
async  def read_all_books(books_to_return:Optional[int]=None):
    print("The number of books:",books_to_return)

    if books_to_return and books_to_return<0:
        raise NegativeNumberException(books_to_return = books_to_return)
    if len(Books)<1:
        create_books_no_api()
    if books_to_return and len(Books) >=books_to_return>0:
        i=1
        new_books = []
        while i <= books_to_return:
            new_books.append(Books[i-1])
            i += 1
        return new_books
    return Books

@app.get("/")
async def read_all_books():
    if len(Books)<=0:
        create_books_no_api()
    return Books

@app.post("/createbook",status_code=status.HTTP_201_CREATED)
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
    raise item_canot_befound_exception()

# update book by passing id
@app.put("/{book_id}")
async  def update_book(book_id:UUID,book:Book):
    count =0
    for x in Books:
        count += 1
        if x.id == book_id:
            Books[count-1] = book
        return Books[count-1]
    raise item_canot_befound_exception()

# Delete book
@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter =0
    for x in Books:
        counter +=1
        if x.id == book_id:
            del Books[counter -1]
            return f'Deleted book id is {x.id}'
    raise item_canot_befound_exception()

def item_canot_befound_exception():
    return HTTPException(status_code=404,
                         detail="Book not found!",
                         headers={"X-Header_Error":"Nothing to be seen at the UUID"})


#Form Field example
@app.post("/book/login")
async def book_login(username:str = Form(),password:str = Form()):
    return {"Username":username,"Password":password}
#Headers
@app.get("/header")
async def read_header(random_header:Optional[str]=Header(None)):
    return {"Read-Header": random_header}
#Assignment for

@app.post("/book/login/")
async def book_login_bookid(book_id:int,username:Optional[str] = Header(None),password:Optional[str] = Header(None)):
    if username == "FastAPIUser" and password == "Welcome@2022":
        return Books[book_id]
    return "Invalid Details"
