from typing import List
from fastapi import (
    APIRouter,
    Depends,
    status,
    Response,
)
from sqlalchemy.orm import Session

from database import get_session
from models.users import User, UserCreate
from services.users import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/", response_model=List[User])
def get_users(user_service: UserService = Depends()):
    return user_service.get_many()


@router.put("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, user_service: UserService = Depends()):
    return user_service.create(
        user_data,
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT,)
def delete_user(user_id: int, user_service: UserService = Depends(),):
    user_service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
