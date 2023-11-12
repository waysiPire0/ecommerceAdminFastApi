from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from tortoise import models, fields


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None


class ProductOut(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    category_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
