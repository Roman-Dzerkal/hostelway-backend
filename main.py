# from typing import Annotated
# from model.schemas import Login
from fastapi import Depends
from fastapi import FastAPI, Form, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import crud
import model.models
from model.database import SessionLocal, engine
from model.hostel import Hostel
from model.schemas import UserModel

model.models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Hostelway',
              contact={'email': 'dzerkal.r@gmail.com'},
              description='This is the Hostelway API doc',
              version='0.1alha')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/signup")
# async def signup(username: Annotated[str, Form()] = '', password: Annotated[str, Form()] = '', role: Annotated[str, Form()] = '', phone_number: Annotated[str, Form()] = ''):
#     if (username == '' or username is None) or \
#             password == '' or \
#             role == '' or \
#             phone_number == '':
#         return {'status': 'ebal 10 yozhikov'}


# @app.post("/signup", response_model=model.schemas.UserModel)
@app.post("/signup")
def signup(email: str = Form(),
           password: str = Form(),
           role: str = Form(),
           phone: str = Form(),
           name: str = Form(),
           db: Session = Depends(get_db)):
    crud.create_user(db, UserModel(email=email, password=password, role=role, phone=phone, name=name))
    return {
        'status': True,
    }

# @app.get("/users/")
# async def read_users(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}

# @app.post("/signin", response_model=model.schemas.UserModel)
# def signin(login_model: Login, db: Session = Depends(get_db)):
#     return crud.get_user(db, login_model.email)
