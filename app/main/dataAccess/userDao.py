from . import databaseInstance

def getByEmail(email):
    users = databaseInstance.users
    return users.find_one({"email": email})

def addUser(user):
    users = databaseInstance.users
    return users.insert_one(user.toString()).inserted_id

def updateUser(userId, user, updatedUserData):
    users = databaseInstance.users
    user.update(updatedUserData)
    users.replace_one({"_id": userId}, user)