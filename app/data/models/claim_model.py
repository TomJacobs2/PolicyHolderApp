#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from app.data.database_app import Base

from .asset_model import AssetModel
from .user_model import UserModel


class ClaimModel(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_number: Column(Integer, nullable=False)
    geo_lat = Column(Float, nullable=True)
    geo_long = Column(Float, nullable=True)
    claim_description: Column(String)
    incident_date: Column(DateTime, nullable=False)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    update_date = Column(DateTime, default=_datetime.datetime.utcnow())
    created_by = Column(Integer, ForeignKey(UserModel.id))
    updated_by = Column(Integer, ForeignKey(UserModel.id))

    #claim_owner = relationship("AssetModel", back_populates="claims")
