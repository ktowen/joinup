from unittest.mock import patch

from django.test import TestCase, override_settings

from users.models import User
from users.serializers import v100, v110


@override_settings(
    EMAIL_SERVICE_BACKEND="services.email.backends.dummy.EmailBackend",
    SMS_SERVICE_BACKEND="services.sms.backends.dummy.SMSBackend",
)
class SignupTestCase(TestCase):
    @patch("services.email.handler.EmailService.send")
    @patch("services.sms.handler.SMSService.send")
    def test_v100_signup_serializer_save(self, mock_sms_service_send, mock_email_service_send):
        serializer = v100.UserSerializer(
            data={
                "email": "Karelle90@hotmail.com",
                "first_name": "Bradley",
                "last_name": "Sanford",
                "phone": "+34642424242",
                "hobbies": "Quia facere quo iure eum tempora tempore earum excepturi.",
            }
        )
        serializer.is_valid()
        serializer.save()

        self.assertEqual(User.objects.count(), 1)

        mock_sms_service_send.assert_called_once()
        mock_email_service_send.assert_called_once()

    @patch("users.tasks.send_user_verification_email.apply_async")
    @patch("users.tasks.send_user_verification_sms.apply_async")
    def test_v110_signup_serializer_save(self, mock_send_sms_task, mock_send_email_task):
        serializer = v110.UserSerializer(
            data={
                "email": "Karelle90@hotmail.com",
                "first_name": "Bradley",
                "last_name": "Sanford",
                "phone": "+34642424242",
                "hobbies": "Quia facere quo iure eum tempora tempore earum excepturi.",
            }
        )
        serializer.is_valid()
        serializer.save()

        self.assertEqual(User.objects.count(), 1)

        mock_send_sms_task.assert_called_once()
        mock_send_email_task.assert_called_once()
