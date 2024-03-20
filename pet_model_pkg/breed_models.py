from sqlalchemy.orm import declarative_base
from enum import Enum
from sqlalchemy import func, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from datetime import datetime

breed_base = declarative_base()


class BreedSize(Enum):
    EXTRASMALL:str = "extra_small"
    SMALL:str = "small"
    MEDIUM:str = "medium"
    LARGE:str = "large"
    GIANT:str = "giant"


class BreedSizeModel(breed_base):
    __tablename__ = "breed_size"
    id = Column(UUID(as_uuid=True), default= uuid4, primary_key=True)
    breed_size_name = Column(ChoiceType(BreedSize), default=BreedSize.SMALL.value)
    created_at = Column(TIMESTAMP, default=func.now)
    updated_at = Column(TIMESTAMP, default=func.now, onupdate=func.now)
