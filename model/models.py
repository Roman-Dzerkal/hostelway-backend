from pydantic import BaseModel
from model.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    hashed_password = Column(String)
    role = Column(String)
    phone = Column(String)


