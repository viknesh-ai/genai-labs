from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "GenAI Labs"
    APP_VERSION: str = "0.1.0"
    DESCRIPTION: str = "A FastAPI application for GenAI Labs"

    class Config:
        env_file = ".env"

#Createing a settings instance to be used across the application
settings = Settings()