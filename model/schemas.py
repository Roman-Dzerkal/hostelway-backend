from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    name: str
    password: str
    role: str
    phone: str
