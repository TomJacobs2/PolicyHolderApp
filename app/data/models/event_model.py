#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.data.database import Base
from .asset_model import AssetModel


class EventModel(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type: Column(Integer, nullable=False)
    geo_lat = Column(Float, nullable=True)
    geo_long = Column(Float, nullable=True)
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
    event_date = Column(DateTime)
    asset_id = Column(Integer, ForeignKey(AssetModel.id))

    event_owner = relationship("AssetModel", back_populates="events")
