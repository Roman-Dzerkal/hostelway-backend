from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str
    hashed_password: str
    role: str
    phone: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    hashed_password: str
    