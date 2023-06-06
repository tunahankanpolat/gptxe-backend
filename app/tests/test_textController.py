from app.tests import get_access_token

def test_summarizeContent(client):
    access_token = get_access_token()
    response = client.post("/api/summarizeContent", headers={"Authorization": access_token}, json={
        "content": "This is a long piece of text that needs to be summarized.",
    })
    assert response.status_code == 200
    assert response.json.get("result") is not None

def test_summarizeContent_empty_content(client):
    access_token = get_access_token()
    response = client.post("/api/summarizeContent", headers={"Authorization": access_token}, json={
        "content": "",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "Content is empty."

def test_fixTypos(client):
    access_token = get_access_token()
    response = client.post("/api/fixTypos", headers={"Authorization": access_token}, json={
        "content": "Ths is a test contnt with som typoos.",
    })
    assert response.status_code == 200
    assert response.json.get("result") is not None

def test_fixTypos_empty_content(client):
    access_token = get_access_token()
    response = client.post("/api/fixTypos", headers={"Authorization": access_token}, json={
        "content": "",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "Content is empty."

def test_explainCode(client):
    access_token = get_access_token()
    response = client.post("/api/explainCode", headers={"Authorization": access_token}, json={
        "content": "for i in range(5):\n    print(i)",
    })
    assert response.status_code == 200
    assert response.json.get("result") is not None

def test_explainCode_empty_content(client):
    access_token = get_access_token()
    response = client.post("/api/explainCode", headers={"Authorization": access_token}, json={
        "content": "",
    })
    assert response.status_code == 400
    assert response.json.get("error") == "Content is empty."