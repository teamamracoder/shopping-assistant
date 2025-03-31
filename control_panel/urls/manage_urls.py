from django.urls import path

from control_panel.views import IndexView,ManageDashboardView,ManageUserView,ManageProductSubCategoryListView
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),
    path('users/', ManageUserView.as_view(), name='manage_user_list'),
    path('product_sub_category/', ManageProductSubCategoryListView.as_view(), name='manage_product_sub_category_list'),
    # path('product_sub_category/', ManageProductSubCategoryCreateView.as_view(), name='manage_product_sub_category_list'),
  
]