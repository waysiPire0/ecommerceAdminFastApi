from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from configs.environment import get_environment_variables
from routers.admin import AdminRouter
from routers.auth import AuthRouter
from routers.product import ProductRouter
from routers.category import CategoryRouter

env = get_environment_variables()

app = FastAPI(title=env.APP_NAME, version=env.API_VERSION)

# Add Routers
app.include_router(AdminRouter)
app.include_router(AuthRouter)
app.include_router(ProductRouter)
app.include_router(CategoryRouter)

register_tortoise(
    app,
    db_url=f"mysql://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}/{env.DB_NAME}",
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
