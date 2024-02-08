from fastapi.testclient import TestClient
from fastapi import status

from ..main import app


client = TestClient(app=app)


def test_get_landing_page__output_is_correct():

    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Ricardo's solution for MyTomorrows' assignment."
