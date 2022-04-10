#!/usr/bin/python3
""" Module for task 9 """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
    for state in session.filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    for state in session.order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
