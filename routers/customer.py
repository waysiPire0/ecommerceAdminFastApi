from fastapi import APIRouter, HTTPException
from schemas.CustomerSchema import CustomerCreate, CustomerOut, CustomerUpdate
from configs.environment import get_environment_variables
from .auth import get_current_user
from services.CustomerService import (
    create_customer,
    get_customer,
    update_customer,
    delete_customer,
    get_all_customers,
)
from typing import List


env = get_environment_variables()

CustomerRouter = APIRouter(prefix=f"/{env.API_VERSION}/customer", tags=["Customers"])


@CustomerRouter.get("/customers", response_model=List[CustomerOut])
async def get_all_customers_endpoint():
    customers = await get_all_customers()
    return customers


@CustomerRouter.post("/", response_model=CustomerOut)
async def create_customer_endpoint(customer: CustomerCreate):
    new_customer = await create_customer(customer)
    return new_customer


@CustomerRouter.get("/{customer_id}", response_model=CustomerOut)
async def get_customer_endpoint(customer_id: int):
    customer = await get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@CustomerRouter.put("/{customer_id}", response_model=CustomerOut)
async def update_customer_endpoint(customer_id: int, customer_data: CustomerUpdate):
    updated_customer = await update_customer(customer_id, customer_data)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer


@CustomerRouter.delete("/{customer_id}")
async def delete_customer_endpoint(customer_id: int):
    deleted_count = await delete_customer(customer_id)
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"message": "Customer deleted successfully"}
