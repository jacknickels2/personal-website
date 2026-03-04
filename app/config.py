from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)
    
    # Application
    app_name: str = "Nicholas Cox - Portfolio"
    environment: str = "production"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Security
    secret_key: str
    allowed_hosts: str = "nicholascox.dev,www.nicholascox.dev,localhost"
    
    # Rate Limiting
    rate_limit_per_minute: int = 60
    
    @property
    def allowed_hosts_list(self) -> list[str]:
        """Get allowed hosts as a list."""
        return [host.strip() for host in self.allowed_hosts.split(",")]


settings = Settings()
