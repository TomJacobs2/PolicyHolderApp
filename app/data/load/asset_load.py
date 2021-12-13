#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schemas.asset_schema import AssetCreate, AssetUpdate
from app.business.logic.asset_logic import AssetLogic

def initial_asset_load():
    logic = AssetLogic()
    raw_data = {"asset_tag": "tag1234", "description": "Lambo", "mileage": 925, "model_year": "2021"}
    data = AssetCreate(**raw_data)
    logic.process_post(request=data)
