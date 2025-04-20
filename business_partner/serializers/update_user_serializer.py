from .user_serializer import UserSerializer

class UserUpdateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'password': {'required': False},
            'gender': {'required': False},
        }
