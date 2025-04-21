from rest_framework import serializers
from control_panel.models import ProductSubCategoryModel

class ProductSubCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.IntegerField()  # ID of the related ProductCategory
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField(default=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return ProductSubCategoryModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_id = validated_data.get('category', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
