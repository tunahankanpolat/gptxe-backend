from app.main.model.user import User
from flask_jwt_extended import create_access_token
from app.main.dataAccess import userDao
from werkzeug.security import check_password_hash, generate_password_hash

class UserService:
    def signUp(self, email, password):     
        if email and password:
            if userDao.getByEmail(email):
                return {"error": "The e-mail address is already registered."}, 400
            
            user = User(email,generate_password_hash(password))
            userDao.addUser(user)
            accessToken = create_access_token(identity=email)
            return {"access_token": accessToken}, 200
        else:
            return {"error": "Email and password fields are required."}, 400
    
    def logIn(self, email, password):
        if email and password:
            user = userDao.getByEmail(email)
            if user and check_password_hash(user["password"], password):
                accessToken = create_access_token(identity=email)
                return {"access_token": accessToken}, 200
            else:
                return {"error": "Email or password is incorrect."}, 401
        else:
            return {"error": "Email and password fields are required."}, 400
        
    def upgradeSubscription(self, user):
        if user:
            user["subscription"] = True
            userDao.updateUser(user["_id"], user)
            
            return {"message": "Subscription upgraded."}, 200
        else:
            return {"error": "User not found."}, 404

    def updateUser(self, user, updatedUserData):
        if("password" in updatedUserData):
            updatedUserData["password"] = generate_password_hash(updatedUserData["password"])
        if user:
            userDao.updateUser(user["_id"], user, updatedUserData)
            
            return {"message": "User updated."}, 200
        else:
            return {"error": "User not found."}, 404
    