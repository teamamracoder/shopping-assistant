from django.urls import path
from control_panel.views import IndexView,ManageDashboardView,ManageUserCreateView,ManageUserListView,ManageUserDeleteView,ManageUserUpdateView

from control_panel.views import IndexView,ManageDashboardView,ManageUserView,ManageProductSubCategoryListView,ManageProductSubCategoryCreateView,ManageProductCategoryEditView,ManageProductSubCategoryDeleteView,ManageProductListView,ManageProductCreateView,ManageProductDeleteView,ManageProductCategoryListView,ManageProductCategoryCreateView,ManageProductCategoryDeleteView
from control_panel.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),
    path('users/', ManageUserCreateView.as_view(), name='manage_user_list'),
    path('users/create/<int:user_id>/', ManageUserCreateView.as_view(), name='manage_user_list'),
    path('admin/users/get/<int:user_id>/', ManageUserUpdateView.as_view(), name='manage_user_update'),
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
  

]