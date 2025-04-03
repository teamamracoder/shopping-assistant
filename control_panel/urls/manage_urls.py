from django.urls import path

from control_panel.views import IndexView,ManageDashboardView,ManageUserView,ManageProductSubCategoryListView,ManageProductSubCategoryCreateView,ManageProductListView,ManageProductCreateView,ManageProductCategoryListView,ManageProductCategoryCreateView
from control_panel.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),

    # product_sub_category
    path('product_sub_category/', ManageProductSubCategoryListView.as_view(), name='manage_product_sub_category_list'),
    path("product-sub-categories/create/", ManageProductSubCategoryCreateView.as_view(), name="manage_product_sub_category_create"),

    
    # Product URLs
    path('products/', ManageProductListView.as_view(), name='manage_product_list'),
    path("products/create/", ManageProductCreateView.as_view(), name="manage_product_create"),
    # path("products/edit/<int:pk>/", ManageProductUpdateView.as_view(), name="manage_product_edit"),
    # path("products/delete/<int:pk>/", ManageProductDeleteView.as_view(), name="manage_product_delete"),


    # Product Category URLs
    path('product_categories/', ManageProductCategoryListView.as_view(), name='manage_product_category_list'),
    path("product_categories/create/", ManageProductCategoryCreateView.as_view(), name="manage_product_category_create"),
    # path("product_categories/edit/<int:pk>/", ManageProductCategoryEditView.as_view(), name="manage_product_category_edit"),
    # path("product_categories/delete/<int:pk>/", ManageProductCategoryDeleteView.as_view(), name="manage_product_category_delete"),


# store urls by priya
    path('stores/', ManageStoreView.as_view(), name='manage_Store_list'),
    path('stores/create/', ManageCreateStore.as_view(), name='manage_create_store'),
    path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
    path('toggle-store-status/<int:store_id>/', ToggleStoreStatus.as_view(), name='toggle_store_status'),

#store category url
    path('stores/category/', ManageStoreCategoryView.as_view(), name='manage_Store_category_list'),
    path('store-category/create/', ManageCreateStoreCategoryView.as_view(), name='manage_create_store_category'),
    path("store-category/delete/<int:category_id>/", ManageDeleteStoreCategoryView.as_view(), name="delete_store_category"),
    path('toggle-store-category-status/<int:category_id>/', ToggleStoreCategoryStatus.as_view(), name='toggle_store_cetegory_status'),


]