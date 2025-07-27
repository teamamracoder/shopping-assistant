from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import StoreCategoryModel

class StoreCategoryService:
    # def get_all_store_categories(self):
    #     return StoreCategoryModel.objects.filter(is_active=True)
    def get_all_store_categories(self):
        return StoreCategoryModel.objects.all()

    def get_store_category_by_id(self, pk):
        try:
            return StoreCategoryModel.objects.get(pk=pk)
        except StoreCategoryModel.DoesNotExist:
            return None

    # def create_store_category(self, validated_data, user = None):
    #     return StoreCategoryModel.objects.create(**validated_data, created_by=user)
    def create_store_category(self, validated_data):
        try:
            return StoreCategoryModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("Store Category creation failed due to integrity issues.")


    # def get_store_category(self, pk):
    #     try:
    #         return StoreCategoryModel.objects.get(pk=pk, is_active=True)
    #     except StoreCategoryModel.DoesNotExist:
    #         return None

    # def update_store_category(self, store_category, validated_data, user = None):
    #     for attr, value in validated_data.items():
    #         setattr(store_category, attr, value)
    #     store_category.updated_by = user 
    #     store_category.save()
    #     return store_category

    
    def update_store_category(self, category, validated_data):
        try:
            category.name = validated_data.get('name', category.name)           
            category.is_active = validated_data.get('is_active', category.is_active)
            category.updated_by = validated_data.get('updated_by', category.updated_by)
            category.save()
            return category
        except IntegrityError:
            raise ValidationError("Store Category update failed due to integrity issues.")


    # def delete_store_category(self, store_category):
    #     store_category.is_active = False
    #     store_category.save()
    #     return True

    def delete_store_category(self, category):
        try:
            category.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting Store category: {str(e)}")

