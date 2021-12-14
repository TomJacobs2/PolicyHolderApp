#  Copyright (c) Thomas Jacobs. All Rights Reserved.

import datetime as _datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.data.database_app import Base


class OAuthModel(Base):
    __tablename__ = "oauths"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(256), nullable=False)
    user_id = Column(Integer, nullable=False)
    create_date = Column(DateTime, default=_datetime.datetime.utcnow())
