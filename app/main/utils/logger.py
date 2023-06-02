from flask import request
from urllib.parse import urlparse
import json
import logging

logMessages = {
    500: (logging.ERROR, lambda response, jsonData: (jsonData.get("error"), {"response_status": response.status_code, "email":jsonData.get("email"), "request_method": request.method, "endpoint": urlparse(request.url).path})),
    403: (logging.WARNING, lambda response, jsonData: (jsonData.get("error"), {"response_status": response.status_code, "email":"", "request_method": request.method, "endpoint": urlparse(request.url).path})),
    range(400, 499): (logging.WARNING, lambda response, jsonData: (jsonData.get("error"), {"response_status": response.status_code, "email":jsonData.get("email"), "request_method": request.method, "endpoint": urlparse(request.url).path})),
    range(200, 299): (logging.INFO, lambda response, jsonData: (jsonData.get("message"), {"response_status": response.status_code, "email":jsonData.get("email"), "request_method": request.method, "endpoint": urlparse(request.url).path}))
}


def createLoggerMessages(app):
    @app.after_request
    def afterRequest(response):
        jsonData = response.get_json()
        statusCode = response.status_code

        logLevel, logData = None, None

        for key, value in logMessages.items():
            if isinstance(key, int) and key == statusCode:
                logLevel, logData = value
                break
            elif isinstance(key, range) and statusCode in key:
                logLevel, logData = value
                break

        if logData:
            logMessage, extraData = logData(response, jsonData)
            app.logger.log(logLevel, logMessage, extra=extraData)

        if("email" in jsonData):
            del jsonData["email"]
        if len(jsonData) > 1 and "message" in jsonData:
            del jsonData["message"]
        response.data =json.dumps(jsonData)
        return response