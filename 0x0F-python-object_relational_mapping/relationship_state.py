#!/usr/bin/python3
""" Module for task 6 """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ 
    Represents a State 
        Attributes:
            - __tablename__ (str): cities (name of table)
            - id (column): column of table
            - name (column, str): column of table
            - state_id (column, int): column of int in table
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
