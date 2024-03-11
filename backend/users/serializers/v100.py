from rest_framework import serializers

from users.models import User


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
        user.send_verification_email()
        user.send_verification_sms()
        return user
