#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

router = APIRouter(prefix="/asset",
                   tags=["assets"],
                   responses={404: {"description": "Not Found"}})


@router.get("/", tags=["assets"])
async def get_action():
    return {"msg": "get asset route"}


@router.get("/{asset_id}", tags=["assets"])
async def get_action(asset_id: int):
    return {"msg": "get asset route with asset id "}


@router.post("/", tags=["assets"])
async def post_action():
    return {"msg": "post asset route"}