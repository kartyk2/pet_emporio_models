from sqlalchemy import Column, String, UUID, ForeignKey, Boolean , TIMESTAMP, func, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import Integer
import uuid

Base2= declarative_base()

class ProductDetails(Base2):
    __tablename__ = "product_details"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(String)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    pet_life_stage = Column(String, nullable=False)
    category_id = Column(ARRAY(UUID), default=[])
    sub_category_id = Column(ARRAY(UUID), default=[])
    brand_id=  Column(ARRAY(UUID), default=[])
    is_published = Column(Boolean)
    is_active = Column(Boolean)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())


class ProductInventory(Base2):
    __tablename__ = "product_inventory"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID,ForeignKey(ProductDetails.id))
    quantity_on_stock = Column(String)
    available_quantity = Column(String)
    supply_chain = Column(String)
    expected_restock = Column(String)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

class ProductImages(Base2):
    __tablename__ = 'product_images'
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID,ForeignKey(ProductDetails.id))
    product_image = ""
    added_on =Column(TIMESTAMP, default=func.now())


class Variant(Base2):
    __tablename__="variant"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID,ForeignKey(ProductDetails.id))
    variant_name=Column(String)
    unit_of_measure= Column(String)
    available_unit=Column(Integer)
    is_avl=Column(Boolean)
    avl_quantity= Column(Integer)
    expected_restock= Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())


class ProductReview(Base2):
    __tablename__="productreview"
    id=   id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID,ForeignKey(ProductDetails.id))
    customer_id = Column(UUID,ForeignKey(ProductDetails.id))
    review_language=Column(String)
    content=Column(String)
    rating= Column(Integer)
    created_at=Column(TIMESTAMP)