from sqlalchemy import func, Column, String, UUID, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid

pet_and_brand_base = declarative_base()


class Pet(pet_and_brand_base):
    __tablename__ = "pet"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    icon = Column(String, unique=True)
    name = Column(String)
    production_status = Column(Boolean, default=False)
    uat_status = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    is_approved = Column(Boolean, default=False)


class Brand(pet_and_brand_base):
    __tablename__ = "brand"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    logo = Column(String, default="path")
    production_status = Column(Boolean, default=False)
    uat_status = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    is_approved = Column(Boolean, default=False)


class PetAndBrand(pet_and_brand_base):
    __tablename__ = "petbrand"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pet_id = Column(UUID(as_uuid=True), ForeignKey(Pet.id))
    brand_id = Column(UUID(as_uuid=True), ForeignKey(Brand.id))


class Category(pet_and_brand_base):
    __tablename__ = "category"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pet_id = Column(
        UUID(as_uuid=True), ForeignKey(Pet.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    name = Column(String, unique=True)
    is_active = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    is_approved = Column(Boolean, default=False)


class SubCategory(pet_and_brand_base):
    __tablename__ = "sub_category"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pet_id = Column(
        UUID(as_uuid=True), ForeignKey(Pet.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey(Category.id, ondelete="CASCADE", onupdate="CASCADE"),
    )
    name = Column(String, unique=True)
    is_active = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now)
    updated_at = Column(TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    is_approved = Column(Boolean, default=False)
