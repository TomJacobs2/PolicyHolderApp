#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.data.database import Base


class AssetModel(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    asset_tag = Column(String(32), nullable=False)
    description = Column(String(256), nullable=False)
    model_year = Column(String(4))
    mileage = Column(Integer, nullable=False)
    date_created = Column(DateTime, default=_datetime.datetime.utcnow())

    events = relationship("EventModel", back_populates="owner")
