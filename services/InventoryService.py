from schemas.InventorySchema import InventoryCreate, InventoryUpdate
from models.models import Inventory
from tortoise.exceptions import DoesNotExist


async def get_all_inventories():
    return await Inventory.all()


async def create_inventory(inventory_data: InventoryCreate):
    inventory = await Inventory.create(**inventory_data.dict())
    return inventory


async def get_inventory(inventory_id: int):
    try:
        return await Inventory.get(inventory_id=inventory_id)
    except DoesNotExist:
        return None


async def update_inventory(inventory_id: int, inventory_data: InventoryUpdate):
    await Inventory.filter(inventory_id=inventory_id).update(
        **inventory_data.dict(exclude_unset=True)
    )
    updated_inventory = await Inventory.get(inventory_id=inventory_id)
    return updated_inventory


async def delete_inventory(inventory_id: int):
    deleted_count = await Inventory.filter(inventory_id=inventory_id).delete()
    return deleted_count
