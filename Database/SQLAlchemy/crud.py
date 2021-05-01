"""A module to cunduct CRUD operations"""

import datetime as dt

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

if __name__ == "__main__":
    
    # creating an individual session manager.
    session1 = Session()

    # recreate_databases()

    # Creating a Book instance
    book1 = Book(
        title='Deep Learning',
        author='Ian GoodFellow',
        pages='775',
        published=dt.date(2016, 11, 18)
    )

    session1.add(book1)     # adding that instance to session.
    session1.commit()       # commiting changes made to session to database.
    session1.close()        # closing the session