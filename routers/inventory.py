from fastapi import APIRouter, HTTPException
from schemas.InventorySchema import InventoryCreate, InventoryOut, InventoryUpdate
from configs.environment import get_environment_variables
from models.models import Inventory
from .auth import get_current_user
from services.InventoryService import (
    create_inventory,
    get_inventory,
    update_inventory,
    delete_inventory,
    get_all_inventories,
)
from typing import List
from tortoise.expressions import F


env = get_environment_variables()

InventoryRouter = APIRouter(prefix=f"/{env.API_VERSION}/inventory", tags=["inventory"])


@InventoryRouter.get("/inventories", response_model=List[InventoryOut])
async def get_all_inventories_endpoint():
    inventories = await get_all_inventories()
    return inventories


@InventoryRouter.get("/low-stock")
async def get_low_stock_alerts():
    low_stock_items = await Inventory.filter(
        quantity_available__lte=F("low_stock_threshold")
    ).all()
    return low_stock_items


@InventoryRouter.post("/", response_model=InventoryOut)
async def create_inventory_endpoint(inventory: InventoryCreate):
    new_inventory = await create_inventory(inventory)
    return new_inventory


@InventoryRouter.get("/{inventory_id}", response_model=InventoryOut)
async def get_inventory_endpoint(inventory_id: int):
    inventory = await get_inventory(inventory_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory


@InventoryRouter.put("/{inventory_id}", response_model=InventoryOut)
async def update_inventory_endpoint(inventory_id: int, inventory_data: InventoryUpdate):
    updated_inventory = await update_inventory(inventory_id, inventory_data)
    if not updated_inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return updated_inventory


@InventoryRouter.delete("/{inventory_id}")
async def delete_inventory_endpoint(inventory_id: int):
    deleted_count = await delete_inventory(inventory_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"message": "Inventory deleted successfully"}
