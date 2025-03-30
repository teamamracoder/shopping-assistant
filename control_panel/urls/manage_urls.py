from django.urls import path

from control_panel.views import IndexView,ManageDashboardView,ManageUserView
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),
    path('users/', ManageUserView.as_view(), name='manage_user_list'),
  
]