from django.test import TestCase, override_settings
from django.urls import reverse

from users.models import User


@override_settings(
    EMAIL_SERVICE_BACKEND="services.email.backends.dummy.EmailBackend",
    SMS_SERVICE_BACKEND="services.sms.backends.dummy.SMSBackend",
)
class ApiQueryCountTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            **{
                "email": "Shawn52@hotmail.com",
                "first_name": "Sylvan",
                "last_name": "Hegmann",
                "phone": "+34642424242",
                "hobbies": "Quisquam eius omnis cum.",
            }
        )

    def test_user_v100_signup(self):
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse(
                    "user-v100-signup",
                ),
                data={
                    "email": "Karelle90@hotmail.com",
                    "first_name": "Bradley",
                    "last_name": "Sanford",
                    "phone": "+34642424242",
                    "hobbies": "Quia facere quo iure eum tempora tempore earum excepturi.",
                },
            )
        self.assertEqual(response.status_code, 201)

    def test_user_v100_profile(self):
        with self.assertNumQueries(1):
            response = self.client.get(reverse("user-v100-profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_user_v110_signup(self):
        with self.assertNumQueries(2):
            response = self.client.post(
                reverse(
                    "user-v110-signup",
                ),
                data={
                    "email": "Karelle90@hotmail.com",
                    "first_name": "Bradley",
                    "last_name": "Sanford",
                    "phone": "+34642424242",
                    "hobbies": "Quia facere quo iure eum tempora tempore earum excepturi.",
                },
            )
        self.assertEqual(response.status_code, 201)

    def test_user_v110_profile(self):
        with self.assertNumQueries(1):
            response = self.client.get(reverse("user-v110-profile", args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
