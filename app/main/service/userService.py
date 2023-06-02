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
            accessToken = create_access_token(identity=email, expires_delta=False)
            return {"access_token": accessToken, "message": "Successfully registered"}, 200
        else:
            return {"error": "Email and password fields are required."}, 400
    
    def logIn(self, email, password):
        if email and password:
            user = userDao.getByEmail(email)
            if user and check_password_hash(user.get("password"), password):
                accessToken = create_access_token(identity=email, expires_delta=False)
                return {"access_token": accessToken, "message": "Successfully logged in"}, 200
            else:
                return {"error": "Email or password is incorrect."}, 401
        else:
            return {"error": "Email and password fields are required."}, 400

    def updateUser(self, user, updatedUserData):
        if("password" in updatedUserData):
            updatedUserData["password"] = generate_password_hash(updatedUserData.get("password"))
        if user:
            userDao.updateUser(user.get("_id"), user, updatedUserData)
            if("email" in updatedUserData):
                accessToken = create_access_token(identity=updatedUserData.get("email"), expires_delta=False)
                return {"access_token": accessToken,"message": "User updated."}, 200
            else:
                return {"message": "User updated."}, 200
        else:
            return {"error": "User not found."}, 404