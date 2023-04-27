from flask_restx import Resource
from flask import request, jsonify
from app.main.model.prompt import Prompt
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class Generate(Resource):
    def get(self,selectedText,operationChoice):
        if request.method == "GET":
            response = openai.ChatCompletion.create(**Prompt(operationChoice, selectedText).getPrompt())
            return jsonify({"result": response.choices[0].message.content})
   