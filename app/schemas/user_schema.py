#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel, HttpUrl
from typing import Sequence


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile_phone: int
    external_user: bool


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int


class UserInDBBase(UserBase):
    id: int
    create_date: str
    update_date: str

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserSearchResults(BaseModel):
    results: Sequence[User]
