from pymongo import MongoClient
from redis import Redis
from werkzeug.local import LocalProxy
from flask import current_app as app
from config import Config

def initDB(url="mongodb://localhost:27017", database="gptxe"):
    client = MongoClient(url)
    return client[database] 

def initCache(host = "localhost", port = 6379, db = 0):
    return Redis(host, port, databaseInstance)

def getDB():
    databaseInstance = getattr(app, '_database', None)
    if databaseInstance is None:
        databaseInstance = app._database = initDB(Config.DATASOURCE_URI, Config.DATASOURCE_DATABASE)
    return databaseInstance

def getCache():
    redisInstance = getattr(app, '_cache', None)
    if redisInstance is None:
        redisInstance = app._cache = initCache(Config.REDIS_HOST, Config.REDIS_PORT, Config.REDIS_DB)
    return redisInstance

databaseInstance = LocalProxy(getDB)
redisInstance = LocalProxy(getCache)