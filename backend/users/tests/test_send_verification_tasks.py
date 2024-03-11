from unittest.mock import patch

from django.test import TestCase, override_settings

from users.models import User
from users.tasks import send_user_verification_email, send_user_verification_sms


@override_settings(
    EMAIL_SERVICE_BACKEND="services.email.backends.dummy.EmailBackend",
    SMS_SERVICE_BACKEND="services.sms.backends.dummy.SMSBackend",
)
class SendVerificationTaskTestCase(TestCase):
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

    @patch("services.email.handler.EmailService.send")
    def test_send_user_verification_email_task(self, mock_email_service_send):
        send_user_verification_email.run(user_id=self.user.id)
        mock_email_service_send.assert_called_once()

    @patch("services.email.handler.EmailService.send")
    def test_send_user_verification_email_task_no_user(self, mock_email_service_send):
        send_user_verification_email.run(user_id=-100)
        mock_email_service_send.assert_not_called()

    @patch("services.sms.handler.SMSService.send")
    def test_send_user_verification_sms_task(self, mock_sms_service_send):
        send_user_verification_sms.run(user_id=self.user.id)
        mock_sms_service_send.assert_called_once()

    @patch("services.sms.handler.SMSService.send")
    def test_send_user_verification_sms_task_no_user(self, mock_sms_service_send):
        send_user_verification_sms.run(user_id=-100)
        mock_sms_service_send.assert_not_called()
