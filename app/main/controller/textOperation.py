from flask_restx import Resource
from flask import request, jsonify
from app.main.service.textOperationService import TextOperationService

textOperationService = TextOperationService()

class summarizeContent(Resource):
    def post(self):
        if request.method == "POST":
            content = request.json
            return jsonify({"result": textOperationService.getSummarizeContent(content)})

class fixTypos(Resource):
    def post(self):
        if request.method == "POST":
            content = request.json
            return jsonify({"result": textOperationService.getFixTypos(content)})

class explainCode(Resource):
    def post(self):
        if request.method == "POST":
            content = request.json
            return jsonify({"result": textOperationService.getExplainCode(content)})
   