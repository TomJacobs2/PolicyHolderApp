#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel, HttpUrl
from typing import Sequence


class AssetBase(BaseModel):
    asset_tag: str
    description: str
    model_year: str
    mileage: int


class AssetCreate(AssetBase):
    pass


class AssetUpdate(AssetBase):
    id: int


class AssetInDBBase(AssetBase):
    id: int
    date_create: str

    class Config:
        orm_mode = True


class Asset(AssetInDBBase):
    pass


class AssetSearchResults(BaseModel):
    results: Sequence[Asset]
