from app.tests import get_access_token

def test_logIn(client):
    response = client.post("/api/logIn", json={
        "email": "tuna@gmail.com",
        "password": "123",
    })
    assert response.status_code == 200
    assert "access_token" in response.json

def test_logIn_with_invalid_credentials(client):
    response = client.post("/api/logIn", json={
        "email": "tuna@gmail.com",
        "password": "wrong_password",
    })
    assert response.status_code == 401
    assert response.json.get("error") == "Email or password is incorrect."

def test_logIn_with_missing_fields(client):
    response = client.post("/api/logIn", json={
        "email": "tuna@gmail.com",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "Email and password fields are required."

def test_signUp(client):
    response = client.post("/api/signUp", json={
        "email": "tunaTest@gmail.com",
        "password": "123",
    })
    assert response.status_code == 200
    assert "access_token" in response.json

def test_signUp_with_existing_email(client):
    response = client.post("/api/signUp", json={
        "email": "tuna@gmail.com",
        "password": "123",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "The e-mail address is already registered."

def test_signUp_with_missing_fields(client):
    response = client.post("/api/signUp", json={
        "email": "tunaTest@gmail.com",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "Email and password fields are required."

def test_upgradeSubscription(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/upgradeSubscription", headers={"Authorization": access_token})
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."

def test_downgradeSubscription(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/downgradeSubscription", headers={"Authorization": access_token})
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."

def test_updateEmail(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/updateEmail", headers={"Authorization": access_token}, json={
        "email": "new_email@gmail.com",
    })
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."

def test_updatePassword(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/updatePassword", headers={"Authorization": access_token}, json={
        "password": "new_password",
    })
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."

def test_updateApiKey(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/updateApiKey", headers={"Authorization": access_token}, json={
        "api_key": "new_api_key",
    })
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."

def test_updateLanguagePreference(client):
    access_token = get_access_token()  # Önce giriş yapmalı ve access_token almalısınız.
    response = client.post("/api/updateLanguagePreference", headers={"Authorization": access_token}, json={
        "language_preference": "en",
    })
    assert response.status_code == 200
    assert response.json.get("message") == "User updated."