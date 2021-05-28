#%%
import datetime as dt

from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from models import Book
from crud import engine

# creating session factory
Session = sessionmaker(bind=engine)

# creating session
s = Session()

#%%
# session.query(Model).filter_by() method

result = s.query(Book).filter_by(title='Deep Learning').first()
print(result)

#%%
# session.query(Model).filter() method
# filter requires Model name inside .filter(), unlike .filter_by()

result2 = s.query(Book).filter(Book.title.ilike('deep learning')).first()
print(result2)

#%%
# .filter() between method.
start_date = dt.datetime(2009, 1, 1)
end_date = dt.datetime(2012, 1, 1)

result3 = s.query(Book).filter(Book.published.between(start_date, end_date)).first()
print(result3)

#%%
# using AND condition. Books with more than 600 pages AND published after 2016.

print(s.query(Book).filter(
        and_(
            Book.pages > 600, 
            Book.published > dt.datetime(2016, 1, 1)
            )).all())
# print(result4)

#%%
# using OR condition. Books published before 2010 OR 2016

result5 = s.query(Book).filter(
    or_(
        Book.published < dt.date(2010, 1, 1),
        Book.published > dt.date(2016, 1, 1)
    )
).all()
print(result5)

#%%
# ORDER BY clause

print(s.query(Book).order_by(Book.pages.desc()).all())
print('\n')
print(s.query(Book).order_by(Book.pages.asc()).all())

#%%
# LIMIT clause
print(s.query(Book).limit(2).all())

#%%
# Making complex queries
"""books either less than 500 pages or greater than 750 pages long
    books published between 2013 and 2017
    ordered by the number of pages
    limit it to one result"""

result6 = s.query(Book).filter(
    and_(
        or_(
            Book.pages < 500,
            Book.pages > 750
        ),
        Book.published.between(dt.datetime(2013, 1, 1), dt.datetime(2017, 1, 1))
    )
)\
.order_by(Book.pages.desc())\
.limit(1)\
.first()

print(result6)
# %%
