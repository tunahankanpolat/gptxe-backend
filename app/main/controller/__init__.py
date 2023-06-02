def initApi(app):
    from flask_restx import Api

    api = Api(app, version=app.config["VERSION"], title=app.config["TITLE"],
        description=app.config["DESCRIPTION"],
    )

    from .textOperation import api as textOperationApi
    from .userController import api as userControllerApi

    api.add_namespace(textOperationApi)
    api.add_namespace(userControllerApi)