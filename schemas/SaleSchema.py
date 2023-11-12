from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    total_price: float
    customer_id: int


class SaleUpdate(BaseModel):
    quantity: Optional[int] = None
    total_price: Optional[float] = None


class SaleOut(BaseModel):
    sale_id: int
    product_id: int
    quantity: int
    sale_date: datetime
    total_price: float
    customer_id: int

    class Config:
        orm_mode = True
