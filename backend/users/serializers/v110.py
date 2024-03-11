from rest_framework import serializers

from users.models import User
from users.tasks import send_user_verification_email, send_user_verification_sms


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "is_email_verified",
            "phone",
            "is_phone_verified",
            "first_name",
            "last_name",
            "hobbies",
        ]
        read_only_fields = ["is_email_verified", "is_phone_verified"]

    def create(self, validated_data):
        user = super().create(validated_data)
        send_user_verification_sms.delay(user_id=user.id)
        send_user_verification_email.delay(user_id=user.id)
        return user
