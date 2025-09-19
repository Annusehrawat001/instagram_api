from fastapi import HTTPException

user_db = [
    {"id": 1, "username": "Annu", "email": "annu@gmail.com"},
    {"id": 2, "username": "Kalu", "email": "kalu@gmail.com"}
]

follows_db = []

# Follow a user
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
    return [f["follower_id"] for f in follows_db if f["following_id"] == user_id]


def get_following(user_id):
    return [f["following_id"] for f in follows_db if f["follower_id"] == user_id]


def unfollow(data):
    for f in follows_db:
        if f["follower_id"] == data.follower_id and f["following_id"] == data.following_id:
            follows_db.remove(f)
            return {"message": f"{data.follower_id} unfollowed {data.following_id}"}
    raise HTTPException(status_code=404, detail="Follow relationship not found")


#  Block 
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


def unblock(data):
    for b in blocks_db:
        if b["blocker_id"] == data.blocker_id and b["blocked_id"] == data.blocked_id:
            blocks_db.remove(b)
            return {"message": f"User {data.blocker_id} unblocked {data.blocked_id}"}
    raise HTTPException(status_code=404, detail="Block relationship not found")


#  Followers / Following check 
def checkFollowers(id):
    users = [f["follower_id"] for f in follows_db if f["following_id"] == id]

    if len(users) > 0:
        for u in blocks_db:
            if u["blocked_id"] == id or u["blocker_id"] == id:
                if u["blocked_id"] in users:
                    users.remove(u["blocked_id"])
                if u["blocker_id"] in users:
                    users.remove(u["blocker_id"])

    if len(users) > 0:
        return {
            "success": True,
            "status": 200,
            "msg": "Followers fetched successfully",
            "total_followers": len(users),
            "followers": users
        }
    raise HTTPException(status_code=200, detail="No one has followed you yet")


def checkFollowing(id):
    users = [f["following_id"] for f in follows_db if f["follower_id"] == id]

    if len(users) > 0:
        for u in blocks_db:
            if u["blocked_id"] == id or u["blocker_id"] == id:
                if u["blocked_id"] in users:
                    users.remove(u["blocked_id"])
                if u["blocker_id"] in users:
                    users.remove(u["blocker_id"])

    if len(users) > 0:
        return {
            "success": True,
            "status": 200,
            "msg": "Following fetched successfully",
            "total_following": len(users),
            "following": users
        }
    raise HTTPException(status_code=200, detail="You haven't followed anyone yet")
