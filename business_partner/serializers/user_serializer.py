from rest_framework import serializers
from control_panel.models import UserModel
from constants.enums import Gender, Role
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    roles = serializers.ListField(
        child=serializers.IntegerField(),
        default=[Role.END_USER.value],  # Default role if not provided
        required=False
    )
    password = serializers.CharField(write_only=True, required=False)  # Password field, write-only
    is_active = serializers.BooleanField(default=True, required=False)

    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'last_name', 
            'email', 
            'phone', 
            'gender',            
            'dob',
            'address',
            'location', 
            'city', 
            'district',
            'state',
            'country',
            'pincode',
            'image_url', 
            'is_seller', 
            'is_service_provider',
            'designation',
            'bio', 
            'roles',
            'is_active', 
            'created_at',
            'updated_at',
            'password'
        ]
        read_only_fields = [ 'id', 'created_at', 'updated_at' ]

    def create(self, validated_data):
        # `password` will be already hashed via the `validate_password` method
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)  # Hash password if provided
        return super().update(instance, validated_data)

    def validate(self, data):
        password = data.get('password')
        if password:
            data['password'] = make_password(password)

        data.setdefault('is_active', True)

        return data

