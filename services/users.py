from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    status,
    HTTPException,
)
from sqlalchemy.orm import Session

import tables
from models import users as user_models
from database import get_session


class UserService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def get_many(self) -> List[tables.User]:
        users = (
            self.session
            .query(tables.User)
            .join(
                tables.Phone,
                tables.Phone.user_id == tables.User.id,
                isouter=True,
            )
            .all()
        )
        return users

    def get(self, user_id: int) -> Optional[tables.User]:
        user = (
            self.session
            .query(tables.User)
            .filter(
                tables.User.id == user_id
            )
            .first()
        )
        if not user:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return user

    def create(self, user_data: user_models.UserCreate) -> tables.User:
        phones = user_data.phones
        user_dict = user_data.dict()
        user_dict.pop("phones")

        user = tables.User(
            **user_dict,
        )
        self.session.add(user)
        self.session.flush()

        for phone in phones:
            self.create_phone(user_id=user.id, phone=phone)

        self.session.commit()
        return user

    def create_phone(self, user_id: int, phone: user_models.PhoneBase):
        user_phone = tables.Phone(
            **phone.dict(),
            user_id=user_id,
        )
        self.session.add(user_phone)

    def update(
        self,
        user_id: int,
        user_data: user_models.UserUpdate,
    ) -> tables.User:
        user = self.get(user_id)
        for field, value in user_data:
            setattr(user, field, value)
        self.session.commit()
        return user

    def delete(self, user_id: int) -> None:
        user = self.get(user_id=user_id)
        self.session.delete(user)
        self.session.commit()
