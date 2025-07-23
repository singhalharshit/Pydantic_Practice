# Pydantic -> Annotated and Field functions to be discussed majorly

"""
from pydantic import BaseModel,EmailStr,AnyUrl ,Field
from typing import List,Dict,Optional,Annotated


# Why do we import typing when we have list and Dict in pydantic also, that is because when we do list from pydantic it goes only to list and check if the data is in list but we wanted to check if the data inside the list is also of our type which is str. So that's why we bring Dict and list from typing  

# Field function is majorly used for attaching meta data also not just for data validation. For this we also need annotated from typing so it's the combo of both. We can see it in the name field 

class Patient(BaseModel):
    name:str= Annotated[str,Field(max_length=50, title='Name of the Patient', description='Give the name of the patient under 50 characters',examples=['Hemant','Shubham'],default='XYZ')]
    email: EmailStr # This is a custom datatype given by pydantic inorder to save email for further data validation
    url: AnyUrl # This is a custom datatype given by pydantic validate URL so instead of making if else logic and Regex and all you can simply use AnyUrl
    age:int = Field(ge=0, lt=120)
    weight:float = Field(ge=0) # So here we had made a constraint where we said that weight should be greater than 0
    married: Optional[bool] = None
    allergies:List[str] = Field(max_length=5)
    contact_detials: Dict(str,str)



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)


patient_info= {'name':'somename','age':'30'}
patient_1 = Patient(**patient_info)

"""


"""
# Field_Validator


from pydantic import BaseModel,EmailStr,AnyUrl ,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name:str= Annotated[str,Field(max_length=50, title='Name of the Patient', description='Give the name of the patient under 50 characters',examples=['Hemant','Shubham'],default='XYZ')]
    email: EmailStr
    url: AnyUrl 
    age:int = Field(ge=0, lt=120)
    weight:float = Field(ge=0) 
    height:float
    married: Optional[bool] = None
    allergies:List[str] = Field(max_length=5)
    contact_detials: Dict[str,str]


    # Field Validator operates in two mode : before and after

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com','icici.com']
        domain_name = value.split('@')
        if domain_name not in valid_domains:
            raise ValueError('Not a Valid Domain')

        return value

    # Wanting our username to be in capital
    @field_validator
    @classmethod
    def name_check(cls,value):
        return value.upper()
     
    # When one needs to validate more than one field say if the age is >60 then we need an emergency contact else we will not create that patient
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older than 60 mush have an emergency contact")
        return model
    

    # Computed Field
    @computed_field
    @property
    def calc_BMI(self) -> float:
        bmi = self.weight/((self.height**2),2)
        return bmi
    
"""

# def insert_patient_data(patient:Patient):
#     print(patient.name)
#     print(patient.age)



"""

# Nested_models
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:str




class Patient_new(BaseModel):
    name:str
    gender:str
    age:int
    address: Address





address_dict = {'city':'Gurgoan','state':'Haryana','pincode':'122001'}
address1 = Address(**address_dict)

patient_dict ={'name':'xyz','gender':'Male','age':35,'address':address1}

Patient_1= Patient_new(**patient_dict)

print(Patient_1)

"""



# Exporting Pydantic models in form of dict


from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:str




class Patient_new(BaseModel):
    name:str
    gender:str
    age:int
    address: Address


address_dict = {'city':'Gurgoan','state':'Haryana','pincode':'122001'}
address1 = Address(**address_dict)

patient_dict ={'name':'xyz','gender':'Male','age':35,'address':address1}

Patient_1= Patient_new(**patient_dict)

temp = Patient_1.model_dump()
