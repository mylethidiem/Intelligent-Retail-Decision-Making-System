from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "💡 Intelligent Retail Decision Making System"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 5050
    API_PREFIX: str = "/api/v1"

    # Model
    MODEL_CHECKPOINT: str = "yainage90/fashion-object-detection"
    DETECTION_THRESHOLD: float = 0.4
    HF_TOKEN: str = "xxx"

    # Security
    SECRET_KEY: str = "xxx"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 1 month
    API_TOKEN: str = "xxx"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()