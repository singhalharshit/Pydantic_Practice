from pydantic import BaseModel
from typing import List,Dict


# Why do we import typing when we have list and Dict in pydantic also, that is because when we do list from pydantic it goes only to list and check if the data is in list but we wanted to check if the data inside the list is also of our type which is str. So that's why we bring Dict and list from typing  


class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married: bool
    allergies:List[str]
    contact_detials: Dict(str,str)



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)


patient_info= {'name':'somename','age':'30'}
patient_1 = Patient(**patient_info)