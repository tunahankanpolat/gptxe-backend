from app.main.utils.prompt import Prompt
from app.main.dataAccess.queryDao import addQuery, getByRequest
from app.main.model.query import Query
from config import Config
import openai
import tiktoken

class TextOperationService:
    def __init__(self):
        self.prompt = Prompt()
        self.chatCompletion = openai.ChatCompletion()
        self.maxToken = int(Config.MAX_TOKEN)
        try:
            self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        except KeyError:
            self.encoding = tiktoken.get_encoding("cl100k_base")

    def getSummarizeContent(self, content, user):
        openai.api_key = user.get("api_key")
        query = getByRequest("summarize_content",content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query, "message": "Request exists in cache"},200
        elif(tokenCount <= self.maxToken):
            try:
                response = self.chatCompletion.create(**self.prompt.getSummarizeContentPromt(content))
                result = response.choices[0].message.content
                newQuery = Query("summarize_content", content, result)
                addQuery(newQuery)
                return {"result": result, "message": "Successfully sent a request to the OpenAI Api"}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body.get("error").get("code"))}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400
    
    def getFixTypos(self, content, user):
        openai.api_key = user.get("api_key")
        query = getByRequest("fix_typos", content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query, "message": "Request exists in cache"},200
        elif(tokenCount <= self.maxToken):
            try:
                response = self.chatCompletion.create(**self.prompt.getFixTyposPromt(content))
                result = response.choices[0].message.content
                newQuery = Query("fix_typos", content, result)
                addQuery(newQuery)
                return {"result": result, "message": "Successfully sent a request to the OpenAI Api"}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body.get("error").get("code"))}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400
    
    
    def getExplainCode(self, content, user):
        openai.api_key = user.get("api_key")
        query = getByRequest("explain_code", content)
        tokenCount = len(self.encoding.encode(content))
        if not content:
            return {"error": "Content is empty."}, 400
        elif(query):
            return {"result": query, "message": "Request exists in cache"},200
        elif(tokenCount <= self.maxToken):
            try:
                response = self.chatCompletion.create(**self.prompt.getExplainCodePromt(content, user.get("language_preference")))
                result = response.choices[0].message.content
                newQuery = Query("explain_code", content, result)
                addQuery(newQuery)
                return {"result": result, "message": "Successfully sent a request to the OpenAI Api"}, 200
            except openai.error.OpenAIError as error:
                return {"error": str(error.json_body.get("error").get("code"))}, error.http_status
        else:
            return {"error": "Your request "+ str(tokenCount) +" tokens exceeds the max token count of " + str(self.maxToken) +  "."}, 400