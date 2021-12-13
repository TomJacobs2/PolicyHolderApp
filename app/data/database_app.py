#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

Base = declarative.declarative_base()

from app.data.models import asset_model, claim_model, event_model, note_model, user_model


class DatabaseApp():
    def __init__(self, db_uri="sqlite:///./asset.db"):
        self.database_uri = db_uri
        self.engine = create_engine(self.database_uri, connect_args={"check_same_thread": False})
        session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = session_local()
        self.base = Base

    def get_session(self):
        return self.session

    def get_base(self):
        return self.base

    def get_engine(self):
        return self.engine

    def get_database_uri(self):
        return self.database_uri

    def does_database_exists(self):
        results = database_exists(self.database_uri)
        print(results)
        return results

    def create_database(self):
        if not database_exists(self.database_uri):
            print("create database")
            create_database(self.database_uri)
            self.base.metadata.create_all(bind=self.engine)

    def initial_load(self):
        print("load data")
        from app.data.load import asset_load, user_load
        asset_load.initial_asset_load()
        user_load.initial_user_load()


database_app = DatabaseApp()

