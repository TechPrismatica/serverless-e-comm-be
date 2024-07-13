from pydantic_settings import BaseSettings


class _ServiceConfig(BaseSettings):
    SERVICE_NAME: str = "user-management-service"
    LOG_LEVEL: str = "INFO"
    ENABLE_CONSOLE_LOG: bool = True
    ENABLE_FILE_LOG: bool = True
    LOG_FILE_PATH: str = "logs"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ROOT_API_PATH: str = "/auth"


class _RootUserConfig(BaseSettings):
    ROOT_USER_EMAIL: str = "serverless.e-comm.root@gmail.com"
    ROOT_USER_PASSWORD: str = "root"
    ROOT_USERNAME: str = "root"
    ROOT_FIRST_NAME: str = "root"
    ROOT_LAST_NAME: str = "root"


ServiceConfig = _ServiceConfig()
RootUserConfig = _RootUserConfig()
