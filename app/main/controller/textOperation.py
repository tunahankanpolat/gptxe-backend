from flask_restx import Resource, Namespace
from flask import request
from app.main.utils.auth import token_required
from app.main.service.textOperationService import TextOperationService

api = Namespace("api")

@api.route("/summarizeContent")
class summarizeContentResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            try:
                json = request.json
                textOperationService = TextOperationService(kwargs)
                result = textOperationService.getSummarizeContent(json["content"])
                retDict = result[0].copy()
                retDict["email"] = kwargs["email"]
                retTupple = (retDict, result[1])
                return retTupple
            except:
                return {"error": "Missing content value in body"}, 400
@api.route("/fixTypos")
class fixTyposResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            try:
                json = request.json
                textOperationService = TextOperationService(kwargs)
                result = textOperationService.getFixTypos(json["content"])
                retDict = result[0].copy()
                retDict["email"] = kwargs["email"]
                retTupple = (retDict, result[1])
                return retTupple
            except:
                return {"error": "Missing content value in body"}, 400

@api.route("/explainCode")
class explainCodeResource(Resource):
    @token_required
    def post(self, *args, **kwargs):
        if request.method == "POST":
            try:
                json = request.get_json()
                textOperationService = TextOperationService(kwargs)
                result = textOperationService.getExplainCode(json["content"])
                retDict = result[0].copy()
                retDict["email"] = kwargs["email"]
                retTupple = (retDict, result[1])
                return retTupple
            except:
                return {"error": "Missing content value in body"}, 400