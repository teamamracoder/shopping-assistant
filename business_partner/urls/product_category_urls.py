from django.urls import path
from ..views.product_category_view import *

urlpatterns = [
    path('productcategories/', ProductCategoryListCreateAPIView.as_view(), name='product-category-list-create'),
    path('productcategories/<int:pk>/',ProductCategoryDetailAPIView.as_view(), name='product-category-detail'),
]
