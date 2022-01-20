from re import A
from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"]
)
