from rest_framework import serializers
from .user_serializer import UserSerializer
from control_panel.models import UserModel

class UserUpdateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            'email': {
                'required': False,
                'validators': []  # Disable DRF's default unique validator
            },
            'password': {'required': False}
        }

    def validate_email(self, value):
        """
        Prevents duplicate email errors even when self.instance is missing.
        Allows the same email if it's the user's current one.
        """
        instance = getattr(self, 'instance', None)
        
        # If the email is the same as the current user's, allow it
        if instance and instance.email == value:

            return value

        # Check for duplicates (exclude the current user if found)
        if UserModel.objects.filter(email=value).exclude(
            pk=instance.pk if instance else None
        ).exists():
            raise serializers.ValidationError("This email is already taken.")
        return value


