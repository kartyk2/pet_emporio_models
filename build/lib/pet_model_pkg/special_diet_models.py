from sqlalchemy.orm import declarative_base
from enum import Enum
from sqlalchemy import func, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from datetime import datetime

special_diet_base= declarative_base()

class SpecialDiet(Enum):
    CHICKENFREE= "chicken_free"
    FLAXFREE= "flax_free"
    GLUTENFREE= "gluten_free"
    GRAINFREE= "gain_free" 
    HIGHFIBER= "high_fiber"
    HIGHPROTEIN= "high_protein" 
 
 
class SpecialDietModel(special_diet_base):
    __tablename__ = "specialdiet"
    id = Column(UUID(as_uuid=True),default= uuid4,primary_key=True)
    special_diet_name = Column(ChoiceType(choices=SpecialDiet))
    created_at = Column(TIMESTAMP,default=datetime.now)
    updated_at = Column(TIMESTAMP,default=datetime.now, onupdate=datetime.now)