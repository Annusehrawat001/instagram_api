from fastapi import APIRouter
from schema.userschema import Follow,BlockData
from controller.user import follow_user, get_followers, get_following,block_user, get_blocked_list

router = APIRouter()

# Follow a user
@router.post("/follow/n")
def follow(data: Follow):
    result = follow_user(data)
    return result

#  Followers of a user
@router.get("/followers/{user_id}")
def read_followers(user_id: str):
    return get_followers(user_id)

# Following of a user
@router.get("/following/{user_id}")
def read_following(user_id: str):
    return get_following(user_id)

@router.post("/block")
def block(data: BlockData):
    return block_user(data)

@router.get("/blocked/{user_id}")
def read_blocked_list(user_id: int):
    return get_blocked_list(user_id)
