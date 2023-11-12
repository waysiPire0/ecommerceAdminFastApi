from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InventoryCreate(BaseModel):
    product_id: int
    quantity_available: int
    low_stock_threshold: int


class InventoryUpdate(BaseModel):
    quantity_available: Optional[int] = None
    low_stock_threshold: Optional[int] = None


class InventoryOut(BaseModel):
    inventory_id: int
    product_id: int
    quantity_available: int
    low_stock_threshold: int
    last_updated: datetime

    class Config:
        orm_mode = True
