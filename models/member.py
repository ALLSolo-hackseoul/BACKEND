from pydantic import BaseModel


class Member(BaseModel):
    userid: str
    name: str
    phone: str
    email: str
    password: str
    address: str
    country: str
