from sqlalchemy.orm import Session

from model.models import User
from model.schemas import UserModel


def create_user(db: Session, user: UserModel):

    db_user = User(id=user.id, email=user.email, name=user.name, hashed_password=user.hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()