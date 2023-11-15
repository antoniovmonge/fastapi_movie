from pydantic import BaseModel, Field
from typing import Optional


class UserSchema(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=4, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {"email": "user@email.com", "password": "pass_1234"}
        }
    }


class MovieSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, max_length=50)
    description: Optional[str] = Field(max_length=150)
    year: int = Field(le=2024)
    rating: Optional[float] = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=2, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Matrix",
                "description": "A computer hacker learns from mysterious rebels about the true nature of his reality.",
                "year": 1999,
                "rating": 8.7,
                "category": "Sci-Fi",
            }
        }
    }
