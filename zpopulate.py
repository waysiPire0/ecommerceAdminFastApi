import asyncio
from tortoise import Tortoise, run_async
from models.models import Product, Category, Inventory, Sale, Customer, AdminUser
from datetime import datetime, timedelta
import random
from configs.environment import get_environment_variables

env = get_environment_variables()


async def populate_demo_data():
    db_url = f"mysql://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}/{env.DB_NAME}"

    await Tortoise.init(db_url=db_url, modules={"models": ["models.models"]})
    await Tortoise.generate_schemas()

    # Create Categories
    categories = ["Electronics", "Clothing", "Home Appliances", "Books", "Toys"]
    for name in categories:
        await Category.create(name=name, description=f"{name} description")

    # Create Products
    for i in range(1, 21):
        category = await Category.get(category_id=random.randint(1, len(categories)))
        await Product.create(
            name=f"Product {i}",
            description=f"Description for product {i}",
            price=random.uniform(10.0, 500.0),
            category=category,
        )

    # Create Customers
    for i in range(1, 11):
        await Customer.create(
            name=f"Customer {i}",
            email=f"customer{i}@example.com",
            phone=f"123456789{i}",
            address=f"Address {i}",
        )

    # Create Sales
    for i in range(1, 16):
        product = await Product.get(product_id=random.randint(1, 20))
        customer = await Customer.get(customer_id=random.randint(1, 10))
        quantity = random.randint(1, 5)
        await Sale.create(
            product=product,
            quantity=quantity,
            sale_date=datetime.now() - timedelta(days=random.randint(0, 10)),
            total_price=product.price * quantity,
            customer=customer,
        )

    # Create Inventory Records
    for i in range(1, 21):
        product = await Product.get(product_id=i)
        await Inventory.create(
            product=product,
            quantity_available=random.randint(0, 100),
            low_stock_threshold=random.randint(10, 20),
        )

    print("Demo data populated successfully!")


if __name__ == "__main__":
    run_async(populate_demo_data())
