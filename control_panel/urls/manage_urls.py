from django.urls import path
from control_panel.views import IndexView,ManageDashboardView,ManageUserCreateView,ManageUserListView,ManageUserDeleteView,ManageUserUpdateView

# ManageUserListView, UserListView, UserDetailView, ManageUserUpdateView, ManageUserDeleteView
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', ManageDashboardView.as_view(), name='manage_dashboard'),
    path('users/create/', ManageUserCreateView.as_view(), name='manage_user_list'),
    path('users/create/<int:user_id>/', ManageUserCreateView.as_view(), name='manage_user_list'),
    path('users/delete/<int:user_id>/', ManageUserDeleteView.as_view(), name="manage_user_delete"),

     path('users/update/<int:user_id>/', ManageUserUpdateView.as_view(), name="manage_user_update"),
    # path('control-panel/users/get/<int:user_id>/', ManageUserDetailView.as_view(), name="manage_user_detail"),
]