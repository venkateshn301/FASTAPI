from fastapi import FastAPI,Depends,HTTPException
import models
from database import engine,sessionLocal
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel,Field

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

class Todo(BaseModel):
    title : str
    description:Optional[str]
    priority: int = Field(gt=0,lt=6,description='The priority between 1-5')
    complete: bool

def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def read_records(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@app.get("/todos/{todos_id}")
async def read_data_y_id(todos_id: int ,db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todos_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()


@app.post("/")
async def create_record(todo: Todo,db:Session = Depends(get_db)):
    todo_models = models.Todos()
    todo_models.title = todo.title
    todo_models.description = todo.description
    todo_models.priority = todo.priority
    todo_models.complete = todo.complete
    db.add(todo_models)
    db.commit()

    return successful_response(201)

@app.put("/{todo_id}")
async def update_record(todo_id:int, todo:Todo,db:Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id==todo_id).first()
    try:
        if todo_model is None:
            raise http_exception()
        todo_model.title = todo.title
        todo_model.description = todo.description
        todo_model.priority = todo.priority
        todo_model.complete = todo.complete

        db.add(todo_model)
        db.commit()

        return successful_response(200)
    finally:
        db.close()

@app.delete("/{todo_id}")
async def delete_record(todo_id: int,db:Session  = Depends(get_db)):
    try:

        todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
        if todo_model is None:
            raise http_exception()
        db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
        db.commit()
        return successful_response(200)
    finally:
        db.close()

def successful_response(status_code):
    return {
        'status_code': status_code,
        'transaction': 'successful'
    }
def http_exception():
    return HTTPException(status_code = 404, detail = "Model Item is not Found")


