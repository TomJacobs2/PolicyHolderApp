#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from pydantic import BaseModel
from typing import Generic, TypeVar, Any
from sqlalchemy.orm import Session

from app.data.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCommand(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: TypeVar[ModelType]):
        self.model = model

    def get_one(self, db: Session, model_id: Any):
        return db.query(self.model).filter(self.model.id == model_id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_all_for_id(self, db: Session, model_id: Any):
        return db.query(self.model).filter(self.model.id == model_id).all()
    