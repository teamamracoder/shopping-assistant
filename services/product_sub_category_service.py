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

    # def update_sub_category(self, instance, validated_data):
    #     instance.category_id = validated_data.get('category', instance.category_id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.is_active = validated_data.get('is_active', instance.is_active)
    #     instance.save()
    #     return instance
    def update_sub_category(self, instance, validated_data):
        try:
            # Preserve original created_by
            original_created_by = instance.created_by

            instance.category_id = validated_data.get('category', instance.category_id)
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.updated_by = validated_data.get('updated_by', instance.updated_by)

            # Restore created_by
            instance.created_by = original_created_by

            instance.save(update_fields=['category', 'name', 'description', 'is_active', 'updated_by', 'created_by'])
            return instance
        except IntegrityError:
            raise ValidationError("Subcategory update failed due to integrity issues.")



    def delete_sub_category(self, instance):
        instance.delete()

    def toggle_sub_category_status(self, pk):
        subcategory = self.get_sub_category_by_id(pk)
        if not subcategory:
            raise ValidationError("Subcategory not found.")

        subcategory.is_active = not subcategory.is_active
        try:
            subcategory.save()
            return subcategory
        except IntegrityError:
            raise ValidationError("Failed to toggle status due to database error.")



# from django.db import IntegrityError
# from django.forms import ValidationError
# from control_panel.models import ProductSubCategoryModel

# class  ProductSubCategoryModelService:
#     def get_all_sub_categories(self):
#         return ProductSubCategoryModel.objects.filter(is_active=True)

#     def get_sub_category_by_id(self, pk):
#         try:
#             return ProductSubCategoryModel.objects.get(pk=pk, is_active=True)
#         except ProductSubCategoryModel.DoesNotExist:
#             return None

#     def create_sub_category(self, validated_data):
#         return ProductSubCategoryModel.objects.create(**validated_data)

#     def update_sub_category(self, instance, validated_data):
#         instance.category_id = validated_data.get('category', instance.category_id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance

#     def delete_sub_category(self, instance):
#         # instance.delete()
#         instance.is_active = False
#         instance.save()

#     def toggle_sub_category_status(self, pk):
#         subcategory = self.get_sub_category_by_id(pk)
#         if not subcategory:
#             raise ValidationError("Subcategory not found.")

#         subcategory.is_active = not subcategory.is_active
#         try:
#             subcategory.save()
#             return subcategory
#         except IntegrityError:
#             raise ValidationError("Failed to toggle status due to database error.")