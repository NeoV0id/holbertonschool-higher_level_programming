#!/usr/bin/python3
""" Modyle for task 100 """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """ Represents a City 
    Attributes:
        - __tablename__ (str): cities (name of table)
        - id (column): column of table
        - name (column, str): column of table
        - state_id (column, int): column of int in table
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
