from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    ADMIN_TOKEN: str


settings = Settings()

tortoise_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": settings.POSTGRES_HOST,
                "port": settings.POSTGRES_PORT,
                "user": settings.POSTGRES_USER,
                "password": settings.POSTGRES_PASSWORD,
                "database": settings.POSTGRES_DB,
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "smit_test.api.cargo_types.models",
                "smit_test.api.tariffs.models",
                "aerich.models",
            ],
            "default_connection": "default",
        }
    },
}
