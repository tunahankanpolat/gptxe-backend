import hashlib
from . import redisInstance


def addQuery(query):
    sha256 = hashlib.sha256()
    sha256.update(query.key().encode('utf-8'))

    hashedQuery = sha256.hexdigest()
    redisInstance.set(hashedQuery, query.value())

def getByRequest(operation, request):
    sha256 = hashlib.sha256()
    key = "operation: " + operation + ", content: " + request
    sha256.update(key.encode('utf-8'))

    hashedQuery = sha256.hexdigest()
    value = redisInstance.get(hashedQuery)
    if(value):
        return value.decode('utf-8')
    else:
        return value