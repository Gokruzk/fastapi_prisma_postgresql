from pydantic import BaseModel

class User(BaseModel):
    dni: str
    name: str
    email: str
    password: str