from flask_restx import Resource, Namespace
from flask import request
from app.main.utils.auth import token_required
from app.main.service.textOperationService import TextOperationService
from app.main.controller import addEmailForLogger

api = Namespace("api")
textOperationService = TextOperationService()

@api.route("/summarizeContent")
class summarizeContentResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        result = textOperationService.getSummarizeContent(json.get("content"), kwargs)
        return addEmailForLogger(result, email)
@api.route("/fixTypos")
class fixTyposResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        result = textOperationService.getFixTypos(json.get("content"), kwargs)
        return addEmailForLogger(result, email)

@api.route("/explainCode")
class explainCodeResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        email = kwargs.get("email")
        json = request.get_json()
        result = textOperationService.getExplainCode(json.get("content"), kwargs)
        return addEmailForLogger(result, email)