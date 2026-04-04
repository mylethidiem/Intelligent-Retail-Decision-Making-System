import io
from unittest.mock import patch

from fastapi.testclient import TestClient
from PIL import Image

from app.models.responses import DetectionResponse


def _minimal_png_bytes() -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", (8, 8), color=(128, 64, 32)).save(buf, format="PNG")
    return buf.getvalue()


def test_detect_image_unauthorized(client: TestClient) -> None:
    files = {"file": ("x.png", _minimal_png_bytes(), "image/png")}
    r = client.post("/api/v1/detect/image", files=files)
    assert r.status_code == 422  # missing X-Token


def test_detect_image_rejects_non_image(client: TestClient, auth_headers: dict) -> None:
    files = {"file": ("x.txt", b"not an image", "text/plain")}
    r = client.post(
        "/api/v1/detect/image",
        files=files,
        headers=auth_headers,
    )
    assert r.status_code == 400
    assert "image" in r.json()["detail"].lower()


@patch("app.api.routes.detection.DetectionService.detect_from_bytes")
def test_detect_image_success(
    mock_detect,
    client: TestClient,
    auth_headers: dict,
) -> None:
    mock_detect.return_value = DetectionResponse(
        success=True,
        message="ok",
        detections=[],
        processing_time=0.01,
        image_size={"width": 8, "height": 8},
        total_detections=0,
    )
    files = {"file": ("x.png", _minimal_png_bytes(), "image/png")}
    r = client.post(
        "/api/v1/detect/image",
        files=files,
        headers=auth_headers,
    )
    assert r.status_code == 200
    body = r.json()
    print(body)
    assert body["success"] is True
    assert len(body["detections"]) == 0
    mock_detect.assert_called_once()
