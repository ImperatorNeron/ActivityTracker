def test_get_uom(client):
    response = client.get("/api/v1/uom/")
    assert response.status_code == 200
    assert len(response.json()) == 8
