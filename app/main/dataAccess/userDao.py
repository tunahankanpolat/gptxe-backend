class UserDao:
    def __init__(self, databaseInstance):
        self.databaseInstance = databaseInstance

    def getByEmail(self, email):
        users = self.databaseInstance.users
        return users.find_one({"email": email})

    def addUser(self, user):
        users = self.databaseInstance.users
        return users.insert_one(user.toString()).inserted_id

    def updateUser(self, userId, user, updatedUserData):
        users = self.databaseInstance.users
        user.update(updatedUserData)
        users.replace_one({"_id": userId}, user)