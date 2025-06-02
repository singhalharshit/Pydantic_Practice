from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id:int
    name:str = Field(...,min_length=3,description="Employee_Name") # Field(...): Means this field is required (same as required=True)
    department: Optional[str] = 'General'

    # email:Optional[str] = Field(min_length=5) # **IMPORTANT => even if you keep a parameter as optional like in this case email but pass Field into it even without (...) you need to pass email into your input else this will fail giving the error. To handle we need to pass default= None

    email: Optional[str] = Field(default=None, min_length=5)
    salary:float = Field(..., ge=10000) #ge= it stands for greater than 

input_data = {'id':101,'name':'Harsh','salary':110000}

user_input = Employee(**input_data)
print(user_input)


# So now what is Field into Pydantic - Wherever we have conditions with our case like name should be atleast greater than 3 characters and salary should be greater than 10000 into these types of case we use Field. Into this (...) The triple dots represent that the Field or the parameter is necessary to pass. It can't be optional. 