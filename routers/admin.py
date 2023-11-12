from fastapi import APIRouter, Depends, status
from models.models import *
from services.AuthService import *
from configs.environment import get_environment_variables
from .auth import get_current_user


env = get_environment_variables()

AdminRouter = APIRouter(prefix=f"/{env.API_VERSION}/admin", tags=["admin"])


@AdminRouter.post("/login")
async def user_login(user: AdminUser_PydanticIn = Depends(get_current_user)):
    admin_user = await AdminUser.get(id=user.id)
    return {
        "status": "ok",
        "data": {
            "user_id": admin_user.id,
            "username": admin_user.username,
            "email": admin_user.email,
            "created_at": admin_user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        },
    }


@AdminRouter.post("/signup")
async def register(user: AdminUser_PydanticIn):
    user_info = user.dict()
    user_info["password"] = get_hash_password(user_info["password"])
    user_obj = await AdminUser.create(**user_info)
    new_user = await AdminUser_Pydantic.from_tortoise_orm(user_obj)
    print(new_user)
    return {
        "status": "ok",
        "data": f"User is created with username {new_user.username}",
    }
