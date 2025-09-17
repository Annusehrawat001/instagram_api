from pydantic import BaseModel
class Follow(BaseModel):
    following_username:str
    follower_username:str

class BlockData(BaseModel):
    blocker_id: int
    blocked_id: int
