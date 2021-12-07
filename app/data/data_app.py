#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from app.data.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()