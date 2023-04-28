from app.main.utils.prompt import Prompt
import openai
import os

class TextOperationService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.prompt = Prompt()
        self.chatCompletion = openai.ChatCompletion()

    def getSummarizeContent(self, content):
        self.prompt.setContent(content)
        response = self.chatCompletion.create(**self.prompt.getSummarizeContentPromt())
        return response.choices[0].message.content
    
    def getFixTypos(self, content):
        self.prompt.setContent(content)
        response = self.chatCompletion.create(**self.prompt.getFixTyposPromt())
        return response.choices[0].message.content
    
    def getExplainCode(self, content):
        self.prompt.setContent(content)
        response = self.chatCompletion.create(**self.prompt.getFixTyposPromt())
        return response.choices[0].message.content
