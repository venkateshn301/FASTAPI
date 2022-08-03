from typing import Optional,List,Union
from datetime import datetime
from pydantic import BaseModel

class Person_Info(BaseModel):
    id: int
    name:str
    signup_ts: Union[datetime,None] = None
    friends: List[int]

class Item(BaseModel):
    Name: str
    Price: float
    Description: Union[str,None]=None
    tax: Union[float,None] = None


external_Data = {"id":1110,
                 "name":"Venkatesh",
                 "signup_ts":"2017-06-01 12:22",
                 "friends": [1, "2", b"3"]}


def display(name:Optional[str]=None):
    if name is not None:
        print(f'The dispaly name is {name}')
    else:
        print("Hello")

class Example:
    def __int__(self,name:str):
        self.name = name

def sample(stringobject:Example):
    print(stringobject)
    return stringobject

#sample("venkatesh")

pobj = Person_Info(**external_Data)
#print(pobj.id)
#display()

from fastapi import FastAPI

app = FastAPI()

@app.post("/Item")
async def create_item(item:Item):
    item.Name.capitalize()
    return item
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#passing multiple query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int,item_id:str,q:Union[str,None] = None,short:bool = False):
    item = {"item_id": item_id,"Owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is good!"})
    return item


from fastapi import FastAPI,Path,Form,Request,Query


@app.get("/items/{item_id}")
async def read_items_path(item_id:int = Path(title="The is path parameter"),
                          q:Union[str,None]= Query(default=None,alias="Item-query")):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results
#Multiple Body parameters

class User(BaseModel):
    first_name: str
    full_name: Union[str,None] = Query(default=None)


@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item,user:User):
    result = {"item_id": item_id,"item":item,"user":user}
    return result
#Depricating parameters

@app.get("/items/")
async def read_items(q:Union[str,None]=Query(default=None,
                                             alias="Item-query",
                                             title="Query String",
                                             min_length=3,
                                             max_length=50,
                                             regex="^fixedquery$",
                                             deprecated=True)):
    result = {"items":[{"item_id": "foo"},{"item_id": "bar"}]}
    if q:
        result.update({"q":q})
    return result


