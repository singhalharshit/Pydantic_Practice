from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    name: str
    is_active:bool

# input_data = {'user_id':101,'name':'dummyName','is_active':True}
input_data = {'user_id':'101','name':'dummyName','is_active':'True'}


user = User(**input_data)
print(user)

# So now into this case on line 9 you can see that user_id is defined as int but you passed '101' and same with is_active which is set to bool but we have passed 'bool' since we have used pydantic it's the job of Pydantic to handle it all since '101' can be converted to string Pydantic converted it for us. 


