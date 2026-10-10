from fastapi import APIRouter

users = [
    {
        "name":"Saurabh",
        "role": "viewer"
    },
    {
        "name": "Admin",
        "role": "admin"
    }
]

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def list_users():
    return users
