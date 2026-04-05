import os
from datetime import timedelta

# Skip heavy HF model load before any app import pulls model_service.
os.environ.setdefault("TESTING", "1")

import pytest
from fastapi.testclient import TestClient

from app.core.security import create_access_token
from app.main import app


@pytest.fixture
def auth_headers() -> dict[str, str]:
    token = create_access_token(
        data={"sub": "test_user"},
        expires_delta=timedelta(minutes=30),
    )
    return {"X-Token": token}


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
