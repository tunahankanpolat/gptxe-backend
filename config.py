import os

class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_DB_IP = os.getenv("MONGO_DB_IP", "172.17.0.2")
    REDIS_CACHE_IP = os.getenv("REDIS_CACHE_IP", "172.17.0.3")
    DATASOURCE_URI = "mongodb://"+MONGO_DB_IP+":27017"
    DATASOURCE_DATABASE="gptxe"
    REDIS_HOST = REDIS_CACHE_IP
    REDIS_PORT = 6379
    REDIS_DB = 0
    JWT_SECRET_KEY="super-secret"
    VERSION="1.0"
    TITLE="GPTXE API"
    DESCRIPTION="A simple GPTXE API"
    MAX_TOKEN=1024
class ProductionConfig(Config):
    LOG_LEVEL="INFO"
    LOG_FORMAT='%(asctime)s - %(levelname)s - [%(request_method)s %(endpoint)s] - [%(response_status)s] - [User: %(email)s] - %(message)s'
class DevelopmentConfig(Config):
    ENV="development"
    LOG_LEVEL="INFO"
    LOG_FORMAT='%(asctime)s - %(levelname)s - [%(request_method)s %(endpoint)s] - [%(response_status)s] - [User: %(email)s] - %(message)s'
    DEBUG = True
class TestingConfig(Config):
    TESTING = True
    LOG_LEVEL="INFO"
    LOG_FORMAT='%(asctime)s - %(levelname)s - [%(request_method)s %(endpoint)s] - [%(response_status)s] - [User: %(email)s] - %(message)s'