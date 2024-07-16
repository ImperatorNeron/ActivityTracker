from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class DatabaseSettings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    echo: bool = False

    @property
    def url(self):
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


class Settings(BaseSettings):
    api_version_prefix: str = "/api/v1"
    database: DatabaseSettings = DatabaseSettings()


settings = Settings()
