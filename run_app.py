#   Copyright (c) Thomas Jacobs. All Rights Reserved.

import uvicorn

from app.api.fastapi_app import FastAPIApp
from app.data.database_setup import DatabaseSetup

app = FastAPIApp().get_app()
DatabaseSetup().create_database()

uvicorn.run(app, host="127.0.0.1", port=5000)
