import requests


class BaseService:
    """
    Base class for all API services.

    Attributes:
        URL (str): Base URL of the API.
        session (requests.Session): HTTP session object with pre-configured 
            authorization header.

    Args:
        access_token (str): Access token required for API authentication.
    """
    URL: str
    session: requests.Session

    def __init__(self, access_token: str) -> None:
        """
        Initializes the BaseService class with an access token.

        Args:
            access_token (str): Access token required for API authentication.
        """
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {access_token}'})

    def __call__(self):
        """
        Raises NotImplementedError as this is an abstract base class.

        Raises:
            NotImplementedError: This method is not implemented and must 
                be overridden by subclasses.
        """
        raise NotImplementedError()
