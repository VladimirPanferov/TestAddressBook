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
from database import get_session


class UserService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session
        
    def get_many(self) -> List[tables.User]:
        users = (
            self.session
            .query(tables.User)
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
    
    def delete(self, user_id: int) -> None:
        user = self.get(user_id=user_id)
        self.session.delete(user)
        self.session.commit()
