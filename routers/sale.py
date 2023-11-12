from fastapi import APIRouter, HTTPException, Depends, Query
from schemas.SaleSchema import SaleCreate, SaleOut, SaleUpdate
from services.SaleService import (
    create_sale,
    get_sale,
    update_sale,
    delete_sale,
    get_all_sales,
)
from configs.environment import get_environment_variables
from .auth import get_current_user
from datetime import date, datetime
from typing import Optional
from models.models import Sale, Inventory
from tortoise.expressions import Q
from tortoise.expressions import F
from collections import defaultdict


env = get_environment_variables()

SaleRouter = APIRouter(prefix=f"/{env.API_VERSION}/sale", tags=["Sales"])


@SaleRouter.get("/sales")
async def get_sales(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    product_id: Optional[int] = None,
    category_id: Optional[int] = None,
):
    query = Q()
    if start_date:
        query &= Q(sale_date__gte=start_date)
    if end_date:
        query &= Q(sale_date__lte=end_date)
    if product_id:
        query &= Q(product_id=product_id)
    if category_id:
        query &= Q(product__category_id=category_id)

    sales = await Sale.filter(query).all()
    return sales


def get_date_key(date: datetime, timeframe: str):
    if timeframe == "daily":
        return date.date()
    elif timeframe == "weekly":
        return f"{date.year}-W{date.isocalendar()[1]}"
    elif timeframe == "monthly":
        return f"{date.year}-{date.month}"
    elif timeframe == "annual":
        return date.year


@SaleRouter.get("/sales/revenue")
async def get_revenue_analysis(
    timeframe: str = Query(..., regex="^(daily|weekly|monthly|annual)$")
):
    sales = await Sale.all().values("sale_date", "total_price")

    revenue_data = defaultdict(float)
    for sale in sales:
        date_key = get_date_key(sale["sale_date"], timeframe)
        revenue_data[date_key] += float(sale["total_price"])

    return [
        {"timeframe": key, "total_revenue": total}
        for key, total in revenue_data.items()
    ]


@SaleRouter.post("/", response_model=SaleOut)
async def create_sale_endpoint(sale: SaleCreate):
    new_sale = await create_sale(sale)
    return new_sale


@SaleRouter.get("/{sale_id}", response_model=SaleOut)
async def get_sale_endpoint(sale_id: int):
    sale = await get_sale(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@SaleRouter.put("/{sale_id}", response_model=SaleOut)
async def update_sale_endpoint(sale_id: int, sale_data: SaleUpdate):
    updated_sale = await update_sale(sale_id, sale_data)
    if not updated_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated_sale


@SaleRouter.delete("/{sale_id}")
async def delete_sale_endpoint(sale_id: int):
    deleted_count = await delete_sale(sale_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"message": "Sale deleted successfully"}
