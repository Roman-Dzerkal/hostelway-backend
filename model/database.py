 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app1.db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/hostelway"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()