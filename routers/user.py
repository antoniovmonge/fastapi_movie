from fastapi import APIRouter
from fastapi.responses import JSONResponse


from schemas import UserSchema
from utils.jwt_manager import create_token

users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post("/login", status_code=200)
def login(user: UserSchema):
    if user.email == "user@email.com" and user.password == "pass_1234":
        token = create_token(user.model_dump())
        return JSONResponse(status_code=200, content={"token": token})
