from schemas.ProductSchema import ProductCreate, ProductUpdate
from models.models import Product
from tortoise.exceptions import DoesNotExist


async def create_product(product_data: ProductCreate):
    product = await Product.create(**product_data.dict())
    return product


async def get_product(product_id: int):
    return await Product.get(product_id=product_id)


async def update_product(product_id: int, product_data: ProductUpdate):
    await Product.filter(product_id=product_id).update(
        **product_data.dict(exclude_unset=True)
    )
    return await Product.get(product_id=product_id)


async def delete_product(product_id: int):
    await Product.filter(product_id=product_id).delete()
