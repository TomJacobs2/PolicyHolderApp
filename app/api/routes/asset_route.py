#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

from app.business.logic.asset_logic import AssetLogic

router = APIRouter(prefix="/asset",
                   tags=["assets"],
                   responses={404: {"description": "Not Found"}})

logic = AssetLogic()


@router.get("/", tags=["assets"])
async def get_action():
    return logic.process_get_all()


@router.get("/{asset_id}", tags=["assets"])
async def get_action(asset_id: int):
    return logic.process_get_asset(asset_id)


@router.post("/", tags=["assets"])
async def post_action():
    return logic.process_post()
