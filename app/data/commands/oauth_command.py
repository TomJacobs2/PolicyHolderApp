#  Copyright (c) Thomas Jacobs. All Rights Reserved.
import random
import string

from app.data.models.oauth_model import OAuthModel


class OAuthCommand():
    def __init__(self):
        print("oauth")
        print(self)

    def generator_token(self, len=256):
        token = ''.join(random.choice(string.printable) for pos in range(len))
        return token

    def check_token(self, token: str):
        return 1

    def process_user_login(self, user_id: int):
        """
        get token
        store token, user id to database via CreateSchema
        return CreateSchema
        """
        pass


oauth_cmd = OAuthCommand()