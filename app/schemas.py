from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from pydantic import BaseModel, Field
from typing import Optional

from utils.jwt_manager import validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "user@email.com":
            raise HTTPException(status_code=401, detail="Unauthorized")


class UserSchema(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=4, max_length=50)


class MovieSchema(BaseModel):
    id: Optional[str] = None
    title: str = Field(min_length=2, max_length=50)
    description: Optional[str] = Field(max_length=150)
    year: int = Field(le=2024)
    rating: Optional[float] = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=2, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "x",
                "title": "The Matrix",
                "description": "A computer hacker learns from mysterious rebels about the true nature of his reality.",
                "year": 1999,
                "rating": 8.7,
                "category": "Sci-Fi",
            }
        }
    }

    def to_dict(self):
        return self.model_dump()
