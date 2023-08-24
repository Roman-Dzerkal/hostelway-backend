from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    email: str
    name: str
    hashed_password: str
    role: str
    class Config:
        orm_mode = True