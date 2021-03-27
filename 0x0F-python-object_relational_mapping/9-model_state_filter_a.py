#!/usr/bin/python3
""" List all State objects with an 'a' from db
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like('%a%'))
    for row in result:
        print("{}: {}".format(row.id, row.name))
