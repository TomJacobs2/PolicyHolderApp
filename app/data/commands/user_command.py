#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from .base_command import BaseCommand
from app.data.models.user_model import UserModel
from app.schemas.user_schema import UserCreate, UserUpdate


class UserCommand(BaseCommand[UserModel, UserCreate, UserUpdate]):
    ...


user_cmd = UserCommand(UserModel)