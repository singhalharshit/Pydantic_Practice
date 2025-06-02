from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime
 

class Address(BaseModel):
    street:str
    city:str
    zip_code:str


class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool = True
    createdAt:datetime
    address:Address # ✅ Nested Pydantic model
    tags:List[str]=[]

    # model_config is used to customize serialization behavior
    # Here, we define how to format datetime objects when we convert the model to JSON
    model_config = ConfigDict(json_encoders={datetime :lambda v:v.strftime('%d-%m-%Y %H:%M:%S')})

# create a user instance

user= User(id=1,name= "Harshit",email="harshit@gmail.com",is_active=True,createdAt=datetime(2025,3,15,13,20),address=Address(street="123 something something", city="Varanasi", zip_code="201305"),tags=["premium","subscriber"])

# Convert the Pydantic model to a Python dictionary using model_dump()
# This returns a standard Python dict — good for further processing within Python
python_dict = user.model_dump()
# print(python_dict)  # Uncomment if you want to see the dictionary output

# Convert the Pydantic model to a JSON string using model_dump_json()
# This respects the json_encoders configuration, so the datetime field is now formatted
json_str = user.model_dump_json()
print(json_str)  # Outputs a string, ready to be sent over API or saved as .json file

# 🔍 Major change:
# The `createdAt` datetime will appear in the formatted style like: "15-03-2025 13:20:00"
# instead of the default ISO format like: "2025-03-15T13:20:00"