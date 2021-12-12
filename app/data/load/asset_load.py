#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session
from app.data.models.asset_model import AssetModel
from app.schemas.asset_schema import AssetCreate, AssetUpdate
from app.data.commands.asset_command import AssetCommand

def initial_asset_load(db: Session):
    cmd = AssetCommand(model=AssetModel)
    session = Session()
    raw_data = {"asset_tag": "tag1234", "description": "Lambo", "mileage": 925, "model_year": "2021"}
    data = AssetCreate(**raw_data)
    cmd.create(db=session, schema_in=data)
