def initApi(app, version, title, description):
    from flask_restx import Api

    api = Api(app, version=version, title=title, description=description)

    from .textOperation import api as textOperationApi
    from .userController import api as userControllerApi

    api.add_namespace(textOperationApi)
    api.add_namespace(userControllerApi)