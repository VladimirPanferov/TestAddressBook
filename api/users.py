from typing import List

from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session

from database import get_session
from models.users import User
from services.users import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", response_model=List[User])
def get_users(user_service: UserService = Depends()):
    return user_service.get_users()
