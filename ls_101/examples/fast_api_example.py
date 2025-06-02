from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app= FastAPI()

class UserSignUp(BaseModel):
    username:str
    email:EmailStr
    password:str

class Settings(BaseModel):
    app_name:str = "Default app"
    admin_email: str = "admin@gmail.com"


def get_settings():
    return Settings()


@app.post('/signup')
def signup(user:UserSignUp):
    return {"message":f"user {user.username} signed up"}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings