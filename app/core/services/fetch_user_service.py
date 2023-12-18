import requests
from app.core.models import User
from app.core.services import BaseService


class FetchUserService(BaseService):
    """
    A class for fetching user information from the Spotify API.

    Attributes:
        URL (str): The base URL for fetching user data from the Spotify API.
        session (requests.Session): HTTP session object with pre-configured 
            a1uthorization header.

    Args:
        access_token (str): Access token required for API authentication.
    """

    URL: str = 'https://api.spotify.com/v1/me'
    session: requests.Session

    def fetch_user(self) -> User:
        """
        Fetches user information from the Spotify API.

        Returns:
            User: An instance of the User model containing the fetched user 
                data.
        """
        response = self.session.get(self.URL)
        response.raise_for_status()
        
        response_json = response.json()
        user = User(
            id=response_json['id'],
            display_name=response_json['display_name'],
            country=response_json['country'],
            email=response_json['email'],
            href=response_json['href'],
            uri=response_json['uri']
        )
        return user

    def __call__(self) -> User:
        """
        Calls the instance to fetch and return user information.

        Returns:
            User: An instance of the User model containing the fetched user 
                data.
        """
        return self.fetch_user()
