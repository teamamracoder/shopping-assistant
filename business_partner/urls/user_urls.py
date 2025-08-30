from django.urls import path
from business_partner.views import UserListCreateAPIView, UserDetailAPIView, MyCustomerListAPIView

urlpatterns = [
    # User URLs
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/my-customers/', MyCustomerListAPIView.as_view(), name='my-customer-list'),
]
