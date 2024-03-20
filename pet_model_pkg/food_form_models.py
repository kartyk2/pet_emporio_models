from sqlalchemy.orm import declarative_base
from enum import Enum
from sqlalchemy import func, Column
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy_utils import ChoiceType
from uuid import uuid4
from datetime import datetime

food_form_base= declarative_base()

class FoodForm(Enum):
    DRYFOOD:str = "dry_food"
    WETFOOD:str = "wet_food"
    FOODTOPPING:str = "food_topping"
    FREEZEDRIED:str = "freezedried"
    TREATS:str = "treats"
    SUPPLIMENTS:str = "suppliments"
    DEHYDRATED:str = "dehydrated"
 
 
class FoodFormModel(food_form_base):
    __tablename__="foodform"
    id = Column(UUID(as_uuid=True),default= uuid4,primary_key=True)
    food_form_name= Column(ChoiceType(choices=FoodForm))
    created_at = Column(TIMESTAMP,default=datetime.now)
    updated_at = Column(TIMESTAMP,default=datetime.now,onupdate=datetime.now)