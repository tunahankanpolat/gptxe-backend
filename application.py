from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from pymongo import MongoClient

app = Flask(__name__)

api = Api(app, version='1.0', title='GPTXE API',
    description='A simple GPTXE API',
)
client = MongoClient("mongodb://localhost:27017")
db = client["gptxe"] 

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!

if __name__ == "__main__":
    from app.main.controller.textOperation import *
    from app.main.controller.userController import *
    jwt = JWTManager(app)
    api.add_resource(summarizeContentResource, "/api/summarizeContent")
    api.add_resource(explainCodeResource, "/api/explainCode")
    api.add_resource(fixTyposResource, "/api/fixTypos")
    api.add_resource(signUpResource, "/api/signUp")
    api.add_resource(logInResource, "/api/logIn")
    api.add_resource(upgradeSubscriptionResource, "/api/upgradeSubscription")
    api.add_resource(downgradeSubscriptionResource, "/api/downgradeSubscription")

    
    api.add_resource(updateEmailResource, "/api/updateEmail")
    api.add_resource(updatePasswordResource, "/api/updatePassword")
    api.add_resource(updateApiKeyResource, "/api/updateApiKey")
    api.add_resource(updateLanguagePreferenceResource, "/api/updateLanguagePreference")

    app.run(debug=True)
