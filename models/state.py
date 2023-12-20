#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """Representtion of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        cities = relationship("City", backref="state")
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """intializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city istances related to the state"""
            all_cities = models.storage.all(City)
            city_list = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
