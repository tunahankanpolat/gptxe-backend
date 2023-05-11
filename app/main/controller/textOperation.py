from flask_restx import Resource
from flask import request, jsonify
from app.main.service.textOperationService import TextOperationService

textOperationService = TextOperationService()

class summarizeContentResource(Resource):
    def post(self):
        if request.method == "POST":
            json = request.json
            return jsonify({"result": textOperationService.getSummarizeContent(json["content"])})

class fixTyposResource(Resource):
    def post(self):
        if request.method == "POST":
            json = request.json
            return jsonify({"result": textOperationService.getFixTypos(json["content"])})

class explainCodeResource(Resource):
    def post(self):
        if request.method == "POST":
            json = request.json
            return jsonify({"result": textOperationService.getExplainCode(json["content"])})
   