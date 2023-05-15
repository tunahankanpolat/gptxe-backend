class User:
    def __init__(self, email, password, apiKey = None, languagePreference = None):
        self.email = email
        self.password = password
        self.apiKey = apiKey
        self.subscription = False
        self.languagePreference = languagePreference
    
    def toString(self):
        return {"email":self.email, "password": self.password, "api_key":self.apiKey, "subscription":self.subscription, "language_preference":self.languagePreference}