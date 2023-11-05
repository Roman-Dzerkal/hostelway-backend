from model.database import Base
from sqlalchemy import Column, Integer, String

from model.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    name = Column(String)
    hashed_password = Column(String)
    role = Column(String)
    phone = Column(String)
