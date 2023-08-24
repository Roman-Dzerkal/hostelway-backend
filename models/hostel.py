from pydantic import BaseModel

class Hostel(BaseModel):
    id: int = 12
    name: str = 'test name'
    rating: float = 2.9
    description: str = 'ghweriuhgeriwgl'