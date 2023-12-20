#!/usr/bin/python3
""" holds class User"""
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Represetation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        password = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)
        reviews = relationship("Review", backref="user")
        last_name = Column(String(128), nullable=True)
        first_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
    else:
        password = ""
        last_name = ""
        email = ""
        first_name = ""

    def __init__(self, *args, **kwargs):
        """iniializes user"""
        super().__init__(*args, **kwargs)
