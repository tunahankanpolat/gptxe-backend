from . import db

def getByEmail(email):
    users = db.users
    return users.find_one({"email": email})

def addUser(user):
    users = db.users
    return users.insert_one(user.toString()).inserted_id

def updateUser(userId, user, updatedUserData):
    users = db.users
    user.update(updatedUserData)
    users.replace_one({"_id": userId}, user)