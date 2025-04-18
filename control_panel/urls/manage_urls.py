from django.urls import path

from control_panel.views import IndexView,ManageDashboardView,ManageUserCreateView,ManageUserDeleteView,ManageUserUpdateView,IndexView,ManageDashboardView,ManageProductSubCategoryListView,ManageProductSubCategoryCreateView,ManageProductCategoryEditView,ManageProductSubCategoryDeleteView,ManageProductListView,ManageProductCreateView,ManageProductDeleteView,ManageProductCategoryListView,ManageProductCategoryCreateView,ManageProductCategoryDeleteView,ManageUserListView
from control_panel.views import *

# app_name = 'user_management'  # Set the app namespace here
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),

    path('users/', ManageUserListView.as_view(), name='manage_user_list'),
    path('users/create/', ManageUserCreateView.as_view(), name='manage_user_create'),
    path('admin/users/update/<int:pk>/', ManageUserUpdateView.as_view(), name='manage_user_update'),
    path('users/delete/<int:user_id>/', ManageUserDeleteView.as_view(), name="manage_user_delete"),

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
  


# product_sub_category
    path('product_sub_category/', ManageProductSubCategoryListView.as_view(), name='manage_product_sub_category_list'),
    path("product_sub_categories/create/", ManageProductSubCategoryCreateView.as_view(), name="manage_product_sub_category_create"),
    path('product_sub_categories/<int:pk>/edit/', ManageProductSubCategoryEditView.as_view(), name='manage_product_sub_category_edit'),
    path('product_sub_categories/delete/<int:pk>/', ManageProductSubCategoryDeleteView.as_view(), name='manage_product_sub_category_delete'),

    # Product URLs
    path('products/', ManageProductListView.as_view(), name='manage_product_list'),
    path("products/create/", ManageProductCreateView.as_view(), name="manage_product_create"),
    path("products/edit/<int:pk>/", ManageProductEditView.as_view(), name="manage_product_edit"),
    path("products/delete/<int:pk>/", ManageProductDeleteView.as_view(), name="manage_product_delete"),

    # Product Category URLs
    path('product_categories/', ManageProductCategoryListView.as_view(), name='manage_product_category_list'),
    path("product_categories/create/", ManageProductCategoryCreateView.as_view(), name="manage_product_category_create"),
    path("product_categories/edit/<int:pk>/", ManageProductCategoryEditView.as_view(), name="manage_product_category_edit"),
    path("product_categories/delete/<int:pk>/", ManageProductCategoryDeleteView.as_view(), name="manage_product_category_delete"),

    #store urls by priya
    path('stores/', ManageStoreView.as_view(), name='manage_Store_list'),
    path('stores/create/', ManageCreateStore.as_view(), name='manage_create_store'),
    path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
    path('toggle-store-status/<int:store_id>/', ToggleStoreStatus.as_view(), name='toggle_store_status'),


    #store category url
    path('stores/category/', ManageStoreCategoryView.as_view(), name='manage_Store_category_list'),
    path('store-category/create/', ManageCreateStoreCategoryView.as_view(), name='manage_create_store_category'),
    path("store-category/delete/<int:category_id>/", ManageDeleteStoreCategoryView.as_view(), name="delete_store_category"),
    path('toggle-store-category-status/<int:category_id>/', ToggleStoreCategoryStatus.as_view(), name='toggle_store_cetegory_status'),

    path('stores/category/update/<int:pk>/',ManageCategoryUpdateStoreView.as_view(), name='manage_update_store_category'),
]