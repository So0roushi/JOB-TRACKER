def test_post(client):
    response = client.post("/applications", json={"company" : "meta", "role" : "dev" })
    data = response.json()
    assert response.status_code == 201
    assert data["company"] == "meta"
    assert data["role"] == "dev"
    assert data["status"] == "Saved"
    assert data["link"] == None
    assert data["notes"] == None
    assert "id" in data

def test_wrong_input_returns_422(client):
    response = client.post("/applications", json={ "role" : "dev" })
    data = response.json()
    assert response.status_code == 422
    assert "detail" in response.json()
    
