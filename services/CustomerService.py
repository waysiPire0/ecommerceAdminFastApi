from schemas.CustomerSchema import CustomerCreate, CustomerUpdate
from models.models import Customer
from tortoise.exceptions import DoesNotExist


async def get_all_customers():
    return await Customer.all()


async def create_customer(customer_data: CustomerCreate):
    customer = await Customer.create(**customer_data.dict())
    return customer


async def get_customer(customer_id: int):
    try:
        return await Customer.get(customer_id=customer_id)
    except DoesNotExist:
        return None


async def update_customer(customer_id: int, customer_data: CustomerUpdate):
    await Customer.filter(customer_id=customer_id).update(
        **customer_data.dict(exclude_unset=True)
    )
    updated_customer = await Customer.get(customer_id=customer_id)
    return updated_customer


async def delete_customer(customer_id: int):
    deleted_count = await Customer.filter(customer_id=customer_id).delete()
    return deleted_count
