from app.main.utils.mongoDBHandler import MongoDBHandler
import os
import logging

class MongoAndConsoleLogger:
    def __init__(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(os.getenv("LOG_LEVEL"))

        mongoHandler = MongoDBHandler()
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter(os.getenv("LOG_FORMAT"))
        mongoHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)
        mongoHandler.setLevel(os.getenv("LOG_LEVEL"))
        streamHandler.setLevel(os.getenv("LOG_LEVEL"))

        logger.addHandler(mongoHandler)
        logger.addHandler(streamHandler)
        self.logger = logger