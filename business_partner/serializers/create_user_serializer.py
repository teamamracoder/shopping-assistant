from .user_serializer import UserSerializer

class UserCreateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True},
        }
