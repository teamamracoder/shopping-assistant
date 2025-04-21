from rest_framework import serializers
from control_panel.models import ServiceBookingModel, ServiceModel, UserModel  # ✅ make sure ServiceModel is imported

class ServiceBookingModelSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=ServiceModel.objects.all())
    service_provider = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), allow_null=True, required=False)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), allow_null=True, required=False)

    class Meta:
        model = ServiceBookingModel
        fields = '__all__'

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
