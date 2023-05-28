from sqlalchemy import create_engine, text

from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import sessionmaker

from urllib.parse import quote

def connect_to_db():

connection_url = "postgresql://postgres:<1234>@localhost/<postgres>"

try:

engine = create_engine(url=connection_url)

# create a session

session = sessionmaker(bind=engine)

conn = session()

if session:

return conn

except SQLAlchemyError as se:

print(se)
