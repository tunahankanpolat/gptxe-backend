import os
from flask import Flask
from flask_jwt_extended import JWTManager
from app.main.controller import initApi
from app.main.utils.mongoDBHandler import MongoDBHandler
from flask.logging import default_handler
import logging

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
    from app.main.utils.logger import createLoggerMessages
    createLoggerMessages(app)