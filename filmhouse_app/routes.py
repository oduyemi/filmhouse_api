from fastapi import APIRouter, Request, status
from sqlalchemy.orm import Session
from filmhouse_app import run



router = APIRouter()


@run.get("/")
async def get_index():
    return{"message": "Welcome to Filmhouse API"}
















