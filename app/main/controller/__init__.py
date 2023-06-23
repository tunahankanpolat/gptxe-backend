from flask_restx import Api
from .textOperation import api as textOperationApi
from .userController import api as userControllerApi

def initApi(app, version, title, description):
    api = Api(app, version=version, title=title, description=description)

    api.add_namespace(textOperationApi)
    api.add_namespace(userControllerApi)