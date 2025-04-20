from django.urls import path
from ..views.product_sub_category_view import *

urlpatterns = [
    path('product-sub-categories/', ProductSubCategoryListCreateAPIView.as_view(), name='product_sub_category_list_create'),
    path('product-sub-categories/<int:pk>/', ProductSubCategoryDetailAPIView.as_view(), name='product_sub_category_detail'),
]
