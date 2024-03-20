from sqlalchemy.orm import declarative_base
from enum import Enum
from sqlalchemy import func, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from datetime import datetime

lifestage_base = declarative_base()

 
class LifeStages(Enum):
    PUPPY:str = "puppy"
    KITTEN:str = "kitten"
    ADULT:str = "adult"
    SENIOR:str = "senior" 
    
 
class LifeStage(lifestage_base):
    __tablename__ = "lifestage"    
    id = Column(UUID(as_uuid=True),default= uuid4,primary_key=True)
    life_stage_name = Column(ChoiceType(choices=LifeStages), nullable= False)
    created_at = Column(TIMESTAMP,default=datetime.now)
    updated_at = Column(TIMESTAMP,default=datetime.now, onupdate=datetime.now)