from passlib.context import CryptContext
from fastapi import HTTPException, status
from models.models import *
from configs.environment import get_environment_variables
import jwt

env = get_environment_variables()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate(username: str, password: str):
    user = await AdminUser.get(username=username)
    if user and verify_password(password, user.password):
        return user
    return False


async def token_generator(username: str, password: str):
    user = await authenticate(username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        token_data = {
            "id": user.id,
            "username": user.username,
        }
        token = jwt.encode(token_data, env.SECRET)
        return token
