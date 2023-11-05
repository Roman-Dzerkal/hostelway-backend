from typing import Type

from sqlalchemy.orm import Session
from model.models import User
from model.schemas import UserModel
import hashlib
import utils


def create_user(db: Session, email: str, password: str, role: str, phone: str, name: str):
    hashed_password = utils.hash_password(password)

    db_user = User(email=email, name=name, hashed_password=hashed_password, role=role,
                   phone=phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user(db: Session, user_email: str, password: str) -> Type[User] | None:
    return db.query(User).filter(
        User.email == user_email and User.hashed_password == utils.hash_password(password)).first()
