#!/usr/bin/python3

"""
a script that deletes all State objects with a name containing the letter a
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))
    query.delete()
    session.commit()
