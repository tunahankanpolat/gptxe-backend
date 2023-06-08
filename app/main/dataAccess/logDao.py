from . import databaseInstance

def addLog(log):
    logs = databaseInstance.logs
    return logs.insert_one(log.toString()).inserted_id