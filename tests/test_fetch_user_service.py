from unittest.mock import patch, MagicMock
import pytest

from app.core.models import User
from app.core.services.fetch_user_service import FetchUserService


ACCESS_TOKEN = 'dummy_token'


@pytest.fixture
def service():
    return FetchUserService(ACCESS_TOKEN)

def test_fetch_user(service):

    expected_user_data = {
        'id': '123',
        'display_name': 'John Doe',
        'email': 'john@example.com',
    }

    mock_response = MagicMock()
    mock_response.json.return_value = expected_user_data

    with patch.object(service.session, 'get', return_value=mock_response):
        user = service.fetch_user()

    assert user.id == expected_user_data['id']
    assert user.display_name == expected_user_data['display_name']
    assert user.email == expected_user_data['email']


@patch('requests.Session')
def test_call(mock_session, service):

    expected_user_data = {
        'id': '123',
        'display_name': 'John Doe',
        'email': 'john@example.com',
    }

    mock_response = MagicMock()
    mock_response.json.return_value = expected_user_data

    mock_session.get.return_value = mock_response

    user = service()

    mock_session.assert_called_once()
    mock_session.get.assert_called_once_with(service.URL)
    assert user.id == expected_user_data['id']
    assert user.display_name == expected_user_data['display_name']
    assert user.email == expected_user_data['email']
