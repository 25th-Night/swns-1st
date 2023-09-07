from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class SignUpViewTest(APITestCase):
    # Set up
    @classmethod
    def setUpTestData(cls):
        cls.user_model = get_user_model()
        cls.signup_url = reverse("signup")
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
        res: HttpResponse = self.client.post(self.signup_url, self.valid_user_data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.user_model.objects.count(), 1)

    def test_signup_invalid_email_data(self):
        res: HttpResponse = self.client.post(self.signup_url, self.invalid_user_data1)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.user_model.objects.count(), 0)

    def test_signup_invalid_fullname_data(self):
        res: HttpResponse = self.client.post(self.signup_url, self.invalid_user_data2)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.user_model.objects.count(), 0)

    def test_signup_invalid_phone_data(self):
        valid_user = self.client.post(self.signup_url, self.valid_user_data)
        res: HttpResponse = self.client.post(self.signup_url, self.invalid_user_data3)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.user_model.objects.count(), 1)

    def test_signup_invalid_password_data(self):
        res: HttpResponse = self.client.post(self.signup_url, self.invalid_user_data4)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.user_model.objects.count(), 0)
