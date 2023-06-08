def initApi(app):
    from flask_restx import Api

    api = Api(app, version=app.config.get("VERSION"), title=app.config.get("TITLE"),
        description=app.config.get("DESCRIPTION"),
    )

    from .textOperation import api as textOperationApi
    from .userController import api as userControllerApi

    api.add_namespace(textOperationApi)
    api.add_namespace(userControllerApi)


def addEmailForLogger(result, email):
    retDict = result[0].copy()
    retDict["email"] = email
    retTupple = (retDict, result[1])
    return retTupple