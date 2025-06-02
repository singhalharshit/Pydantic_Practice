from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    street:str
    city:str
    postal_code:str


class User(BaseModel):
    id:int
    name:str
    address:Address #this is called nested model referencing


class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']] = None # Self referencing model / Forward referencing

Comment.model_rebuild() # This is mandatory as when we are doing Forward Referencing we need to rebuild the class 


address = Address(street="123 something", city="Jaipur",postal_code="10001")
user = User(id=1, name="Harshit",address=address)
comment = Comment(id=1,content="something something",replies=[Comment(id=2,content="second value")])

