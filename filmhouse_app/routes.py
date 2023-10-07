from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from filmhouse_app import run
from filmhouse_app.dependencies import get_db
from typing import List as FastAPIList
from filmhouse_app.models import Movie


filmhouse_router = APIRouter()

@run.get("/", status_code=200)
async def get_index():
    return {"message": "Welcome to Filmhouse API"}

@run.get("/movies")
async def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@run.get("/movie/{movie_id}")
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
















