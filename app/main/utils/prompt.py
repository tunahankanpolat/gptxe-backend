class Prompt:
    def setContent(self, content):
        self.content = content

    def __checkInformationPromtMessage(self):
        return [{"role": "system", "content": "You are a information checker that checks whether the information is correct. Check the correctness of the information using the translated content into English. Return true if the information is correct, Return false and correct content if the information is incorrect."},
                {"role": "user", "content": self.content}]

    def __summarizeContentPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that summarizes the content in the language of the user's content in the shortest way without losing its meaning."},
                {"role": "user", "content": self.content}]

    def __explainCodePromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that explains the code in the shortest way."},
                {"role": "user", "content": self.content}]

    def __fixTyposPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that corrects typos."},
                {"role": "user", "content": self.content}]

    def __getCheckInformationPromt(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__checkInformationPromtMessage(),
            "temperature": 0
        }

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