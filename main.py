
from fastapi import Form
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RegisterSchema(BaseModel):
    username:  str
    password: str


@app.post("/home")
async def home():
    return {"message": "Welcome to Twitter"}



@app.post("/login/")
async def login():
    return{"login":"enter your login details here"}

## Twitter signup form ##

@app.post("/signup/")
async def signup(name: str = Form(...),
 emailaddress: str = Form(...), 
 Dateofbirth: str = Form(...),
 phonenumber: int = Form(...)):
        if len(phonenumber) != 10:
     return {"message": "Phone number must be 10 digits"}
    return {"name": name, 
    "emailaddress": emailaddress, 
    "Dateofbirth": Dateofbirth, 
    "phonenumber": phonenumber
    }







