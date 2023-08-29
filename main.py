# from typing import Annotated
from typing import Annotated
from fastapi import FastAPI, Form, HTTPException
from model.hostel import Hostel
import crud
import model.models
import model.schemas
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from model.database import SessionLocal, engine
from  model.schemas import Login


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
    return crud.create_user(db, model.schemas.UserModel(email=user.email, name=user.name, hashed_password=user.hashed_password, role=user.role))


@app.get("/user/", response_model=model.schemas.UserModel)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
   return crud.get_user(db, user_id)


@app.post("/signin/", response_model=model.schemas.UserModel)
def signin(login_model: Login, db: Session = Depends(get_db)):
   return crud.get_user(db, login_model.email)