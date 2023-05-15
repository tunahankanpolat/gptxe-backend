from application import db

def getByRequest(operation, request):
    queries = db.queries
    return queries.find_one({"content": request, "operation": operation})

def addQuery(qery):
    queries = db.queries
    return queries.insert_one(qery.toString()).inserted_id

