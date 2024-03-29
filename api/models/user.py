from pydantic import BaseModel


class Register(BaseModel):
    username: str
    email: str
    password: str
