from schemas.CategorySchema import CategoryCreate, CategoryUpdate
from models.models import Category
from tortoise.exceptions import DoesNotExist


async def create_category(category_data: CategoryCreate):
    category = await Category.create(**category_data.dict())
    return category


async def get_category(category_id: int):
    try:
        return await Category.get(category_id=category_id)
    except DoesNotExist:
        return None


async def get_all_categories():
    return await Category.all()


async def update_category(category_id: int, category_data: CategoryUpdate):
    await Category.filter(category_id=category_id).update(
        **category_data.dict(exclude_unset=True)
    )
    updated_category = await Category.get(category_id=category_id)
    return updated_category


async def delete_category(category_id: int):
    deleted_count = await Category.filter(category_id=category_id).delete()
    return deleted_count
