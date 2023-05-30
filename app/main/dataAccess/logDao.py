from app import db

def addLog(log):
    logs = db.logs
    return logs.insert_one(log.toString()).inserted_id