from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory

from account import views

from .api import UpdateUserApi


class AccountViewTest(TestCase):
    """do setup before test"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", password="12test12", email="test@example.com"
        )

    def tearDown(self):
        self.user.delete()

    """do correct login"""

    def test_correct(self):
        response = self.client.post(
            "/api/token/", {"username": "test", "password": "12test12"}
        )
        self.assertTrue(response.data["access"])

    """do incorrect registration"""

    def test_empty_password_registration(self):
        response = self.client.post(
            "/account/api/register", {"username": "test", "password": ""}
        )
        self.assertTrue(
            response.data["password"], "This field may not be blank."
        )

    """do incorrect registration"""

    def test_empty_username_registration(self):
        response = self.client.post(
            "/account/api/register", {"username": "", "password": ""}
        )
        self.assertTrue(
            response.data["username"], "This field may not be blank."
        )

    """do incorrect registration"""

    def test_repeated_username_registration(self):
        response = self.client.post(
            "/account/api/register",
            {"username": "test", "password": "12test12"},
        )
        self.assertTrue(
            response.data["username"],
            "A user with that username already exists.",
        )

    """do correct update password"""

    def test_update_password(self):
        view = UpdateUserApi.as_view()
        factory = APIRequestFactory()
        id = User.objects.get(username="test")
        request = factory.put(
            "/account/api/update/",
            {"username": "test", "password": "test12", "repassword": "test12"},
        )
        response = view(request, pk=str(id.pk))
        assert response.status_code == 200

    """do correct logout"""

    def test_logout(self):
        view = views.logout_view
        client = APIClient()
        id = User.objects.get(username="test")
        resp = self.client.post(
            "/api/token/",
            {"username": "test", "password": "12test12"},
        )
        access_token = resp.data["access"]
        refresh_token = resp.data["refresh"]
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = client.post(
            "/account/api/logout",
            {"refresh": refresh_token},
        )
        assert response.status_code == 200

    """do incorrect login"""

    def test_wrong_username(self):
        response = self.client.post(
            "/api/token/", {"username": "wrong", "password": "12test12"}
        )
        self.assertTrue(
            response.data["detail"],
            "No active account found with the given credentials",
        )

    """do incorrect login"""

    def test_wrong_pssword(self):
        response = self.client.post(
            "/api/token/", {"username": "test", "password": "wrong"}
        )
        self.assertTrue(
            response.data["detail"],
            "No active account found with the given credentials",
        )
