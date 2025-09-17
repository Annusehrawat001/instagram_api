from fastapi import HTTPException

user_db = [
    {"id": 1, "username": "Annu", "email": "annu@gmail.com"},
    {"id": 2, "username": "Kalu", "email": "kalu@gmail.com"}
]

follows_db = []

# ➤ Follow a user
def follow_user(data):
    if data.follower_id == data.following_id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    for f in follows_db:
        if f["follower_id"] == data.follower_id and f["following_id"] == data.following_id:
            raise HTTPException(status_code=400, detail="Already following this user")

    follows_db.append({
        "follower_id": data.follower_id,
        "following_id": data.following_id
    }) 
    return {"follower_id": data.follower_id, "following_id": data.following_id}

def get_followers(user_id):
    followers = []
    for f in follows_db:
        if f["following_id"] == user_id:
            followers.append(f["follower_id"])
    return followers

def get_following(user_id):
    following = []
    for f in follows_db:
        if f["follower_id"] == user_id:
            following.append(f["following_id"])
    return following

blocks_db = []

def block_user(data):
    if data.blocker_id == data.blocked_id:
        raise HTTPException(status_code=400, detail="You cannot block yourself")
    for b in blocks_db:
        if b["blocker_id"] == data.blocker_id and b["blocked_id"] == data.blocked_id:
            raise HTTPException(status_code=400, detail="Already blocked this user")
    blocks_db.append({
        "blocker_id": data.blocker_id,
        "blocked_id": data.blocked_id
    })
    return {"blocker_id": data.blocker_id, "blocked_id": data.blocked_id}

def get_blocked_list(user_id):
    blocked_users = []
    for b in blocks_db:
        if b["blocker_id"] == user_id:
            blocked_users.append(b["blocked_id"])
    return blocked_users
