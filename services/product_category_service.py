from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ProductCategoryModel

class ProductCategoryModelService:
    def get_all_categories(self):
        return ProductCategoryModel.objects.all()

    def get_category_by_id(self, pk):
        try:
            return ProductCategoryModel.objects.get(pk=pk)
        except ProductCategoryModel.DoesNotExist:
            return None

    def create_category(self, validated_data):
        try:
            return ProductCategoryModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("Category creation failed due to integrity issues.")

    def update_category(self, category, validated_data):
        try:
            category.name = validated_data.get('name', category.name)
            category.description = validated_data.get('description', category.description)
            category.is_active = validated_data.get('is_active', category.is_active)
            category.updated_by = validated_data.get('updated_by', category.updated_by)
            category.save()
            return category
        except IntegrityError:
            raise ValidationError("Category update failed due to integrity issues.")

    def delete_category(self, category):
        try:
            category.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting category: {str(e)}")

