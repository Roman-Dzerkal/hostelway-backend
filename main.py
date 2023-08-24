# from typing import Annotated
from typing import Annotated
import annotated_types
from fastapi import FastAPI, Form, HTTPException, Response, responses, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model.hostel import Hostel
import crud
import model.models
import model.schemas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlite3 import Connection, connect
from model.database import SessionLocal, engine


model.models.Base.metadata.create_all(bind=engine)


app = FastAPI(title='Hostelway',
              contact={'email': 'dzerkal.r@gmail.com'},
              description='This is the Hostelway API doc',
              version='0.1alha')




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    if username == '' or password == '':
        return status.HTTP_400_BAD_REQUEST
    return {"username": username}


# @app.post("/signup")
# async def signup(username: Annotated[str, Form()] = '', password: Annotated[str, Form()] = '', role: Annotated[str, Form()] = '', phone_number: Annotated[str, Form()] = ''):
#     if (username == '' or username is None) or \
#             password == '' or \
#             role == '' or \
#             phone_number == '':
#         return {'status': 'ebal 10 yozhikov'}


@app.put('/hostels')
def update_hostel_by_id(id: Annotated[int, Form()] , name: Annotated[str, Form()], rating: Annotated[float, Form()], desciprion: Annotated[str, Form()]):
    """ Update a hostel by its ID """
    if id is None:
        raise HTTPException(status_code=400, detail={'message': 'User not found'})
    else:
        return Hostel()


@app.post("/signup/", response_model=model.schemas.UserModel)
def signup(user: model.schemas.UserModel, db: Session = Depends(get_db)):
    return crud.create_user(db, model.schemas.UserModel(id=user.id, email=user.email, name=user.name, hashed_password=user.hashed_password, role=user.role))
