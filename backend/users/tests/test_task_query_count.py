from django.test import TestCase, override_settings

from users.models import User
from users.tasks import send_user_verification_email, send_user_verification_sms


@override_settings(
    EMAIL_SERVICE_BACKEND="services.email.backends.dummy.EmailBackend",
    SMS_SERVICE_BACKEND="services.sms.backends.dummy.SMSBackend",
)
class TaskQueryCountTestCase(TestCase):
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

    def test_send_user_verification_email(self):
        with self.assertNumQueries(1):
            send_user_verification_email.run(user_id=self.user.id)

    def test_send_user_verification_sms(self):
        with self.assertNumQueries(1):
            send_user_verification_sms.run(user_id=self.user.id)
