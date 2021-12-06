#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

router = APIRouter(prefix="/event",
                   tags=["events"],
                   responses={404: {"description": "Not Found"}})


@router.get("/{asset_id}", tags=["events"])
async def get_action(asset_id: int):
    return {"msg": "get event route with asset id "}


@router.post("/", tags=["events"])
async def post_action():
    return {"msg": "post events route"}
