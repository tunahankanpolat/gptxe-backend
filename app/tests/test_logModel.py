from app.main.model.log import Log

def test_constructor():
    log_dict = {
        "level": "INFO",
        "timestamp": "2022-01-01 12:00:00",
        "request_method": "GET",
        "endpoint": "/api",
        "response_status": 200,
        "email": "user@example.com",
        "msg": "Log message"
    }
    log = Log(log_dict)
    assert log.level == "INFO"
    assert log.timeStamp == "2022-01-01 12:00:00"
    assert log.requestMethod == "GET"
    assert log.endpoint == "/api"
    assert log.responseStatus == 200
    assert log.email == "user@example.com"
    assert log.msg == "Log message"

def test_toString():
    log_dict = {
        "level": "INFO",
        "timestamp": "2022-01-01 12:00:00",
        "request_method": "GET",
        "endpoint": "/api",
        "response_status": 200,
        "email": "user@example.com",
        "msg": "Log message"
    }
    log = Log(log_dict)
    logString = log.toString()
    assert logString.get("level") == "INFO"
    assert logString.get("time_stamp") == "2022-01-01 12:00:00"
    assert logString.get("request_method") == "GET"
    assert logString.get("endpoint") == "/api"
    assert logString.get("response_status") == 200
    assert logString.get("email") == "user@example.com"
    assert logString.get("msg") == "Log message"