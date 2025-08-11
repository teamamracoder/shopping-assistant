from rest_framework import serializers
from services import services
from django.contrib.auth import get_user_model

User = get_user_model()

class SendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False, max_length=100, help_text="First name (required if the email is not registered)")
    last_name = serializers.CharField(required=False, max_length=100, help_text="Last name (required if the email is not registered)")

    def validate(self, data):
        email = data.get('email')

        # Check if email exists
        if not services.user_service.is_exist(email=email):
            required_fields = ['first_name', 'last_name']
            missing_fields = [field for field in required_fields if not data.get(field)]
            
            if missing_fields:
                raise serializers.ValidationError(
                    f"For new users, these fields are required: {', '.join(missing_fields)}"
                )

        return data
    


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'roles']


class VerifyOTPResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = UserAuthSerializer()


class SendOTPResponseSerializer(serializers.Serializer):
    existing_user = serializers.BooleanField()
