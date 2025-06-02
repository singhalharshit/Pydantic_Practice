from pydantic import BaseModel, field_validator, model_validator,computed_field


class User(BaseModel):
    username:str

    @field_validator('username')
    def username_length(cls,v):
        if len(v)<4:
            raise ValueError("UserName must be atleast 4 characters")
        return v
    
    # Field_validators are run before pydantic as we can see that it is very obvious


class SingupData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Password doesnot matches")
        return values
    
    
class Product(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self)-> float:
        return self.price * self.quantity
    
"""
In this part, we are learning how to add custom checks (validations) to our data.

@field_validator is used when we want to check or control the value of one specific field (like checking if a username is long enough).

@model_validator is used when we want to check multiple fields together (like checking if password and confirm password match). The option mode="after" means the check will run after all fields are filled. We can also use mode="before" if we want to clean or change the data before it's used.

Now you may ask — if we already use Field(...) to set rules, why do we need these validators? The answer is: Field is great for simple rules like minimum length or value, but when we need more complex logic, we use @field_validator or @model_validator.

Lastly, @computed_field is used when we want to show a value that is calculated using other fields — like showing the total price by multiplying price and quantity. It works with @property to add this as a new field in our output.

"""