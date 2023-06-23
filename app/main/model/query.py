class Query:
    def __init__(self, operation, content, result):
        self.operation = operation
        self.content = content
        self.result = result

    def toString(self):
        return {"operation": self.operation, "content": self.content, "result": self.result}
    
    def key(self):
        return "operation: " + self.operation + ", content: " + self.content
    
    def value(self):
        return self.result
