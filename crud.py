from sqlalchemy.orm import Session
from model.models import User
from model.schemas import UserModel
import hashlib


def create_user(db: Session, user: UserModel):
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()

    db_user = User(email=user.email, name=user.name, hashed_password=hashed_password, role=user.role,
                   phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def get_user(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()
