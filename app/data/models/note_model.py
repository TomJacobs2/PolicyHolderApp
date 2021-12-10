#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from app.data.database import Base
from .claim_model import ClaimModel


class ClaimModel(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    note_type: Column(Integer, nullable=False)
    note_subject: Column(String)
    note_description: Column(String)
    date_created = Column(DateTime, default=_datetime.datetime.utcnow())
    update_created = Column(DateTime, default=_datetime.datetime.utcnow())
