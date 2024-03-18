from sqlalchemy import Engine
from pet_model_pkg.brand_model import Base1
from pet_model_pkg.product_models import Base2


def create_models(engine: Engine):
    """
    create all the table in the package into the DB corresponding to the engine 
    """
    Base1.metadata.create_all(bind= engine)
    Base2.metadata.create_all(bind= engine)
    