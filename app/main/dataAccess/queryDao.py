import hashlib

class QueryDao:
    def __init__(self, redisInstance):
        self.redisInstance = redisInstance

    def addQuery(self, query):
        sha256 = hashlib.sha256()
        sha256.update(query.key().encode('utf-8'))

        hashedQuery = sha256.hexdigest()
        self.redisInstance.set(hashedQuery, query.value())

    def getByRequest(self, operation, request):
        sha256 = hashlib.sha256()
        key = "operation: " + operation + ", content: " + request
        sha256.update(key.encode('utf-8'))

        hashedQuery = sha256.hexdigest()
        value = self.redisInstance.get(hashedQuery)
        if(value):
            return value.decode('utf-8')
        else:
            return value