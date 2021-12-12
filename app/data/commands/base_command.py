#  Copyright (c) Thomas Jacobs. All Rights Reserved.

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Generic, TypeVar, Any, Dict, Union
from sqlalchemy.orm import Session

from app.data.database_app import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseCommand(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: ModelType):
        self.model = model

    def get_one(self, db: Session, model_id: int):
        print(model_id)
        return db.query(self.model).filter(self.model.id == model_id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_all_for_id(self, db: Session, model_id: Any):
        return db.query(self.model).filter(self.model.id == model_id).all()

    def create(self, db: Session, *, schema_in: CreateSchemaType) -> ModelType:
        model_data = jsonable_encoder(schema_in)
        db_model = self.model(**model_data)
        db.add(db_model)
        db.commit()
        db.refresh()
        return db_model

    def update(self, db: Session, *, model_type: ModelType, schema_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        model_data = jsonable_encoder(schema_in)
        if isinstance(schema_in, dict):
            update_data = schema_in
        else:
            update_data = schema_in.dict(exclude_unset=True)

        for field in model_data:
            if field in update_data:
                setattr(model_type, field, update_data[field])

        db.add(model_type)
        db.commit()
        db.refresh()
        return model_type

    def delete(self, db: Session, *, model_id: int) -> ModelType:
        model_data = db.query(self.model).get(model_id)
        db.delete(model_data)
        db.commit()
        return model_data
    