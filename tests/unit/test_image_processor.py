import io

from PIL import Image

from app.utils.image_processor import image_processor


def test_validate_image_accepts_png() -> None:
    buf = io.BytesIO()
    Image.new("RGB", (4, 4), color="white").save(buf, format="PNG")
    assert image_processor.validate_image(buf.getvalue()) is True


def test_validate_image_rejects_garbage() -> None:
    assert image_processor.validate_image(b"not-an-image") is False
