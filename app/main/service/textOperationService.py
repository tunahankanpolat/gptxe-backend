from app.main.utils.prompt import Prompt
from app.main.dataAccess import queryDao
from app.main.model.query import Query
import openai
import tiktoken
import os

class TextOperationService:
    def __init__(self, user):
        openai.api_key = user["api_key"]
        self.prompt = Prompt(user["language_preference"])
        self.chatCompletion = openai.ChatCompletion()
        self.maxToken = int(os.getenv("MAX_TOKEN"))
        try:
            self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        except KeyError:
            self.encoding = tiktoken.get_encoding("cl100k_base")

    def getSummarizeContent(self, content):
        query = queryDao.getByRequest("summarize_content",content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query["result"]},200
        elif(tokenCount <= self.maxToken):
            try:
                self.prompt.setContent(content)
                response = self.chatCompletion.create(**self.prompt.getSummarizeContentPromt())
                result = response.choices[0].message.content
                newQuery = Query("summarize_content", content, result)
                queryDao.addQuery(newQuery)
                return {"result": result}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body["error"]["code"])}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400
    
    def getFixTypos(self, content):
        query = queryDao.getByRequest("fix_typos", content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query["result"]},200
        elif(tokenCount <= self.maxToken):
            try:
                self.prompt.setContent(content)
                response = self.chatCompletion.create(**self.prompt.getFixTyposPromt())
                result = response.choices[0].message.content
                newQuery = Query("fix_typos", content, result)
                queryDao.addQuery(newQuery)
                return {"result": result}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body["error"]["code"])}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400
    
    
    def getExplainCode(self, content):
        query = queryDao.getByRequest("explain_code", content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query["result"]},200
        elif(tokenCount <= self.maxToken):
            try:
                self.prompt.setContent(content)
                response = self.chatCompletion.create(**self.prompt.getExplainCodePromt())
                result = response.choices[0].message.content
                newQuery = Query("explain_code", content, result)
                queryDao.addQuery(newQuery)
                return {"result": result}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body["error"]["code"])}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400