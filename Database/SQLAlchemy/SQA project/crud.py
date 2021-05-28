"""A module to cunduct CRUD operations"""

import datetime as dt
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Book)
import config

# Creating an engine instance.
# This instance will connect to the database we mentioned in the config URI.
engine = create_engine(config.DATABASE_URI)

# Creating a global Session instance binded to our database
# This is a factory for individual session managers.
Session = sessionmaker(bind=engine)


"""
# Creatign and droping all tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
"""

def recreate_databases():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# making a function that manages sessions for queries.
# It makes sure commits are rolled back if error, and
# sessions are closed if error or not.
@contextmanager
def session_scope():

    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    
    # creating an individual session manager.
    session1 = Session()

    # recreate_databases()

    # Creating a Book instance
    book1 = Book(
        title='Machine Learning: A Probabilistic Perspective',
        author='Kevin Murphy',
        pages=1104,
        published=dt.date(2012, 8, 24)
    )

    # session1.add(book1)     # adding that instance to session.
    # session1.commit()       # commiting changes made to session to database.

    print(session1.query(Book).first())     # selecting the first entry in the database
    print(session1.query(Book).all())       # selecting all the entries in the database
    session1.close()        # closing the session

    # Using context manager function
    with session_scope() as s:
        book = s.query(Book).filter(Book.title.ilike("%introduction to statistical%")).first()
        book.price = 68.98
        s.add(book)