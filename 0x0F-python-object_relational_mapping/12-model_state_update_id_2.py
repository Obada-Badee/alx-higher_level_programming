#!/usr/bin/python3

"""
A script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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
    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = 'New Mexico'
    session.commit()
