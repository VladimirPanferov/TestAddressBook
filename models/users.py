from datetime import date
from enum import Enum
from typing import (
    List,
    Optional
)

from pydantic import BaseModel


class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class PhoneKind(str, Enum):
    LANDLINE = "landline"
    MOBILE = "mobile"


class EMailKind(str, Enum):
    WORD = "work"
    HOME = "home"


class PhoneBase(BaseModel):
    kind: PhoneKind
    phone_number: str


class Phone(PhoneBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class EMailBase(BaseModel):
    kind: EMailKind
    email: str


class EMail(EMailBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class BaseUser(BaseModel):
    FIO: str
    avatar: str
    sex: Sex
    birthdate: date
    address: Optional[str] = ""
    phones: Optional[List[PhoneBase]] = []
    emails: Optional[List[EMailBase]] = []


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass


class User(BaseUser):
    id: int
    phones: Optional[List[Phone]] = []
    emails: Optional[List[EMail]] = []

    class Config:
        orm_mode = True
