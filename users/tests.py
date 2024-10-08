from django.test import TestCase
import pytest
from django.urls import reverse   # permet de generer dynamiqument l'url du chemin
from rest_framework.test import APIClient
import jwt
from django.conf import settings
from django.utils import timezone
from .models import CustomUser

# Create your tests here.

@pytest.fixture
def api_client(db):
    return APIClient()

@pytest.fixture
def sample_user_data(db):
    return {'email' : 'paulnicolas519@gmail.com' , 'password' : 'Davide2020'}


def test_registration_pass(api_client, sample_user_data):
    sample_user_data.update({'confirm_password': sample_user_data['password']})
    registration_url = reverse('register')
    response = api_client.post(registration_url, data=sample_user_data)
    assert response.status_code == 201
    # assert not User.objects.get(email=sample_user_data['email']).verified





def test_confirm_registration_pass(api_client, create_sample_user, sample_user_data):
    confirm_registration_url = reverse("confirm_registration")
    sample_user_data.update(
        {"id": 9, "email": "tuttest1@ecoms.com", "password": "ecoms_1029"}
    )
    new_user = create_sample_user(**sample_user_data)
    token = new_user.get_confirmation_token
    response = api_client.get(f"{confirm_registration_url}?token={token}")

    assert response.status_code == 302
    assert CustomUser.objects.get(email="tuttest1@ecoms.com").verified




def test_confirm_registration_fail(api_client, create_sample_user, sample_user_data):
    confirm_registration_url = reverse("confirm_registration")
    sample_user_data.update(
        {"id": 9, "email": "tuttest1@ecoms.com", "password": "ecoms_1029"}
    )
    new_user = create_sample_user(**sample_user_data)
    response = api_client.get(f"{confirm_registration_url}")

    assert response.status_code == 302
    assert not CustomUser.objects.get(email="tuttest1@ecoms.com").verified

    # test for expired token
    token = new_user.get_confirmation_token
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    payload["exp"] = int(timezone.now().strftime("%s"))
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    response = api_client.get(f"{confirm_registration_url}?token={token}")
    assert response.status_code == 302
    assert not CustomUser.objects.get(email="tuttest1@ecoms.com").verified

