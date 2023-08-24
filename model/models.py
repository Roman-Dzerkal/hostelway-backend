from pydantic import BaseModel
from model.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, primary_key=False, index=False)
    name = Column(String, primary_key=False, index=False)
    hashed_password  = Column(String)
    role =Column(String, primary_key=False, index=False)
