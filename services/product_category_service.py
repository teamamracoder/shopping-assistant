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


    def toggle_category_status(self, pk, updated_by=None):
        """
        Toggle the is_active status of a product category.
        :param pk: Primary key of the category
        :param updated_by: User performing the toggle
        :return: Updated ProductCategoryModel instance
        :raises ValidationError: If not found or save fails
        """
        category = self.get_category_by_id(pk)
        if not category:
            raise ValidationError("Product category not found.")

        category.is_active = not category.is_active

        # ✅ Only assign if authenticated user is passed
        if updated_by and updated_by.is_authenticated:
            category.updated_by = updated_by

        try:
            category.save()
            return category
        except IntegrityError:
            raise ValidationError("Failed to toggle category status due to integrity issues.")





# from django.db import IntegrityError
# from django.forms import ValidationError
# from control_panel.models import ProductCategoryModel

# class ProductCategoryModelService:
#     def get_all_categories(self):
#         return ProductCategoryModel.objects.filter(is_active=True)

#     def get_category_by_id(self, pk):
#         try:
#             return ProductCategoryModel.objects.get(pk=pk, is_active=True)
#         except ProductCategoryModel.DoesNotExist:
#             return None

#     def create_category(self, validated_data):
#         try:
#             return ProductCategoryModel.objects.create(**validated_data)
#         except IntegrityError:
#             raise ValidationError("Category creation failed due to integrity issues.")

#     def update_category(self, category, validated_data):
#         try:
#             category.name = validated_data.get('name', category.name)
#             category.description = validated_data.get('description', category.description)
#             category.is_active = validated_data.get('is_active', category.is_active)
#             category.updated_by = validated_data.get('updated_by', category.updated_by)
#             category.save()
#             return category
#         except IntegrityError:
#             raise ValidationError("Category update failed due to integrity issues.")

#     def delete_category(self, category):
#         try:
#             category.is_active = False
#             category.save()
#         except Exception as e:
#             raise ValidationError(f"Error deleting category: {str(e)}")


#     def toggle_category_status(self, pk, updated_by=None):
#         """
#         Toggle the is_active status of a product category.
#         :param pk: Primary key of the category
#         :param updated_by: User performing the toggle
#         :return: Updated ProductCategoryModel instance
#         :raises ValidationError: If not found or save fails
#         """
#         category = self.get_category_by_id(pk)
#         if not category:
#             raise ValidationError("Product category not found.")

#         category.is_active = not category.is_active

#         # ✅ Only assign if authenticated user is passed
#         if updated_by and updated_by.is_authenticated:
#             category.updated_by = updated_by

#         try:
#             category.save()
#             return category
#         except IntegrityError:
#             raise ValidationError("Failed to toggle category status due to integrity issues.")
