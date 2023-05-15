from flask_restx import Resource
from flask import request
from app.main.utils.auth import token_required
from app.main.service.textOperationService import TextOperationService

class summarizeContentResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            json = request.json
            textOperationService = TextOperationService(kwargs)
            return textOperationService.getSummarizeContent(json["content"])

class fixTyposResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            json = request.json
            textOperationService = TextOperationService(kwargs)
            return textOperationService.getFixTypos(json["content"])

class explainCodeResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            json = request.json
            textOperationService = TextOperationService(kwargs)
            return textOperationService.getExplainCode(json["content"])
   