class LogDao:
    def __init__(self, databaseInstance):
        self.databaseInstance = databaseInstance

    def addLog(self, log):
        logs = self.databaseInstance.logs
        return logs.insert_one(log.toString()).inserted_id