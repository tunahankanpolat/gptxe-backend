from app.main.model.user import User
from flask_jwt_extended import create_access_token, decode_token
from application import db
from werkzeug.security import check_password_hash, generate_password_hash

class UserService:
    def signUp(self, email, password):     
        if email and password:
            users = db.users
            if users.find_one({"email": email}):
                return {"error": "The e-mail address is already registered."}, 400
            
            user = User(email,generate_password_hash(password))
            userId = users.insert_one(user.toString()).inserted_id
            accessToken = create_access_token(identity=email)
            return {"access_token": accessToken}, 200
        else:
            return {"error": "Email and password fields are required."}, 400
    
    def logIn(self, email, password):
        if email and password:
            user = db.users.find_one({"email": email})
            if user and check_password_hash(user["password"], password):
                accessToken = create_access_token(identity=email)
                return {"access_token": accessToken}, 200
            else:
                return {"error": "Email or password is incorrect."}, 401
        else:
            return {"error": "Email and password fields are required."}, 400
        

    
