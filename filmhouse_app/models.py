from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from filmhouse_app import Base



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=200), index=True)
    age = Column(Integer, CheckConstraint("age >= 0") index=True)
    email = Column(String(length=120), unique=True, index=True)
    phone = Column(String(length=80), index=True)
    password = Column(String(length=100), index=True)
    hashedpassword = Column(String(length=100))

    movie_rented_id = Column(Integer, ForeignKey("movie.id"))
    movie_bought_id = Column(Integer, ForeignKey("movie.id"))

    movie_rented = relationship("Movie", foreign_keys=[movie_rented_id], back_populates="rented", cascade="all, delete-orphan")
    movie_bought = relationship("Movie", foreign_keys=[movie_bought_id], back_populates="bought", cascade="all, delete-orphan")
    rented = relationship("Movie", back_populates="rentals", foreign_keys=[movie_rented_id])
    bought = relationship("Movie", back_populates="sales", foreign_keys=[movie_bought_id])


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=255), index=True)
    description = Column(Text)
    genre = Column(String(length=255), index=True)
    rating_id = Column(Integer, ForeignKey("ratings.id"))
    rating = relationship("Rating", back_populates="movies")
    price = Column(Float, index=True)
    image = Column(String(length=200))
    is_new = Column(Boolean, default=True)
    rentals = relationship("Rental", back_populates="movie")

    rented = relationship("User", back_populates="movie_rented", foreign_keys=[User.movie_rented_id])
    bought = relationship("User", back_populates="movie_bought", foreign_keys=[User.movie_bought_id])
    

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=255), index=True)
    description = Column(Text)
    stars = Column(Integer)
   
    movies = relationship("Movie", back_populates="rating")


class Rental(Base):
    __tablename__ = "rental"
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movie.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    rental_date = Column(DateTime, default=datetime.utcnow)


class Sales(Base):
    __tablename__ = "sales"
    movie_id = Column(Integer, ForeignKey("movie.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    sales_date = Column(DateTime, default=datetime.utcnow)


class Admin(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=200), index=True)
    email = Column(String(length=120), unique=True, index=True)
    phone = Column(String(length=80), index=True)
    password = Column(String(length=100), index=True)
    hashedpassword = Column(String(length=100))
    role = Column(String(length=255), default="user")




