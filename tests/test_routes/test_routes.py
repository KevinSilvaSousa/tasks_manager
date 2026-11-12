import pytest
from fastapi.testclient import TestClient
from src.api.routes import search_tasks
from src.main import app


@pytest.fixture
def client():
  """Fixture que fornece um cliente de teste isolado para a API."""
  # Se quiser usar o context manager para garantir limpeza de conexões:
  with TestClient(app, base_url="http://testserver",
      raise_server_exceptions=True,
      root_path="",
      backend="asyncio",
      backend_options=None,
      cookies=None,
      headers=None,
      follow_redirects=True,
      client=("testclient", 50000)) as c:
    yield c



def test_path_routes(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Task Manager API"}
