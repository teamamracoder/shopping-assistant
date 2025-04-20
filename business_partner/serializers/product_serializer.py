from rest_framework import serializers 
from control_panel.models import ProductsModel, ProductCategoryModel, ProductSubCategoryModel

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=True)
    product_code = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    discount_per = serializers.DecimalField(max_digits=5, decimal_places=2, required=False)
    quantity = serializers.IntegerField(required=False)
    maf_date = serializers.DateTimeField(required=False, allow_null=True)
    exp_date = serializers.DateTimeField(required=False, allow_null=True)
    image_urls = serializers.ListField(
        child=serializers.URLField(max_length=500),
        required=False,
        allow_null=True
    )
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategoryModel.objects.all(), required=True)
    sub_category = serializers.PrimaryKeyRelatedField(queryset=ProductSubCategoryModel.objects.all(), required=False, allow_null=True)
    others_category = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)
    is_active = serializers.BooleanField(default=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    updated_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        return ProductsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.product_code = validated_data.get('product_code', instance.product_code)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.discount_per = validated_data.get('discount_per', instance.discount_per)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.maf_date = validated_data.get('maf_date', instance.maf_date)
        instance.exp_date = validated_data.get('exp_date', instance.exp_date)
        instance.image_urls = validated_data.get('image_urls', instance.image_urls)
        instance.category = validated_data.get('category', instance.category)
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.others_category = validated_data.get('others_category', instance.others_category)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
