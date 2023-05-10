from flask_restx import Resource
from flask import request
from app.main.service.userService import UserService

userService = UserService()

class signUp(Resource):
    def post(self):
        if request.method == "POST":
            json = request.json
            email = json["email"]
            password = json["password"]
            return userService.signUp(email, password)

class logIn(Resource):
    def post(self):
            json = request.json
            email = json["email"]
            password = json["password"]
            return userService.logIn(email, password)
    
