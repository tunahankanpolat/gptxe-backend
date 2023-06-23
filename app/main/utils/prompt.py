class Prompt:
    def __init__(self, encoding):
        self.encoding = encoding

    def __summarizeContentPromptMessage(self, content):
        return [{"role": "system", "content": "You are a helpful assistant that summarizes the content in the language of the user's content in the shortest way without losing its meaning."},
                {"role": "user", "content": content}]

    def __explainCodePromptMessage(self, content, languagePreference):
        return [{"role": "system", "content": "You are a helpful assistant who briefly explains the code in " + str(languagePreference) + "."},
                {"role": "user", "content": content}]

    def __fixTyposPromptMessage(self, content):
        return [{"role": "system", "content": "You are a helpful assistant that corrects typos."},
                {"role": "user", "content": content}]

    def getSummarizeContentPrompt(self, content):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__summarizeContentPromptMessage(content),
            "temperature": 0
        }

    def getExplainCodePrompt(self, content, languagePreference):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__explainCodePromptMessage(content, languagePreference),
            "temperature": 0
        }

    def getFixTyposPrompt(self, content):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__fixTyposPromptMessage(content),
            "temperature": 0
        }
    
    def getTokenCount(self, content):
        return len(self.encoding.encode(content))