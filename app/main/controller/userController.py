from flask_restx import Resource, Namespace
from flask import request, current_app as app
from app.main.utils.auth import token_required
from app.main.utils.logger import addEmailForLogger
from app.main.utils.dependencyInjection import DependencyInjection

api = Namespace("api")

@api.route("/signUp")
class signUpResource(Resource):
    def post(self):
        json = request.get_json()
        email = json.get("email")
        password = json.get("password")
        result = DependencyInjection().getUserService(app).signUp(email, password)
        return addEmailForLogger(result, email)        

@api.route("/logIn")
class logInResource(Resource):
    def post(self):
        json = request.get_json()
        email = json.get("email")
        password = json.get("password")
        result = DependencyInjection().getUserService(app).logIn(email, password)
        return addEmailForLogger(result, email)
@api.route("/upgradeSubscription")
class upgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"subscription":True})
        email = kwargs.get("email")
        return addEmailForLogger(result, email)
@api.route("/downgradeSubscription")
class downgradeSubscriptionResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"subscription":False})
        email = kwargs.get("email")
        return addEmailForLogger(result, email)

@api.route("/updateEmail")
class updateEmailResource(Resource):
    @token_required
    def post(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        updatedEmail = json.get("email")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"email":updatedEmail})
        return addEmailForLogger(result, email) 
@api.route("/updatePassword")
class updatePasswordResource(Resource):
    @token_required
    def post(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        password = json.get("password")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"password":password})    
        return addEmailForLogger(result, email)
@api.route("/updateApiKey")
class updateApiKeyResource(Resource):
    @token_required
    def post(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        apiKey = json.get("api_key")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"api_key":apiKey})   
        return addEmailForLogger(result, email)
@api.route("/updateLanguagePreference")
class updateLanguagePreferenceResource(Resource):
    @token_required
    def post(self, *args, **kwargs):     
        email = kwargs.get("email")
        json = request.get_json()
        languagePreference = json.get("language_preference")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"language_preference":languagePreference})  
        return addEmailForLogger(result, email)