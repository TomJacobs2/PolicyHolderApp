#   Copyright (c) Thomas Jacobs. All Rights Reserved.

import uvicorn

from app.api.fastapi_app import FastAPIApp
from app.data.database_app import database_app


data_app = database_app
data_app.create_database()
fast_app = FastAPIApp().get_app()


uvicorn.run(fast_app, host="127.0.0.1", port=5000)
