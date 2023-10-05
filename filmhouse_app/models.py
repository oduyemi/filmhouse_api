from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from .database import Base

class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    cast = Column(String, index=True)
    price = Column(Float, index=True)
    rating = Column(Integer, ForeignKey("rating.id"))
    is_new = Column(Boolean, default=True)
    

class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(String, index=True)
    description = title = Column(Text, index=True)
   


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    password = Column(String, index=True)
    hashedpassword = Column(String)
    movie_rented_id = Column(Integer, ForeignKey("movie.id"))
    movie_bought_id = Column(Integer, ForeignKey("movie.id"))

    movie_rented = relationship("Movie", foreign_keys=[movie_rented_id], back_populates="rented", cascade="all, delete-orphan")
    movie_bought = relationship("Movie", foreign_keys=[movie_bought_id], back_populates="bought", cascade="all, delete-orphan")

class Rental(Base):
    __tablename__ = "rental"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Sales(Base):
    __tablename__ = "sales"
    movie_id = Column(Integer, ForeignKey("movie.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    password = Column(String, index=True)
    hashedpassword = Column(String)
    role = Column(String, default="user")




