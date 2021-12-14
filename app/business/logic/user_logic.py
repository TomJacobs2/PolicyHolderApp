#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from typing import Any
from app.data.database_app import database_app
from app.data.commands.user_command import user_cmd
from app.data.commands.oauth_command import oauth_cmd
from app.schemas.user_schema import UserCreate, UserUpdate

class UserLogic():
    def __init__(self):
        self.session = database_app.get_session()

    def process_get_all(self):
        print("User Logic: get all called")
        return user_cmd.get_all(db=self.session)

    def process_get_asset(self, user_id: int):
        print(f"User Logic: get user with id of {user_id}")
        return user_cmd.get_one(db=self.session, model_id=user_id)

    def process_post(self, request: Any):
        if isinstance(request, UserUpdate):
            print("Is UserCreate")
        user_cmd.create(db=self.session, schema_in=request)
        print("User Logic: post request called")
        print(request)

