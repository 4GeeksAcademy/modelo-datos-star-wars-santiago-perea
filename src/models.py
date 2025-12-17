from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    FullName: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    created: Mapped[str] = mapped_column(nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    birth_year: Mapped[str] = mapped_column(nullable=False)
    films: Mapped[str] = mapped_column(nullable=False)
    eye_color: Mapped[str] = mapped_column(nullable=False)
    hair_color: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)  
    homeworld: Mapped[str] = mapped_column(nullable=False) 
    height: Mapped[str] = mapped_column(nullable=False) 
    skin_color: Mapped[str] = mapped_column(nullable=False) 
    planet: Mapped[str] = mapped_column(nullable=False) 
    species: Mapped[str] = mapped_column(nullable=False) 
    starships: Mapped[str] = mapped_column(nullable=False) 
    vehicles: Mapped[str] = mapped_column(nullable=False) 
    url: Mapped[str] = mapped_column(nullable=False) 
    created: Mapped[str] = mapped_column(nullable=False)

    favorite_people: Mapped[List["FavoritePeople"]] = relationship(back_populates="people")


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    diameter: Mapped[str] = mapped_column(nullable=False)
    rotation_period: Mapped[str] = mapped_column(nullable=False)
    orbital_period: Mapped[str] = mapped_column(nullable=False)
    gravity: Mapped[str] = mapped_column(nullable=False)
    population: Mapped[str] = mapped_column(nullable=False)  
    climate: Mapped[str] = mapped_column(nullable=False) 
    terrain: Mapped[str] = mapped_column(nullable=False) 
    surface_water: Mapped[str] = mapped_column(nullable=False) 
    residents: Mapped[str] = mapped_column(nullable=False) 
    films: Mapped[str] = mapped_column(nullable=False) 
    url: Mapped[str] = mapped_column(nullable=False) 
    created: Mapped[str] = mapped_column(nullable=False)

    favorite_planet: Mapped[List["FavoritePlanet"]] = relationship(back_populates="planet")


class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_ID: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="favorites")

class FavoritePlanet(Favorites):
    __tablename__ = "favoritesplanets"
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_ID: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped["Planet"] = relationship(back_populates="favorite_planet")

class FavoritePeople(Favorites):
    __tablename__ = "favoritespeople"
    id: Mapped[int] = mapped_column(primary_key=True)
    people_ID: Mapped[int] = mapped_column(ForeignKey("people.id"))
    people: Mapped["People"] = relationship(back_populates="favorite_people")
