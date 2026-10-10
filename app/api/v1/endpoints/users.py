from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from uuid import uuid4
from enum import Enum


class Role(Enum):
    viewer = "viewer"
    editor = "editor"
    admin = "admin"


users = [
    {
        "id": "ed38f5d9-a1c3-49a3-88fa-29b3f9b27770",
        "name": "Saurabh",
        "role": Role.viewer,
    },
    {"id": "3c9dfd9b-b522-4d72-89ac-cf5e7b04eeca", "name": "Admin", "role": Role.admin},
]


class UserCreate(BaseModel):
    name: str
    role: str


class UserIDResponse(BaseModel):
    user_id: str


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK)
def list_users(role: Role | None = None):
    if role is None:
        return users
    return [user for user in users if user["role"] == role]


@router.post("/")
def create_user(new_user: UserCreate):
    new_user_id = str(uuid4())
    users.append({"id": new_user_id, "name": new_user.name, "role": new_user.role})
    return UserIDResponse(user_id=new_user_id)


@router.get("/{id}")
def get_user(id: str):
    for user in users:
        if user.get("id") == id:
            return user
    raise HTTPException(detail="User not found", status_code=404)


@router.delete("/{id}")
def delete_user(id: str):
    if any([True if user.get("id") == id else False for user in users]):
        users = [user for user in users if user.get("id") != id]
    else:
        raise HTTPException(
            detail="Cannot delete user, User not found", status_code=404
        )
