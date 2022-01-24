from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class BaseUser(BaseModel):
    FIO: str
    avatar: str
    sex: Sex
    birthdate: date
    address: Optional[str]


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
