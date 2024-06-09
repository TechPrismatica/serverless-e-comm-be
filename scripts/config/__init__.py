from pydantic_settings import BaseSettings


class _ServiceConfig(BaseSettings):
    SERVICE_NAME: str = "user-management-service"
    LOG_LEVEL: str = "INFO"
    ENABLE_CONSOLE_LOG: bool = True
    ENABLE_FILE_LOG: bool = True
    LOG_FILE_PATH: str = "logs"


class _Databases(BaseSettings):
    MONGO_URI: str


ServiceConfig = _ServiceConfig()
Databases = _Databases()
