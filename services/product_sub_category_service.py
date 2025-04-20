from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ProductSubCategoryModel

class  ProductSubCategoryModelService:
    def get_all_sub_categories(self):
        return ProductSubCategoryModel.objects.all()

    def get_sub_category_by_id(self, pk):
        try:
            return ProductSubCategoryModel.objects.get(pk=pk)
        except ProductSubCategoryModel.DoesNotExist:
            return None

    def create_sub_category(self, validated_data):
        return ProductSubCategoryModel.objects.create(**validated_data)

    def update_sub_category(self, instance, validated_data):
        instance.category_id = validated_data.get('category', instance.category_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def delete_sub_category(self, instance):
        instance.delete()
