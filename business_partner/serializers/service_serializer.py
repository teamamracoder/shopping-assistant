from rest_framework import serializers # type: ignore
from control_panel.models.service_model import ServiceModel
from control_panel.models.service_type_model import ServiceTypeModel
from control_panel.models.user_model import UserModel
class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    service_type = serializers.PrimaryKeyRelatedField(queryset=ServiceTypeModel.objects.all())
    service_provider = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    services_charge = serializers.FloatField()
    description = serializers.CharField(allow_blank=True, required=False)

    def create(self, validated_data):
        return ServiceModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.service_type = validated_data.get('service_type', instance.service_type)
        instance.service_provider = validated_data.get('service_provider', instance.service_provider)
        instance.services_charge = validated_data.get('services_charge', instance.services_charge)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


