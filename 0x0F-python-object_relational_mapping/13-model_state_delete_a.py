#!/usr/bin/python3
""" Module for task 13 """

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
from sqlalchemy import *


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
            continue
        else:
            continue
    session.commit()

    session.close()
