#!/usr/bin/python3
""" Quiero usar un IDE nieryyy
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(State.id == City.state_id).all()
    for city in result:
        print("{}: ({}) {}".format(city.State.name,
                                   city.City.id, city.City.name))
