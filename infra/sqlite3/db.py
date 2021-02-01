from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

RDB_PATH = 'sqlite:///infra/sqlite3/db.sqlite3'
ECHO_LOG = True
 
engine = create_engine(
   RDB_PATH, echo=ECHO_LOG
)
 
Session = sessionmaker(bind=engine)
session = Session()