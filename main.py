from fastapi import FastAPI
from enum import Enum
app = FastAPI()

Books = {'book_1':{'title':'title one','author':'author one'},
		 'book_2':{'title':'title two','author':'author two'},
		 'book_3':{'title':'title three','author':'author three'},
		 'book_4':{'title':'title four','author':'author four'},
		 'book_5':{'title':'title five','author':'author five'}}

@app.get("/{book_name}")
def read_all_books(bookname):
	return  Books[bookname]

@app.get("/")
async def read_all_books():
    return Books
class Directions(str,Enum):
	north = "North"
	south = "South"
	east = "East"
	west = "West"

@app.get("/directions/{directionname}")
async def directions(directionname: Directions):
	if directionname == Directions.north:
		return {"directionname":directionname,"sub":"right"}
	if directionname == Directions.west:
		return {"directionname":directionname,"sub":"up"}
	if directionname == Directions.east:
		return {"directionname":directionname,"sub":"down"}
	if directionname == Directions.south:
		return {"directionname":directionname,"sub":"left"}

@app.get("/books/{book_name}")
async def read_book_name(book_name: str):
	return {"My Book Name is":book_name}
@app.get("/books/{book_id}")
async def read_book_id(book_id: int):
	return {"My Book Id is":book_id}


@app.post("/")
async def create_book(title,author):
	current_book_id =0
	if len(Books)>0:
		for book in Books:
			x= int(book.split('_',)[-1])
			if current_book_id<x:
				current_book_id =x
	Books[f'book_{current_book_id + 1 }']={'title':title,'author':author}
	return Books[f'book_{current_book_id + 1}']
@app.put("/{book_name}")
async def update_book(book_name:str,book_title:str,book_author:str):
	book_info = {"title":book_title,"author":book_author}
	Books[book_name] = book_info
	return  book_info

@app.delete("/{book_name}")
async def delete_book(book_name:str):
	del Books[book_name]
	return f'The {book_name} has been deleted!'

#Query parameters

@app.get("/assignments/")
async def read_book(book_name:str):
	return Books[book_name]

@app.delete("/assignment/")
async def delete_book(book_name:str):
	del Books[book_name]
	return Books





