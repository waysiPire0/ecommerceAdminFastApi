from fastapi import APIRouter, Depends
from models.models import *
from services.AuthService import *
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from configs.environment import get_environment_variables
import jwt

env = get_environment_variables()

oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

AuthRouter = APIRouter(prefix="", tags=["auth"])


@AuthRouter.post("/token")
async def generate_token(request_form: OAuth2PasswordRequestForm = Depends()):
    token = await token_generator(request_form.username, request_form.password)
    return {"access_token": token, "token_type": "bearer"}


async def get_current_user(token: str = Depends(oath2_scheme)):
    try:
        payload = jwt.decode(token, env.SECRET, algorithms=["HS256"])
        user = await AdminUser.get(id=payload.get("id"))
        return await user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
