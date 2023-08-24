# from typing import Annotated
from typing import Annotated
import annotated_types
from fastapi import FastAPI, Form, HTTPException, Response, responses, status

from models.hostel import Hostel


def hello():
    print('Hwllo back')


""" Abona """

app = FastAPI(title='Hostelway',
              contact={'email': 'dzerkal.r@gmail.com'},
              description='This is the Hostelway API doc',
              on_startup=[hello],
              version='0.1alha')


@app.get('/')
async def hello():
    return {'Hello!'}


# @app.post("/login")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     if username == '' or password == '':
#         return status.HTTP_400_BAD_REQUEST
#     return {"username": username}


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
