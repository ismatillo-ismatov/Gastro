from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_made=True
        schema_extra={
            'example':{
                "username":"ismatillo",
                "email":"ismatilloismatov1995@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }