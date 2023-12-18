from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'BeatBot'
    client_id: str
    client_secret: str
    redirect_uri: str
    scopes: List[str] = [
        "user-read-private", 
        "user-read-email", 
        "playlist-modify-public", 
        "playlist-modify-private"
    ]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
