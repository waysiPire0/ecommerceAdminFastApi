from fastapi import APIRouter, HTTPException, Depends
from schemas.CategorySchema import CategoryCreate, CategoryOut, CategoryUpdate
from .auth import get_current_user
from services.CategoryService import (
    create_category,
    get_category,
    get_all_categories,
    update_category,
    delete_category,
)
from typing import List

CategoryRouter = APIRouter(prefix="/category", tags=["category"])


@CategoryRouter.post("/", response_model=CategoryOut)
async def create_category_endpoint(category: CategoryCreate):
    new_category = await create_category(category)
    return new_category


@CategoryRouter.get("/{category_id}", response_model=CategoryOut)
async def get_category_endpoint(category_id: int):
    category = await get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@CategoryRouter.get("/", response_model=List[CategoryOut])
async def get_all_categories_endpoint():
    categories = await get_all_categories()
    return categories


@CategoryRouter.put("/{category_id}", response_model=CategoryOut)
async def update_category_endpoint(category_id: int, category_data: CategoryUpdate):
    updated_category = await update_category(category_id, category_data)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category


@CategoryRouter.delete("/{category_id}")
async def delete_category_endpoint(category_id: int):
    deleted_count = await delete_category(category_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
