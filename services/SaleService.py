from schemas.SaleSchema import SaleCreate, SaleUpdate
from models.models import Sale
from tortoise.exceptions import DoesNotExist


async def get_all_sales():
    return await Sale.all()


async def create_sale(sale_data: SaleCreate):
    sale = await Sale.create(**sale_data.dict())
    return sale


async def get_sale(sale_id: int):
    try:
        return await Sale.get(sale_id=sale_id)
    except DoesNotExist:
        return None


async def update_sale(sale_id: int, sale_data: SaleUpdate):
    await Sale.filter(sale_id=sale_id).update(**sale_data.dict(exclude_unset=True))
    updated_sale = await Sale.get(sale_id=sale_id)
    return updated_sale


async def delete_sale(sale_id: int):
    deleted_count = await Sale.filter(sale_id=sale_id).delete()
    return deleted_count
