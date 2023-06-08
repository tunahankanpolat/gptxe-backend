from pymongo import MongoClient
from redis import Redis
from werkzeug.local import LocalProxy
from flask import current_app as app, g

def initDB(url="mongodb://localhost:27017", database="gptxe"):
    client = MongoClient(url)
    return client[database] 

def initCache(host = "localhost", port = 6379, db = 0):
    return Redis(host, port, db)

def getDB():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = initDB(app.config.get("DATASOURCE_URI"), app.config.get("DATASOURCE_DATABASE"))
    return db

def getCache():
    r = getattr(g, '_cache', None)
    if r is None:
        r = g._cache = initCache(app.config.get("REDIS_HOST"), app.config.get("REDIS_PORT"), app.config.get("REDIS_DB"))
    return r

db = LocalProxy(getDB)
r = LocalProxy(getCache)