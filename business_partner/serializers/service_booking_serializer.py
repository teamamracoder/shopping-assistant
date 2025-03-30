from rest_framework import serializers
from control_panel.models.service_booking_model import ServiceBookingModel

class ServiceBookingModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service = serializers.PrimaryKeyRelatedField(queryset=ServiceBookingModel.objects.all())
    service_provider = serializers.PrimaryKeyRelatedField(queryset=ServiceBookingModel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=ServiceBookingModel.objects.all())
    booking_charge = serializers.FloatField()
    booking_time = serializers.DateTimeField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=ServiceBookingModel.objects.all(), allow_null=True)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=ServiceBookingModel.objects.all(), allow_null=True)

    def create(self, validated_data):
        return ServiceBookingModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service = validated_data.get('service', instance.service)
        instance.service_provider = validated_data.get('service_provider', instance.service_provider)
        instance.user = validated_data.get('user', instance.user)
        instance.booking_charge = validated_data.get('booking_charge', instance.booking_charge)
        instance.booking_time = validated_data.get('booking_time', instance.booking_time)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)
        instance.save()
        return instance