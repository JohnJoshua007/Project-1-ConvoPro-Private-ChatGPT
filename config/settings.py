# from dotenv import load_dotenv
# from pydantic_settings import BaseSettings
#
# load_dotenv()
#
#
# class Settings(BaseSettings):
#
#     MONGO_DB_URL: str
#     MONGO_DB_NAME: str
#     OLLAMA_URL: str
#     OLLAMA_MODELS: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"



from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    # MongoDB settings
    MONGO_DB_URL: str
    MONGO_DB_NAME: str

    # Gemini settings
    GOOGLE_API_KEY: str
    GEMINI_MODELS: str = "gemini-3.5-flash,gemini-3.6-flash, gemini-3.7-flash"   # comma-separated list

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",          # ignore any extra env vars
    )

settings = Settings()