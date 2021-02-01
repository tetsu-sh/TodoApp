from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

Base = declarative_base()

RDB_PATH = os.environ["RDB_PATH"]
ECHO_LOG = True
 
engine = create_engine(
   RDB_PATH, echo=ECHO_LOG
)
 
Session = sessionmaker(bind=engine)
session = Session()