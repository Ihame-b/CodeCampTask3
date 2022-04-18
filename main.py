from atexit import register
import email
from sqlite3 import Date
from typing import Optional
from fastapi import FastAPI, Form
from phonenumbers import PhoneNumber
from pydantic import BaseModel, EmailStr

app = FastAPI()

class TwiterRegistration(BaseModel):
    Names: str
    Phone: str
    Email: EmailStr
    DateOfBirth: Date
    
@app.post("/register/") 
# async def create_account(register: TwiterRegistration):
#     return create_account
async def create_account(Names: str= Form(...), Phone: str=Form(...), Email: EmailStr=Form(...), DateOfBirth: Date=Form(...)):
    return {"You Twiter Account created succesfull Here is your detail : Name: ":Names, "DOB is ":DateOfBirth, " Your Email is ":Email, "Phone number is ":Phone}
