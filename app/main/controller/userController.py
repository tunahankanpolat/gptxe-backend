from flask_restx import Resource, Namespace
from flask import request
from app.main.service.userService import UserService
from app.main.utils.auth import token_required

api = Namespace("api")
userService = UserService()

@api.route("/signUp")
class signUpResource(Resource):
    def post(self):
        if request.method == "POST":
            email = ""
            try:
                json = request.json
                email = json["email"]
                password = json["password"]
                result = userService.signUp(email, password)
                return addEmail(result, email)
            except:
                return {"error": "Missing email and password values in body", "email":email}, 400
@api.route("/logIn")
class logInResource(Resource):
    def post(self):
        email = ""
        try:
            json = request.json
            email = json["email"]
            password = json["password"]
            result = userService.logIn(email, password)
            return addEmail(result, email)
        except:
            return {"error": "Missing email and password values in body", "email":email}, 400
@api.route("/upgradeSubscription")
class upgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        result = userService.updateUser(kwargs, {"subscription":True})
        email = kwargs["email"]
        return addEmail(result, email)
@api.route("/downgradeSubscription")
class downgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        result = userService.updateUser(kwargs, {"subscription":False})
        email = kwargs["email"]
        return addEmail(result, email)

@api.route("/updateEmail")
class updateEmailResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = ""
        try:
            email = kwargs["email"]
            json = request.json
            updatedEmail = json["email"]
            result = userService.updateUser(kwargs, {"email":updatedEmail})
            return addEmail(result, email)
        except:
            return {"error": "Missing email value in body", "email":email}, 400    
@api.route("/updatePassword")
class updatePasswordResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = ""
        try:
            email = kwargs["email"]
            json = request.json
            password = json["password"]
            result = userService.updateUser(kwargs, {"password":password})    
            return addEmail(result, email)
        except:
            return {"error": "Missing password value in body", "email":email}, 400
@api.route("/updateApiKey")
class updateApiKeyResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = ""
        try:
            email = kwargs["email"]
            json = request.json
            apiKey = json["api_key"]
            result = userService.updateUser(kwargs, {"api_key":apiKey})   
            return addEmail(result, email)
        except:
            return {"error": "Missing api_key value in body", "email":email}, 400
@api.route("/updateLanguagePreference")
class updateLanguagePreferenceResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = ""
        try:
            email = kwargs["email"]
            json = request.json
            languagePreference = json["language_preference"]
            result = userService.updateUser(kwargs, {"language_preference":languagePreference})  
            return addEmail(result, email)
        except:
            return {"error": "Missing language_preference value in body", "email":email}, 400
        
def addEmail(result, email):
    retDict = result[0].copy()
    retDict["email"] = email
    retTupple = (retDict, result[1])
    return retTupple