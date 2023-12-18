import unittest
from unittest.mock import patch, MagicMock
import pytest
import base64
from requests import Response

from app.core.services import RequestAccessTokenService

CODE = 'dummy_code'
REDIRECT_URI = 'http://example.com/callback'
CLIENT_ID = 'dummy_client_id'
CLIENT_SECRET = 'dummy_client_secret'


@pytest.fixture
def service():
    return RequestAccessTokenService(
        CODE, REDIRECT_URI, CLIENT_ID, CLIENT_SECRET
    )


def test_make_payload(service):

    payload = service.make_payload()
    assert payload == {
        'code': CODE, 
        'redirect_uri': REDIRECT_URI, 
        'grant_type': 'authorization_code'
    }


def test_make_headers(service):

    headers = service.make_headers()
    expected_auth = base64.b64encode(
        f'{CLIENT_ID}:{CLIENT_SECRET}'.encode("utf-8")
    ).decode("utf-8")
    
    assert headers == {
        'content-type': 'application/x-www-form-urlencoded', 
        'Authorization': 'Basic ' + expected_auth
    }


@patch('requests.post')
def test_request_access_token(mock_post, service):

    expected_access_token = 'dummy_access_token'
    mock_response = MagicMock(spec=Response)
    mock_response.json.return_value = {'access_token': expected_access_token}
    mock_post.return_value = mock_response

    access_token = service.request_access_token()

    mock_post.assert_called_once_with(
        service.URL, 
        data=service.make_payload(), 
        headers=service.make_headers()
    )
    assert access_token == expected_access_token


@patch.object(RequestAccessTokenService, 'request_access_token')
def test_call(mock_request_access_token, service):

    expected_access_token = 'dummy_access_token'
    mock_request_access_token.return_value = expected_access_token

    access_token = service()

    mock_request_access_token.assert_called_once()
    assert access_token == expected_access_token
