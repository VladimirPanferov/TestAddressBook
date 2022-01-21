from typing import (
    List,
    Optional,
)

from fastapi import Depends
from sqlalchemy.orm import Session

import tables
from database import get_session


class UserService:
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session
        
    def get_users(self) -> List[tables.User]:
        users = (
            self.session
            .query(tables.User)
            .all()
        )
        return users
