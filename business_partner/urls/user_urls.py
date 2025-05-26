from django.urls import path
from ..views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    # User URLs
    path('users', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
]
