# from django.db import models
# from control_panel.models import ProductSubCategoryModel


# # class ProductSubCategoryModelService:
# #     @staticmethod
# #     def get_all_subcategories():
# #         """
# #         Fetch all product subcategories from the database.
# #         :return: QuerySet of all ProductSubCategoryModel instances.
# #         """
# #         return ProductSubCategoryModel.objects.all()


# from control_panel.models import ProductSubCategoryModel

# class ProductSubCategoryModelService:
#     # @staticmethod
#     def get_all_subcategories():
#         """ Fetch all product subcategories from the database. """
#         return ProductSubCategoryModel.objects.all()

#     # @staticmethod
#     def create_subcategory(category, name, description):
#         """ Create and save a new product subcategory. """
#         return ProductSubCategoryModel.objects.create(
#             category=category,
#             name=name,
#             description=description
#         )
