from flask import Flask
from flask_restx import Api
from app.main.controller.textOperation import summarizeContent, explainCode, fixTypos

app = Flask(__name__)

api = Api(app, version='1.0', title='GPTXE API',
    description='A simple GPTXE API',
)

api.add_resource(summarizeContent,"/api/summarizeContent/<string:content>")
api.add_resource(explainCode,"/api/explainCode/<string:content>")
api.add_resource(fixTypos,"/api/fixTypos/<string:content>")

if __name__ == "__main__":
    app.run(debug=True)