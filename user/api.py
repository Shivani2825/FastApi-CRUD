from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from fastapi_login import LoginManager
# from fastapiencoders import jsonable_encoder
# from fastapi.security import OAuth2PasswordRequestForm

from fastapi import FastAPI
from fastapi import APIRouter
from . models import *
# from user.pydantic_models import createuser,loginuser,Token,updateuser,deleteuser
from passlib.context import CryptContext


router =APIRouter()
pwd_context=CryptContext(schemes=['bcrypt'],deprecated="auto")
SECRET='your-secret-key'
# manager=LoginManager(SECRET,token_url="/auth/token")


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)