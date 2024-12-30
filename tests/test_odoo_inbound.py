from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_odoo_inbound():
    payload = {
        "picking_id": 123,
        "origin": "SO1234"
    }
    response = client.post("/api/odoo/stock_picking", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["data"]["picking_id"] == 123
    assert data["data"]["origin"] == "SO1234"

