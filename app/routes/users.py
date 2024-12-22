from fastapi import APIRouter, HTTPException

router = APIRouter()

# In-memory database
users_db = []

@router.post("/")
def create_user(user: dict):
    users_db.append(user)
    return user

@router.get("/")
def list_users():
    return users_db

@router.get("/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
def update_user(user_id: int, updated_user: dict):
    for user in users_db:
        if user["id"] == user_id:
            user.update(updated_user)
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: int):
    global users_db
    users_db = [user for user in users_db if user["id"] != user_id]
    return {"message": "User deleted successfully"}
