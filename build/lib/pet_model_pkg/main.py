from sqlalchemy import Engine, text
from pet_model_pkg.brand_model import pet_and_brand_base
from pet_model_pkg.breed_models import breed_base
from pet_model_pkg.food_form_models import food_form_base
from pet_model_pkg.product_models import product_base
from pet_model_pkg.user_model import user_base
from pet_model_pkg.lifestage_model import lifestage_base
from pet_model_pkg.special_diet_models import special_diet_base

from pet_model_pkg.breed_models import BreedSize
from pet_model_pkg.food_form_models import FoodForm
from pet_model_pkg.lifestage_model import LifeStage
from pet_model_pkg.special_diet_models import SpecialDiet

from uuid import uuid4

def create_models(engine: Engine):
    """
    create all the table in the package into the DB corresponding to the engine 
    """
    pet_and_brand_base.metadata.create_all(bind= engine)
    breed_base.metadata.create_all(bind= engine)
    food_form_base.metadata.create_all(bind= engine)
    product_base.metadata.create_all(bind= engine)
    user_base.metadata.create_all(bind= engine)
    lifestage_base.metadata.create_all(bind= engine)
    special_diet_base.metadata.create_all(bind= engine)


def insert_basic_data(engine: Engine):
    with engine.connect() as cnx:

        """
        insert breed size data
        """
        for data in BreedSize:
            add_breed = cnx.execute(
                text("INSERT INTO public.breed_size("
                    "id, breed_size_name) "
                    "VALUES (:id, :breed_size_name);"),
                {
                    "id": uuid4(),
                    "breed_size_name": data.value,
                }
            )

        """
        insert food_form_name data
        """
        for data in FoodForm:
            add_breed = cnx.execute(
                text("INSERT INTO public.foodform("
                    "id, food_form_name) "
                    "VALUES (:id, :food_form_name);"),
                {
                    "id": uuid4(),
                    "food_form_name": data.value,
                }
            )

        """
        insert special diet data
        """
        for data in FoodForm:
            add_breed = cnx.execute(
                text("INSERT INTO public.lifestage("
                    "id, life_stage_name) "
                    "VALUES (:id, :life_stage_name);"),
                {
                    "id": uuid4(),
                    "life_stage_name": data.value,
                }
            )

        """
        insert special diet data
        """
        for data in FoodForm:
            add_breed = cnx.execute(
                text("INSERT INTO public.specialdiet("
                    "id, special_diet_name) "
                    "VALUES (:id, :special_diet_name);"),
                {
                    "id": uuid4(),
                    "special_diet_name": data.value,
                }
            )