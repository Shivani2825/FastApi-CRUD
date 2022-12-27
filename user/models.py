from tortoise.models import Model
from tortoise import Tortoise,fields
from fastapi import FastAPI
from tortoise import Tortoise


class User(Model):
    id=fields.UUIDField(pk=True)
    name=fields.CharField(50)
    email=fields.CharField(50,unique=True)
    password=fields.CharField(250)

Tortoise.init_models(['user.models'],'models')