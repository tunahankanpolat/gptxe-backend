from flask import Flask
from flask_restx import Api
from app.main.controller.textOperation import Generate

app = Flask(__name__)

api = Api(app, version='1.0', title='GPTXE API',
    description='A simple GPTXE API',
)

api.add_resource(Generate,"/api/generate/<string:selectedText>&<string:operationChoice>")
  
if __name__ == "__main__":
    app.run(debug=True)