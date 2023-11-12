from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Admin(models.Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    password_hash = fields.CharField(max_length=255)
    role = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)


class Product(models.Model):
    product_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    category = fields.ForeignKeyField("models.Category", related_name="products")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class Category(models.Model):
    category_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()


class Sale(models.Model):
    sale_id = fields.IntField(pk=True)
    product = fields.ForeignKeyField("models.Product", related_name="sales")
    quantity = fields.IntField()
    sale_date = fields.DatetimeField()
    total_price = fields.DecimalField(max_digits=10, decimal_places=2)
    customer = fields.ForeignKeyField("models.Customer", related_name="sales")


class Customer(models.Model):
    customer_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=255)
    address = fields.TextField()


class Inventory(models.Model):
    inventory_id = fields.IntField(pk=True)
    product = fields.ForeignKeyField("models.Product", related_name="inventory")
    quantity_available = fields.IntField()
    low_stock_threshold = fields.IntField()
    last_updated = fields.DatetimeField(auto_now=True)
