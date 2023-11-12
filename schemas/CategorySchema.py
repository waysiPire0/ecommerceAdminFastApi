from pydantic import BaseModel
from typing import Optional


class CategoryCreate(BaseModel):
    name: str
    description: str


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class CategoryOut(BaseModel):
    category_id: int
    name: str
    description: str

    class Config:
        orm_mode = True
