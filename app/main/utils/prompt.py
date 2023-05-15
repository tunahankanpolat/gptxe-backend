class Prompt:
    def __init__(self, languagePreference):
        if(languagePreference):
            self.languagePreference = languagePreference
        else:
            self.languagePreference = "English"

    def setContent(self, content):
        self.content = content
        
    def __summarizeContentPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that summarizes the content in the language of the user's content in the shortest way without losing its meaning."},
                {"role": "user", "content": self.content}]

    def __explainCodePromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant who briefly explains the code in " + self.languagePreference + "."},
                {"role": "user", "content": self.content}]

    def __fixTyposPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that corrects typos."},
                {"role": "user", "content": self.content}]

    def getSummarizeContentPromt(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__summarizeContentPromtMessage(),
            "temperature": 0
        }

    def getExplainCodePromt(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__explainCodePromtMessage(),
            "temperature": 0
        }

    def getFixTyposPromt(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__fixTyposPromtMessage(),
            "temperature": 0
        }