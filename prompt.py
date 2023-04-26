class Prompt:
    def __init__(self, choice, content):
        self.choice = choice
        self.content = content
        return 

    def __checkInformationPromtMessage(self):
        return [{"role": "system", "content": "You are a information checker that checks whether the information is correct. Check the correctness of the information using the translated content into English. Return true if the information is correct, Return false and correct content if the information is incorrect."},
                {"role": "user", "content": self.content}]

    def __summarizeContentPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant summarizing the content."},
                {"role": "user", "content": self.content}]

    def __explainCodePromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant explaining the code."},
                {"role": "user", "content": self.content}]

    def __fixTyposPromtMessage(self):
        return [{"role": "system", "content": "You are a helpful assistant that corrects typos."},
                {"role": "user", "content": self.content}]

    def __checkInformationPromtObject(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__checkInformationPromtMessage(),
            "temperature": 0
        }

    def __summarizeContentPromtObject(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__summarizeContentPromtMessage(),
            "temperature": 0
        }

    def __explainCodePromtObject(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__explainCodePromtMessage(),
            "temperature": 0
        }

    def __fixTyposPromtObject(self):
        return {
            "model": "gpt-3.5-turbo",
            "messages": self.__fixTyposPromtMessage(),
            "temperature": 0
        }

    def getPrompt(self):
        if self.choice == "summarizeContent":
            return self.__summarizeContentPromtObject()
        elif self.choice == "fixTypos":
            return self.__fixTyposPromtObject()
        elif self.choice == "explainCode":
            return self.__explainCodePromtObject()
        elif self.choice == "checkInformation":
            return self.__checkInformationPromtObject()
        else:
            return None
