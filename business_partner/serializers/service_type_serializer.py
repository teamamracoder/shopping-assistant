from rest_framework import serializers
from control_panel.models import ServiceTypeModel

class ServiceTypeModelSerializer(serializers.Serializer):
    # Define the fields for serialization
    id = serializers.IntegerField(read_only=True)
    service_name = serializers.CharField(max_length=100, required=True)

    is_active = serializers.BooleanField(default=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    # Update method to handle updates to existing user
    def update(self, instance, validated_data):
        instance.service_name = validated_data.get('service_name', instance.service_name)
        instance.save()
        return instance
    
        # Create method to handle creating a new user
    def create(self, validated_data):
        return ServiceTypeModel.objects.create(**validated_data)


