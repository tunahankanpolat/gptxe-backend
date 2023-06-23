class Config(object):
    DEBUG = False
    TESTING = False
    DATASOURCE_URI = "mongodb://localhost:27017"
    DATASOURCE_DATABASE="gptxe"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    JWT_SECRET_KEY="super-secret"
    VERSION="1.0"
    TITLE="GPTXE API"
    DESCRIPTION="A simple GPTXE API"
    MAX_TOKEN=1024
class ProductionConfig(Config):
    pass
class DevelopmentConfig(Config):
    ENV="development"
    LOG_LEVEL="INFO"
    LOG_FORMAT='%(asctime)s - %(levelname)s - [%(request_method)s %(endpoint)s] - [%(response_status)s] - [User: %(email)s] - %(message)s'
    DEBUG = True
class TestingConfig(Config):
    TESTING = True