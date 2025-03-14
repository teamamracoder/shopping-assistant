from rest_framework import serializers # type: ignore
from control_panel.models import UserModel
from constants.enums import Role, Gender
from django.contrib.postgres.fields import ArrayField

class UserSerializer(serializers.Serializer):
    # Define the fields for serialization
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)
    gender = serializers.ChoiceField(choices=[(gender.value, gender.name) for gender in Gender], required=False)
    dob = serializers.DateField(required=False, allow_null=True)
    address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    location = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    city = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    district = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    state = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    pincode = serializers.IntegerField(required=False, allow_null=True)
    image_url = serializers.URLField(required=False, allow_null=True, allow_blank=True)
    is_seller = serializers.BooleanField(required=False)
    is_service_provider = serializers.BooleanField(required=False)
    designation = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    bio = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    roles = serializers.ListField(
        child=serializers.IntegerField(),
        required=False
    )
    is_active = serializers.BooleanField(default=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # Update method to handle updates to existing user
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.address = validated_data.get('address', instance.address)
        instance.location = validated_data.get('location', instance.location)
        instance.city = validated_data.get('city', instance.city)
        instance.district = validated_data.get('district', instance.district)
        instance.state = validated_data.get('state', instance.state)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.is_seller = validated_data.get('is_seller', instance.is_seller)
        instance.is_service_provider = validated_data.get('is_service_provider', instance.is_service_provider)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.roles = validated_data.get('roles', instance.roles)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    # Create method to handle creating a new user
    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

