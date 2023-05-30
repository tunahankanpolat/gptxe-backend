from flask import Flask, request
from flask_jwt_extended import JWTManager
from app.main.controller import api
from app.main.utils.logger import MongoAndConsoleLogger
import json
import os
from urllib.parse import urlparse

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  # Change this!
api.init_app(app)

customLogger = MongoAndConsoleLogger(__name__)

@app.after_request
def afterRequest(response):
    jsonData = response.get_json()
    if(response.status_code >= 500):
        customLogger.logger.error(jsonData["error"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
    elif(response.status_code == 403):
        customLogger.logger.warning(jsonData["error"], extra={"response_status": response.status_code, "email":"", "request_method": request.method, "endpoint": urlparse(request.url).path})
    elif(response.status_code >= 400 and response.status_code < 500):
        customLogger.logger.warning(jsonData["error"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
    elif(response.status_code >= 200 and response.status_code < 300):
        customLogger.logger.info(jsonData["message"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
    
    if("email" in jsonData):
        del jsonData["email"]
    if len(jsonData) > 1 and "message" in jsonData:
        del jsonData["message"]
    response.data =json.dumps(jsonData)
    return response

if __name__ == "__main__":
    jwt = JWTManager(app)
    app.run(debug=True)
