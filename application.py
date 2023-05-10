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
    from app.main.controller.textOperation import summarizeContent, explainCode, fixTypos
    from app.main.controller.userController import signUp, logIn, upgradeSubscription
    jwt = JWTManager(app)
    api.add_resource(summarizeContent, "/api/summarizeContent")
    api.add_resource(explainCode, "/api/explainCode")
    api.add_resource(fixTypos, "/api/fixTypos")
    api.add_resource(signUp, "/api/signUp")
    api.add_resource(logIn, "/api/logIn")

    app.run(debug=True)
