import os
from flask import Flask, request, current_app, g
from flask_jwt_extended import JWTManager
from app.main.controller import initApi
from app.main.utils.mongoDBHandler import MongoDBHandler
from flask.logging import default_handler
from urllib.parse import urlparse
import logging
import json
from app.main.dataAccess import initCache, initDB

def createApp(name = "gptxe"):
    app = Flask(name)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    JWTManager(app)

    initApi(app)
    initLogger(app)
    return app


def initLogger(app):
    app.logger.removeHandler(default_handler)

    mongoHandler = MongoDBHandler()
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter(app.config["LOG_FORMAT"])
    mongoHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)
    mongoHandler.setLevel(app.config["LOG_LEVEL"])
    streamHandler.setLevel(app.config["LOG_LEVEL"])
    
    app.logger.addHandler(mongoHandler)
    app.logger.addHandler(streamHandler)

    @app.after_request
    def afterRequest(response):
        jsonData = response.get_json()
        if(response.status_code >= 500):
            app.logger.error(jsonData["error"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
        elif(response.status_code == 403):
            app.logger.warning(jsonData["error"], extra={"response_status": response.status_code, "email":"", "request_method": request.method, "endpoint": urlparse(request.url).path})
        elif(response.status_code >= 400 and response.status_code < 500):
            app.logger.warning(jsonData["error"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
        elif(response.status_code >= 200 and response.status_code < 300):
            app.logger.info(jsonData["message"], extra={"response_status": response.status_code, "email":jsonData["email"], "request_method": request.method, "endpoint": urlparse(request.url).path})
        
        if("email" in jsonData):
            del jsonData["email"]
        if len(jsonData) > 1 and "message" in jsonData:
            del jsonData["message"]
        response.data =json.dumps(jsonData)
        return response