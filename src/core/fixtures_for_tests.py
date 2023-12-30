from rest_framework.test import APIClient
import pytest

from users.models import Users

client = APIClient()


@pytest.fixture
def create_user(db) -> Users:
    user_dict = {
        'name': 'Bohdan',
        'surname': 'Hnydyn',
        'age': 18
    }

    user = Users.objects.create(**user_dict)

    return user
