from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    llm_model: str = "gpt-3.5-turbo"
    db_path: str = "local_data.duckdb"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
