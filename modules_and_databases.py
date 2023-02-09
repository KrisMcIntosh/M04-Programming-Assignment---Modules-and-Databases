# Modules and Databases pt.2
# author: Kris McIntosh
# created: 2023-02-09  updated: 2023-02-09 (Kris McIntosh)
# Part two of this assignment.

# Import using 'from'
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# create an engine for connecting to the database
engine = create_engine("sqlite:///books.db")

# create a session to execute queries
Session = sessionmaker(bind=engine)
session = Session()

# create metadata and table objects to represent the book table
metadata = MetaData()
book_table = Table("book", metadata, autoload=True, autoload_with=engine)

# execute a query to select the title column from the book table
query = book_table.select().with_only_columns([book_table.c.title]).order_by(book_table.c.title)
result = session.execute(query)

# print the results
for row in result:
    print(row[0])

# close the session
session.close()
