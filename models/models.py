from tortoise import models, fields
from tortoise.contrib.pydantic import pydantic_model_creator
from datetime import datetime


class Product(models.Model):
    product_id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    # category = fields.ForeignKeyField("models.Category", related_name="products")
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "products"


class Category(models.Model):
    category_id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    class Meta:
        table = "categories"


class AdminUser(models.Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=20, null=False, unique=True)
    email = fields.CharField(max_length=200, null=False, unique=True)
    password = fields.CharField(max_length=255, null=False)
    created_at = fields.DatetimeField(default=datetime.utcnow)


# admin user pydanti
AdminUser_Pydantic = pydantic_model_creator(
    AdminUser,
    name="AdminUser",
    exclude=("id"),
)
AdminUser_PydanticIn = pydantic_model_creator(
    AdminUser,
    name="AdminUser_PydanticIn",
    exclude_readonly=True,
    exclude=(
        "id",
        "created_at",
    ),
)
AdminUser_PydanticOut = pydantic_model_creator(
    AdminUser, name="AdminUser_PydanticOut", exclude=("password",)
)
