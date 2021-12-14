#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel, HttpUrl
from typing import Sequence


class OAuthBase(BaseModel):
    user_id: int
    token: str
    create_date: str


class OAuthCreate(OAuthBase):
    pass


class OAuthUpdate(OAuthBase):
    id: int


class OAuthInDBBase(OAuthBase):
    id: int

    class Config:
        orm_mode = True


class OAuth(OAuthInDBBase):
    pass


class OAuthSearchResults(BaseModel):
    results: Sequence[OAuth]
