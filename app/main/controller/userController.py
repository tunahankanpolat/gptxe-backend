from flask_restx import Resource, Namespace
from flask import request, current_app as app
from app.main.utils.auth import token_required
from app.main.utils.logger import addEmailForLogger
from app.main.utils.dependencyInjection import DependencyInjection

api = Namespace("api/user")

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
    
@api.route("/subscription")
class updateSubscriptionResource(Resource):
    @token_required
    def put(self, *args, **kwargs):
        json = request.get_json()
        subscription = json.get("subscription")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"subscription":subscription})
        email = kwargs.get("email")
        return addEmailForLogger(result, email)

@api.route("/email")
class updateEmailResource(Resource):
    @token_required
    def put(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        updatedEmail = json.get("email")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"email":updatedEmail})
        return addEmailForLogger(result, email) 
@api.route("/password")
class updatePasswordResource(Resource):
    @token_required
    def put(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        password = json.get("password")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"password":password})    
        return addEmailForLogger(result, email)
@api.route("/apiKey")
class updateApiKeyResource(Resource):
    @token_required
    def put(self, *args, **kwargs):       
        email = kwargs.get("email")
        json = request.get_json()
        apiKey = json.get("api_key")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"api_key":apiKey})   
        return addEmailForLogger(result, email)
@api.route("/languagePreference")
class updateLanguagePreferenceResource(Resource):
    @token_required
    def put(self, *args, **kwargs):     
        email = kwargs.get("email")
        json = request.get_json()
        languagePreference = json.get("language_preference")
        result = DependencyInjection().getUserService(app).updateUser(kwargs, {"language_preference":languagePreference})  
        return addEmailForLogger(result, email)