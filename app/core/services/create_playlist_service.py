from typing import Any

from app.core.services import BaseService
from app.core.models import User


class CreatePlaylistService(BaseService):
    user: User

    def __init__(self, access_token: str, user: User):
        super().__init__(access_token)
        self.user = user
    
    def make_payload(self, name: str) -> dict:
        return {
            'name': f'{name} by BeatBot',
            'public': False
        }

    def create_playlist(self, name: str) -> dict:
        user_id = self.user.id
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

        payload = self.make_payload(name)
        response = self.session.post(url, json=payload)
        response.raise_for_status()

        return response.json()

    def __call__(self, name) -> dict:
        return self.create_playlist(name)
