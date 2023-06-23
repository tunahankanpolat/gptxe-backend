import logging
from app.main.model.log import Log
from app.main.dataAccess.logDao import addLog

class MongoDBHandler(logging.Handler):
    def emit(self, record):
        logEntry = {
            'level': record.levelname,
            'timestamp': record.created,
            'request_method': record.request_method,
            'endpoint': record.endpoint,
            'response_status': record.response_status,
            'email': record.email,
            'msg': record.msg
        }
        log = Log(logEntry)
        addLog(log)