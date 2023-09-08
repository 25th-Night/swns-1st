from datetime import datetime

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.response import Response

from users.models import Profile


class SignUpViewTest(APITestCase):
    # Set up
    @classmethod
    def setUpTestData(cls):
        cls.test_model = get_user_model()
        cls.test_url = reverse("signup")
        cls.valid_user_data = {
            "email": "valid_user@test.com",
            "fullname": "Valid User",
            "phone": "01099999999",
            "password": "qwer1234!",
        }
        cls.invalid_user_data1 = {
            "email": "invalid_user1",
            "fullname": "Invalid User1",
            "phone": "01099999998",
            "password": "qwer1234!",
        }
        cls.invalid_user_data2 = {
            "email": "invalid_user2@test.com",
            "fullname": "",
            "phone": "01099999997",
            "password": "qwer1234!",
        }
        cls.invalid_user_data3 = {
            "email": "invalid_user3@test.com",
            "fullname": "Invalid User3",
            "phone": "01099999999",
            "password": "qwer1234!",
        }
        cls.invalid_user_data4 = {
            "email": "invalid_user4@test.com",
            "fullname": "Invalid User4",
            "phone": "01099999995",
            "password": "",
        }

    def test_signup_valid_data(self):
        res: Response = self.client.post(self.test_url, self.valid_user_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.test_model.objects.count(), 1)

    def test_signup_invalid_email_data(self):
        res: Response = self.client.post(self.test_url, self.invalid_user_data1)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_model.objects.count(), 0)

    def test_signup_invalid_fullname_data(self):
        res: Response = self.client.post(self.test_url, self.invalid_user_data2)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_model.objects.count(), 0)

    def test_signup_invalid_phone_data(self):
        valid_user = self.client.post(self.test_url, self.valid_user_data)
        res: Response = self.client.post(self.test_url, self.invalid_user_data3)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_model.objects.count(), 1)

    def test_signup_invalid_password_data(self):
        res: Response = self.client.post(self.test_url, self.invalid_user_data4)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.test_model.objects.count(), 0)


class LoginViewTest(APITestCase):
    # Set up
    @classmethod
    def setUpTestData(cls):
        cls.test_model = get_user_model()
        cls.test_url = reverse("login")
        cls.test_user = cls.test_model.objects.create_user(
            email="test@example.com",
            fullname="Test User",
            phone="01293845642",
            password="password",
        )
        cls.valid_user_data = {
            "email": "test@example.com",
            "password": "password",
        }
        cls.invalid_user_data = {
            "email": "test@example.com",
            "password": "invalid_password",
        }

    def test_login_valid_data(self):
        res: Response = self.client.post(self.test_url, self.valid_user_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("access", res.data.get("token"))
        self.assertIn("refresh", res.data.get("token"))

    def test_login_invalid_password(self):
        res: Response = self.client.post(self.test_url, self.invalid_user_data)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn("token", res.data)


class UserViewSetTest(APITestCase):
    # Set up
    @classmethod
    def setUpTestData(cls):
        cls.test_model = get_user_model()
        cls.admin_user = cls.test_model.objects.create(
            email="admin@example.com",
            fullname="Admin User",
            phone="01000000000",
            password="password",
            is_admin=True,
        )
        cls.user01 = cls.test_model.objects.create(
            email="user01@example.com",
            fullname="User01",
            phone="01111111111",
            password="password",
        )
        cls.user02 = cls.test_model.objects.create(
            email="user02@example.com",
            fullname="User02",
            phone="01222222222",
            password="password",
        )
        cls.user03 = cls.test_model.objects.create(
            email="user03@example.com",
            fullname="User03",
            phone="0133333333",
            password="password",
        )
        cls.user01_profile = Profile.objects.create(
            user=cls.user01, nickname="TestUser", birthday=datetime.now().date()
        )

    def test_list_data(self):
        test_url = reverse("user-list")
        client = APIClient()
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 4)

    def test_retrieve_with_no_login(self):
        test_url = reverse("user-detail", args=[self.user01.pk])
        client = APIClient()
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_with_admin_user_login(self):
        test_url = reverse("user-detail", args=[self.user01.pk])
        client = APIClient()
        client.force_authenticate(user=self.admin_user)
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_other_data(self):
        test_url = reverse("user-detail", args=[self.user01.pk])
        client = APIClient()
        client.force_authenticate(user=self.user02)
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_own_data(self):
        test_url = reverse("user-detail", args=[self.user01.pk])
        client = APIClient()
        client.force_authenticate(user=self.user01)
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_profile_with_no_login(self):
        test_url = reverse("user-profile", args=[self.user01.pk])
        client = APIClient()
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_with_login(self):
        test_url = reverse("user-profile", args=[self.user01.pk])
        client = APIClient()
        client.force_authenticate(user=self.user01)
        res: Response = client.get(test_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get("id"), self.user01_profile.id)


class ProfileViewSetTest(APITestCase):
    # Set up
    @classmethod
    def setUpTestData(cls):
        cls.test_model = Profile
        cls.user_model = get_user_model()
        cls.test_url = reverse("profile-list")
        cls.user01 = cls.user_model.objects.create(
            email="user01@example.com",
            fullname="User01",
            phone="01000000000",
            password="password",
        )
        cls.profile = cls.test_model.objects.create(
            user=cls.user01, nickname="TestUser01", birthday=datetime.now().date()
        )
        cls.user02 = cls.user_model.objects.create(
            email="user02@example.com",
            fullname="User02",
            phone="01000000001",
            password="password",
        )
        cls.user02_profile_data = {
            "user": cls.user02.id,
            "nickname": "TestUser02",
            "birthday": datetime.now().date(),
        }

    def test_create_data(self):
        client = APIClient()
        client.force_authenticate(user=self.user02)
        res: Response = client.post(self.test_url, self.user02_profile_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.test_model.objects.count(), 2)

    def test_list_data_with_no_login(self):
        client = APIClient()
        res: Response = client.get(self.test_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
