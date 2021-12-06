#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

from app.business.logic.asset_logic import AssetLogic

router = APIRouter(prefix="/asset",
                   tags=["assets"],
                   responses={404: {"description": "Not Found"}})

logic = AssetLogic()

@router.get("/", tags=["assets"])
async def get_action():
    logic.process_get_all()
    return {"msg": "get asset route"}


@router.get("/{asset_id}", tags=["assets"])
async def get_action(asset_id: int):
    logic.process_get_asset(asset_id)
    return {"msg": "get asset route with asset id "}


@router.post("/", tags=["assets"])
async def post_action():
    logic.process_post()
    return {"msg": "post asset route"}