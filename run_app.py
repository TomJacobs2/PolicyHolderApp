#   Copyright (c) Thomas Jacobs. All Rights Reserved.

import uvicorn

from app.api.fastapi_app import FastAPIApp

app = FastAPIApp().get_app()

uvicorn.run(app, host="127.0.0.1", port=5000)