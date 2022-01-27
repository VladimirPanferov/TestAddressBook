from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    FIO = Column(String, unique=True)
    avatar = Column(String, unique=True, nullable=True)
    sex = Column(String)
    birthdate = Column(Date)
    address = Column(String, nullable=True)


class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    kind = Column(String)
    phone_number = Column(String)

    user = relationship("User", backref="phones")


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    kind = Column(String)
    email = Column(String)

    user = relationship("User", backref="emails")
