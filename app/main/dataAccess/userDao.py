from . import db
from flask import current_app as app

def getByEmail(email):
    users = db.users
    return users.find_one({"email": email})

def addUser(user):
    if not app.config.get("TESTING"):
        users = db.users
        return users.insert_one(user.toString()).inserted_id

def updateUser(userId, user, updatedUserData):
    if not app.config.get("TESTING"):
        users = db.users
        user.update(updatedUserData)
        users.replace_one({"_id": userId}, user)