from pydantic import BaseModel
class Follow(BaseModel):
    following_id:int
    follower_id:int

class BlockData(BaseModel):
    blocker_id: int
    blocked_id: int
