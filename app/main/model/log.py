class Log:
    def __init__(self, log):
        self.level = log.get("level")
        self.timeStamp = log.get("timestamp")
        self.requestMethod = log.get("request_method")
        self.endpoint = log.get("endpoint")
        self.responseStatus = log.get("response_status")
        self.email = log.get("email")
        self.msg = log.get("msg")
        
    def toString(self):
        return {
            "level": self.level,
            "time_stamp": self.timeStamp,
            "request_method": self.requestMethod,
            "endpoint": self.endpoint,
            "response_status": self.responseStatus,
            "email": self.email,
            "msg": self.msg
        }