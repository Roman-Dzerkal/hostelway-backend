from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: int
    email: str
    name: str
    role: str
    phone: str
