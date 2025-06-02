from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool = True # This is the way we define the default value



