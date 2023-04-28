from flask import Flask
from flask_restx import Api
from app.main.controller.textOperation import summarizeContent, explainCode, fixTypos

app = Flask(__name__)

api = Api(app, version='1.0', title='GPTXE API',
    description='A simple GPTXE API',
)

api.add_resource(summarizeContent,"/api/summarizeContent")
api.add_resource(explainCode,"/api/explainCode")
api.add_resource(fixTypos,"/api/fixTypos")

if __name__ == "__main__":
    app.run(debug=True)