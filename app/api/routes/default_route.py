#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import APIRouter

router = APIRouter(tags=["default"], responses={404: {"description": "Not found"}})

@router.get("/", tags=["default"])
async def get_action():
    return {"msg": {"Default route is not available"}}
