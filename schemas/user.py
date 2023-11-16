from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=4, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {"email": "user@email.com", "password": "pass_1234"}
        }
    }
