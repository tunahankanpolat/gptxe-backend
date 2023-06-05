from . import db
from flask import current_app as app

def addLog(log):
    if not app.config.get("TESTING"):
        logs = db.logs
        return logs.insert_one(log.toString()).inserted_id