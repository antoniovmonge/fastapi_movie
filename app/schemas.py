from pydantic import BaseModel, Field
from typing import Optional


class MovieSchema(BaseModel):
    id: Optional[str] = None
    title: str = Field(min_length=2, max_length=50)
    description: Optional[str] = Field(max_length=150)
    year: int = Field(le=2024)
    rating: Optional[float] = Field(ge=0.0, le=10.0)
    category: str = Field(min_length=2, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1",
                "title": "New Film",
                "description": "Description",
                "year": 2021,
                "rating": 5.0,
                "category": "Unclassified",
            }
        }
