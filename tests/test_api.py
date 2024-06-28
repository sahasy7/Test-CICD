from fastapi.testclient import TestClient
from Source import app

client = TestClient(app)

def test_read_main():
    resposne = client.get("/")
    assert resposne.status_code == 200
    assert resposne.json() == {"message":"Its working! trial once"}