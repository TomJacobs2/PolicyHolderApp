#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi import FastAPI

from app.api.routes import default_route, asset_route, event_route

class FastAPIApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.include_router(default_route.router)
        self.app.include_router(asset_route.router)
        self.app.include_router(event_route.router)

    def get_app(self) -> object:
        return self.app
