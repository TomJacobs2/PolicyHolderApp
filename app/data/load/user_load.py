#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.schemas.user_schema import UserCreate, UserUpdate
from app.business.logic.user_logic import UserLogic

def initial_user_load():
    logic = UserLogic()
    raw_data = {"first_name": "Super", "last_name": "User", "email": "super.user@newcompany.com", "mobile_phone": 5739991234, "external_user": 0}
    data = UserCreate(**raw_data)
    logic.process_post(request=data)