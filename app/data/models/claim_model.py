#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from app.data.database import Base
from .asset_model import AssetModel


class ClaimModel(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    claim_number: Column(Integer, nullable=False)
    geo_lat = Column(Float, nullable=True)
    geo_long = Column(Float, nullable=True)
    claim_description: Column(String)
    incident_date: Column(DateTime, nullable=False)
    date_created = Column(DateTime, default=_datetime.datetime.utcnow())
    update_created = Column(DateTime, default=_datetime.datetime.utcnow())
    asset_id = Column(Integer, ForeignKey(AssetModel.id))

    #claim_owner = relationship("AssetModel", back_populates="claims")
