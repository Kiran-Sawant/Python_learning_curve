"""A Script to add price value to price column in book table"""

from crud import engine
from models import Book
from sqlalchemy.orm.session import sessionmaker

Session = sessionmaker(bind=engine)

s = Session()

books = s.query(Book).all()

for book in books:
    price = int(input(f"Insert price for {book.title}: "))
    book.price = price
    s.add(book)

s.commit()
s.close()