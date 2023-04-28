from flask_restx import Resource
from flask import request, jsonify
from app.main.service.textOperationService import TextOperationService

textOperationService = TextOperationService()

class summarizeContent(Resource):
    def get(self,content):
        if request.method == "GET":
            return jsonify({"result": textOperationService.getSummarizeContent(content)})

class fixTypos(Resource):
    def get(self,content):
        if request.method == "GET":
            return jsonify({"result": textOperationService.getFixTypos(content)})

class explainCode(Resource):
    def get(self,content):
        if request.method == "GET":
            return jsonify({"result": textOperationService.getExplainCode(content)})
   