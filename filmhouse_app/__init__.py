from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from .database import SessionLocal
from instance.config import SECRET_KEY, DATABASE_URI

run = FastAPI()

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base: DeclarativeMeta = declarative_base()


from filmhouse_app import routes
run.include_router(routes.router)
