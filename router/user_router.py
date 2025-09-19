from fastapi import APIRouter
from schema.userschema import Follow, BlockData
from controller.user import (follow_user,unfollow,block_user,unblock,checkFollowers,checkFollowing)

router = APIRouter()

@router.post("/follow")
def follow(data: Follow):
    return follow_user(data)

@router.post("/unfollow")
def unfollow_user(data: Follow):
    return unfollow(data)

@router.get("/followers/{user_id}")
def read_followers(user_id: int):
    return checkFollowers(user_id)

@router.get("/following/{user_id}")
def read_following(user_id: int):
    return checkFollowing(user_id)

@router.post("/block")
def block(data: BlockData):
    return block_user(data)

@router.post("/unblock")
def unblock_user(data: BlockData):
    return unblock(data)


