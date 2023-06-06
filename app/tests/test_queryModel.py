from app.main.model.query import Query

def test_constructor_with_attributes():
    query = Query("search", "apple", ["apple", "apples", "pineapple"])
    assert query.operation == "search"
    assert query.content == "apple"
    assert query.result == ["apple", "apples", "pineapple"]

def test_toString():
    query = Query("search", "apple", ["apple", "apples", "pineapple"])
    query_dict = query.toString()
    assert query_dict["operation"] == "search"
    assert query_dict["content"] == "apple"
    assert query_dict["result"] == ["apple", "apples", "pineapple"]

def test_key():
    query = Query("search", "apple", ["apple", "apples", "pineapple"])
    key = query.key()
    assert key == "operation: search, content: apple"

def test_value():
    query = Query("search", "apple", ["apple", "apples", "pineapple"])
    value = query.value()
    assert value == ["apple", "apples", "pineapple"]
