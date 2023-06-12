class Prompt:
    def __init__(self, encoding):
        self.encoding = encoding

    def __summarizeContentPromtMessage(self, content):
        return [{"role": "system", "content": "You are a helpful assistant that summarizes the content in the language of the user's content in the shortest way without losing its meaning."},
                {"role": "user", "content": content}]

    def __explainCodePromtMessage(self, content, languagePreference):
        return [{"role": "system", "content": "You are a helpful assistant who briefly explains the code in " + str(languagePreference) + "."},
                {"role": "user", "content": content}]

    def __fixTyposPromtMessage(self, content):
        return [{"role": "system", "content": "You are a helpful assistant that corrects typos."},
                {"role": "user", "content": content}]

    def getSummarizeContentPromt(self, content):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__summarizeContentPromtMessage(content),
            "temperature": 0
        }

    def getExplainCodePromt(self, content, languagePreference):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__explainCodePromtMessage(content, languagePreference),
            "temperature": 0
        }

    def getFixTyposPromt(self, content):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__fixTyposPromtMessage(content),
            "temperature": 0
        }
    
    def getTokenCount(self, content):
        return len(self.encoding.encode(content))