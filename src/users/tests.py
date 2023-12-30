from core.fixtures_for_tests import create_user
import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_create_user():
    payload = {
        'name': 'Name',
        'surname': 'Surname',
        'age': 18
    }


    expected = {
        'message': 'User was successfully added to member list',
        'user': {
            'id': 1,
            'name': 'Name',
            'surname': 'Surname',
            'age': 18
        }
    }

    response = client.post('/api/v1/user/', payload)

    data = response.data

    assert data == expected


@pytest.mark.django_db
def test_create_user_with_wrong_age():
    payload = {
        'name': 'Name',
        'surname': 'Surname',
        'age': -18
    }

    expected = {
        "errors": {
            "non_field_errors": [
                "User cannot have negative age!"
            ]
        }
    }

    response = client.post('/api/v1/user/', payload)

    data = response.data

    assert data == expected


def test_get_all_users(create_user):
    expected = {
        'name': 'Bohdan',
        'surname': 'Hnydyn',
        'age': 18
    }

    response = client.get('/api/v1/user/')

    data = dict(response.data['users'][0])

    assert data['name'] == expected['name'] and data['surname'] == data['surname']


def test_get_user_by_id(create_user):
    expected = {
        'user_by_id': {
            'id': create_user.id,
            'name': 'Bohdan',
            'surname': 'Hnydyn',
            'age': 18
        }
    }

    response = client.get(f'/api/v1/user/{create_user.id}/')

    data = response.data

    assert data == expected


@pytest.mark.django_db
def test_user_does_not_exist():
    expected = {
        'error': 'User with id 99999 does not exist!'
    }

    response = client.get('/api/v1/user/99999/')

    data = response.data

    assert data == expected
