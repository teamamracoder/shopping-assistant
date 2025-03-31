from django.urls import path

from control_panel.views import *
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),
    path('users/', ManageUserView.as_view(), name='manage_user_list'),
    path('stores/', ManageStoreView.as_view(), name='manage_Store_list'),
    path('stores/create/', ManageCreateStore.as_view(), name='manage_create_store'),
    path('stores/update/<int:pk>/', ManageUpdateStoreView.as_view(), name='manage_update_store'),
  
]