from rest_framework import serializers
from control_panel.models import UserModel
from constants.enums import Gender, Role
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    gender_display = serializers.SerializerMethodField()  # Human-readable gender (read-only)
    roles = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )
    password = serializers.CharField(write_only=True, required=False)  # Password field, write-only
    is_active = serializers.BooleanField(default=True, required=False)
    roles_display = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = [
            'id',
            'first_name',
            'last_name', 
            'email', 
            'phone', 
            'gender',                   # raw gender (write-read)
            'gender_display',           # human-readable gender (read-only)
            'dob',
            'address',
            'location', 
            'city', 
            'district',
            'state',
            'pincode',
            'image_url', 
            'is_seller', 
            'is_service_provider',
            'designation',
            'bio', 
            'roles',                    # roles field for user input
            'roles_display',            # roles_display field for human-readable roles
            'is_active', 
            'created_at',
            'updated_at',
            'password'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'gender_display', 'roles_display']

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

    def get_gender_display(self, obj):
        # Return human-readable gender name
        return Gender(obj.gender).name if obj.gender else None  # Fixed typo here
    
    def get_roles_display(self, obj):
        # Converts role integers to human-readable role names
        return [Role(role).name for role in obj.roles] if obj.roles else []
