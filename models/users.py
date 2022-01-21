from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"


class User(BaseModel):
    FIO: str
    avatar: str
    sex: Sex
    birthdate: date
    address: Optional[str]
