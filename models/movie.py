from config.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Float,
)


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
