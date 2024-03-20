from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    Boolean,
    TIMESTAMP,
    func,
    ARRAY,
    FLOAT,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.sqltypes import Integer
from datetime import datetime
import uuid

product_base = declarative_base()


class ProductDetails(product_base):
    __tablename__ = "product_details"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(String)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    pet_life_stage = Column(String)
    category_id = Column(ARRAY(UUID), default=[])
    sub_category_id = Column(ARRAY(UUID), default=[])
    brand_id = Column(ARRAY(UUID), default=[])
    is_published = Column(Boolean)
    is_active = Column(Boolean)
    created_at = Column(TIMESTAMP, default= datetime.now)
    updated_at = Column(TIMESTAMP, default= datetime.now, onupdate= datetime.now)


class ProductInventory(product_base):
    __tablename__ = "product_inventory"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID, ForeignKey(ProductDetails.id))
    quantity_on_stock = Column(String)
    available_quantity = Column(String)
    supply_chain = Column(String)
    expected_restock = Column(String)
    created_at = Column(TIMESTAMP, default= datetime.now)
    updated_at = Column(TIMESTAMP, default= datetime.now, onupdate= datetime.now)


class ProductImages(product_base):
    __tablename__ = "product_images"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID, ForeignKey(ProductDetails.id))
    product_image = Column(String,)
    added_on = Column(TIMESTAMP, default= datetime.now)


class Variant(product_base):
    __tablename__ = "variant"
    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID, ForeignKey(ProductDetails.id))
    variant_name = Column(String, nullable= False)
    unit_of_measure = Column(String, nullable= False)
    available_unit = Column(Integer, nullable= False)
    is_avl = Column(Boolean)
    avl_quantity = Column(Integer)
    expected_restock = Column(TIMESTAMP)
    is_default= Column(Boolean, default= False)

    created_at = Column(TIMESTAMP, default= datetime.now)
    updated_at = Column(TIMESTAMP, default= datetime.now, onupdate= datetime.now)


class ProductReview(product_base):
    __tablename__ = "productreview"
    id = id = Column(UUID, default=uuid.uuid1, primary_key=True)
    product_id = Column(UUID, ForeignKey(ProductDetails.id))
    customer_id = Column(UUID, ForeignKey(ProductDetails.id))
    review_language = Column(String)
    content = Column(String)
    rating = Column(FLOAT)
    created_at = Column(TIMESTAMP)
