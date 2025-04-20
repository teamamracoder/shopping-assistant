from django.urls import path
from ..views import *
urlpatterns = [
    path('services/', ServiceListCreateAPIView.as_view(), name='api_service_list_create'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='api_service_detail'),
    path('service-types/', ServiceTypeListCreateAPIView.as_view(), name='api_service_type_list_create'),
    path('service-types/<int:pk>/', ServiceTypeDetailAPIView.as_view(), name='api_service_type_detail'),
]


