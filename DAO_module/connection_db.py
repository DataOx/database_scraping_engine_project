import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_string = os.environ.get('POSTGRES_CONNECTION_STR', "postgresql://summer:q2VmcgOJff@194.163.164.118:5434/summer_db")
engine = create_engine(db_string)
Base = declarative_base()
