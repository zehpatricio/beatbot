import base64
import requests


class RequestAccessTokenService:
    """
    A class to request and retrieval of an access token from Spotify's API.

    Attributes:
        URL (str): The base URL for the access token request.
        code (str): The authorization code obtained during the OAuth2.0 flow.
        redirect_uri (str): The redirect URI used during the auth process.
        client_id (str): The client ID associated with the Spotify application.
        client_secret (str): The client secret associated with the Spotify 
            application.
    """

    URL: str = 'https://accounts.spotify.com/api/token'

    def __init__(self,
                 code: str,
                 redirect_uri: str,
                 client_id: str,
                 client_secret: str,
    ) -> None:
        """
        Initializes the RequestAccessTokenService instance.

        Args:
            code (str): The authorization code obtained during the auth flow.
            redirect_uri (str): The redirect URI used during the auth process.
            client_id (str): The client ID associated with the Spotify app.
            client_secret (str): The client secret associated with the Spotify 
                application.
        """
        self.code = code
        self.redirect_uri = redirect_uri
        self.client_id = client_id
        self.client_secret = client_secret

    def make_payload(self) -> dict:
        """
        Creates the payload for the access token request.

        Returns:
            dict: The payload containing the authorization code, redirect URI, 
                and grant type.
        """
        return {
            'code': self.code,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

    def make_headers(self) -> dict:
        """
        Creates the headers for the access token request.

        Returns:
            dict: The headers containing the content type and authorization 
                information.
        """
        auth = f'{self.client_id}:{self.client_secret}'.encode("utf-8")
        encoded_auth = base64.b64encode(auth).decode("utf-8")

        return {
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + encoded_auth
        }

    def request_access_token(self) -> str:
        """
        Sends a request to Spotify's API to obtain an access token.

        Returns:
            str: The obtained access token.
        """
        data = self.make_payload()
        headers = self.make_headers()

        response = requests.post(self.URL, data=data, headers=headers)
        response.raise_for_status()
        return response.json()['access_token']

    def __call__(self) -> str:
        """
        Calls the instance to request and return the access token.

        Returns:
            str: The obtained access token.
        """
        return self.request_access_token()
