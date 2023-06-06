def test_testing_config(app):
    assert app.config['TESTING'] == True
    assert app.config['DEBUG'] == False
    assert app.config['LOG_LEVEL'] == "INFO"
    assert app.config['LOG_FORMAT'] == '%(asctime)s - %(levelname)s - [%(request_method)s %(endpoint)s] - [%(response_status)s] - [User: %(email)s] - %(message)s'
    assert app.config['DATASOURCE_URI'] == "mongodb://localhost:27017"
    assert app.config['DATASOURCE_DATABASE'] == "gptxe"
    assert app.config['REDIS_HOST'] == "localhost"
    assert app.config['REDIS_PORT'] == 6379
    assert app.config['REDIS_DB'] == 0
    assert app.config['JWT_SECRET_KEY'] == "super-secret"
    assert app.config['VERSION'] == "1.0"
    assert app.config['TITLE'] == "GPTXE API"
    assert app.config['DESCRIPTION'] == "A simple GPTXE API"
    assert app.config['MAX_TOKEN'] == 1024