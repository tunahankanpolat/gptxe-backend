import logging
from app.main.model.log import Log

class MongoDBHandler(logging.Handler):
    def __init__(self, logDao):
        logging.Handler.__init__(self)
        self.logDao = logDao

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
        self.logDao.addLog(log)