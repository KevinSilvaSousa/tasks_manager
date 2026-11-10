import pytest
from fastapi.testclient import TestClient
from src.api.routes import search_tasks
from src.main import app

test_client = TestClient(
    app,
    base_url="http://testserver",
    raise_server_exceptions=True,
    root_path="",
    backend="asyncio",
    backend_options=None,
    cookies=None,
    headers=None,
    follow_redirects=True,
    client=("testclient", 50000),
)