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

    initApi(app, version=app.config["VERSION"], title=app.config["TITLE"], description=app.config["DESCRIPTION"])
    initLogger(app, app.config["LOG_FORMAT"])
    return app


def initLogger(app, logLevel = "INFO"):
    app.logger.removeHandler(default_handler)
    
    formatter = logging.Formatter(logLevel)

    app.logger.addHandler(initMongoDBHandler(formatter, app))
    app.logger.addHandler(initConsoleHandler(formatter, app))

    from app.main.utils.logger import createLoggerMessages
    createLoggerMessages(app)

def initMongoDBHandler(formatter, app):
    mongoHandler = MongoDBHandler()
    mongoHandler.setFormatter(formatter)
    mongoHandler.setLevel(app.config["LOG_LEVEL"])
    return mongoHandler


def initConsoleHandler(formatter, app):
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(app.config["LOG_LEVEL"])
    return streamHandler