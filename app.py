import os
from prompt import Prompt
import openai
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/api/generate", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data = request.json
        selectedText = data["selectedText"]
        operationChoice = data["operationChoice"]
        response = openai.ChatCompletion.create(**Prompt(operationChoice, selectedText).getPrompt())
        print("sa")
        print(response)
        print("as")
        return jsonify({"result": response.choices[0].message.content})