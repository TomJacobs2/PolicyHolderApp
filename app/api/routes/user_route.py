#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

from app.business.logic.user_logic import UserLogic

router = APIRouter(prefix="/user",
                   tags=["users"],
                   responses={404: {"description": "Not Found"}})

logic = UserLogic()


@router.get("/", tags=["users"])
async def get_action():
    return logic.process_get_all()


@router.get("/{user_id}", tags=["users"])
async def get_action(user_id: int):
    return logic.process_get_asset(user_id)


@router.post("/", tags=["users"])
async def post_action():
    return logic.process_post()
