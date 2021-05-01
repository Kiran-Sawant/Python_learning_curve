"""Module to define ORM Models."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, String, Date)

# Creating an instance of declarative base
# Our models need to inherit this instance, for SQA to recognise our models.
Base = declarative_base()

# Creating a Model
class Book(Base):
    __tablename__ = 'books'
    id          = Column(Integer, primary_key=True)
    title       = Column(String)
    author      = Column(String)
    pages       = Column(Integer)
    published   = Column(Date)

    def __repr__(self):
        return f"{self.title} by {self.author}"


