#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy.orm import Session
from .base_command import BaseCommand
from app.data.models.asset_model import AssetModel
from app.schemas.asset_schema import AssetCreate, AssetUpdate


class AssetCommand(BaseCommand[AssetModel, AssetCreate, AssetUpdate]):
    ...


asset_cmd = AssetCommand(AssetModel)

