class User:
    def __init__(self, email, password, apiKey = None, languagePreference = None):
        self.email = email
        self.password = password
        self.apiKey = apiKey
        self.subscription = False
        self.languagePreference = languagePreference

    def setApiKey(self, apiKey):
        self.apiKey = apiKey

    def getApiKey(self):
        return self.apiKey

    def setSubscription(self, subscription):
        self.subscription = subscription

    def getSubscription(self):
        return self.subscription

    def setLanguagePreference(self, languagePreference):
        self.languagePreference = languagePreference

    def getLanguagePreference(self):
        return self.languagePreference
    
    def toString(self):
        return {"email":self.email, "password": self.password, "apiKey":self.apiKey, "subscription":self.subscription, "languagePreference":self.languagePreference}