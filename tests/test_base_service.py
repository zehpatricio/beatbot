import unittest
from unittest.mock import patch
from requests import Session

from app.core.services import BaseService


def test_init_creates_session_with_correct_headers():
    access_token = 'dummy_token'
    base_service = BaseService(access_token)
    
    assert isinstance(base_service.session, Session)
    assert (
        base_service.session.headers['Authorization'] == 
        f'Bearer {access_token}'
    )


def test_call_raises_not_implemented_error():
    access_token = 'dummy_token'
    base_service = BaseService(access_token)
    
    with unittest.TestCase().assertRaises(NotImplementedError):
        base_service()


@patch('requests.Session')
def test_session_is_updated_with_access_token(mock_session):
    access_token = 'dummy_token'
    BaseService(access_token)
    
    mock_session_instance = mock_session.return_value
    mock_session_instance.headers.update.assert_called_once_with(
        {'Authorization': f'Bearer {access_token}'}
    )
