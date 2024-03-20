from sqlalchemy import func, Column, String, UUID, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy_utils import ChoiceType
from enum import Enum
import uuid

user_base = declarative_base()


class ROLE_TYPES(Enum):
    ADMIN:str = 'admin'
    USER: str = 'user'
    DOCTOR: str = 'doctor'


class User(user_base):
    __tablename__ = "user"
    user_id = Column(String, primary_key=True, unique=True)
    role = Column(ChoiceType(ROLE_TYPES), default=ROLE_TYPES.USER)
    email = Column(String)
    password = Column(String)
    profile_picture = Column(String)
    is_social = Column(Boolean, default=False)

    created_at = Column(TIMESTAMP, default=func.now)
    updated_at = Column(TIMESTAMP, default=func.now, onupdate=func.now)


class SocialUser(user_base):
    __tablename__ = "social_user"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    user_id = Column(String, ForeignKey(User.user_id))
    provider = Column(String)
    provider_uid = Column(String)
