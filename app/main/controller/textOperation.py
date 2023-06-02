from flask_restx import Resource, Namespace
from flask import request
from app.main.utils.auth import token_required
from app.main.service.textOperationService import TextOperationService
from app.main.controller import addEmailForLogger

api = Namespace("api")

@api.route("/summarizeContent")
class summarizeContentResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        textOperationService = TextOperationService(kwargs)
        result = textOperationService.getSummarizeContent(json.get("content"))
        return addEmailForLogger(result, email)
@api.route("/fixTypos")
class fixTyposResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        textOperationService = TextOperationService(kwargs)
        result = textOperationService.getFixTypos(json.get("content"))
        return addEmailForLogger(result, email)

@api.route("/explainCode")
class explainCodeResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        textOperationService = TextOperationService(kwargs)
        result = textOperationService.getExplainCode(json.get("content"))
        return addEmailForLogger(result, email)