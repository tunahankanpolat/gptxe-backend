import os
from flask_restx import Api
from .textOperation import api as textOperationApi
from .userController import api as userControllerApi


api = Api(version=os.getenv("VERSION"), title=os.getenv("TITLE"),
    description=os.getenv("DESCRIPTION"),
)

api.add_namespace(textOperationApi)
api.add_namespace(userControllerApi)