from flask_restx import Resource
from flask import request
from app.main.service.userService import UserService
from app.main.utils.auth import token_required

userService = UserService()

class signUpResource(Resource):
    def post(self):
        if request.method == "POST":
            json = request.json
            email = json["email"]
            password = json["password"]
            return userService.signUp(email, password)

class logInResource(Resource):
    def post(self):
        json = request.json
        email = json["email"]
        password = json["password"]
        return userService.logIn(email, password)
    
class upgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        return userService.upgradeSubscription(kwargs)

class downgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        return userService.upgradeSubscription(kwargs)
    
class updateEmailResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        json = request.json
        email = json["email"]
        return userService.updateUser(kwargs, {"email":email})    

class updatePasswordResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        json = request.json
        password = json["password"]
        return userService.updateUser(kwargs, {"password":password})    

class updateApiKeyResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        json = request.json
        apiKey = json["api_key"]
        return userService.updateUser(kwargs, {"api_key":apiKey})    

class updateLanguagePreferenceResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        json = request.json
        languagePreference = json["language_preference"]
        return userService.updateUser(kwargs, {"language_preference":languagePreference})    