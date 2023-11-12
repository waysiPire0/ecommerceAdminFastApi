from fastapi import APIRouter, HTTPException, Depends
from schemas.ProductSchema import ProductCreate, ProductOut, ProductUpdate
from configs.environment import get_environment_variables
from .auth import get_current_user
from services.ProductService import (
    create_product,
    get_product,
    update_product,
    delete_product,
    get_all_products,
)
from typing import List

env = get_environment_variables()

ProductRouter = APIRouter(prefix=f"/{env.API_VERSION}/product", tags=["product"])


@ProductRouter.get("/products", response_model=List[ProductOut])
async def get_all_product_endpoint():
    products = await get_all_products()
    return products


@ProductRouter.post("/", response_model=ProductOut)
async def create_product_endpoint(product: ProductCreate):
    return await create_product(product)


@ProductRouter.get("/{product_id}", response_model=ProductOut)
async def get_product_endpoint(product_id: int):
    product = await get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@ProductRouter.put("/{product_id}", response_model=ProductOut)
async def update_product_endpoint(product_id: int, product: ProductUpdate):
    return await update_product(product_id, product)


@ProductRouter.delete("/{product_id}")
async def delete_product_endpoint(product_id: int):
    await delete_product(product_id)
    return {"message": "Product deleted successfully"}
