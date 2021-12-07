#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy_utils import create_database, database_exists
import app.data.database as db_app

from app.data.models import asset_model, event_model


class DatabaseSetup():
    def __init__(self):
        pass

    def create_database(self):
        if not database_exists(db_app.SQLALCHEMY_DATABASE_URL):
            create_database(db_app.SQLALCHEMY_DATABASE_URL)
            db_app.Base.metadata.create_all(bind=db_app.engine)
