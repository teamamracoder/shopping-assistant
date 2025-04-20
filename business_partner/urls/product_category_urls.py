from django.urls import path
from ..views.product_category_view import *

urlpatterns = [
    path('product-categories/', ProductCategoryListCreateAPIView.as_view(), name='product-category-list-create'),
    path('product-categories/<int:pk>/',ProductCategoryDetailAPIView.as_view(), name='product-category-detail'),
]
