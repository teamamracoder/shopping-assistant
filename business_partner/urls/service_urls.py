from django.urls import path, re_path
from ..views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="Service API",
        default_version='v1',
        description="Swagger documentation for Service & Service Type endpoints",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

urlpatterns = [
    # API endpoints
    path('services/', ServiceListCreateAPIView.as_view(), name='api_service_list_create'),
    path('services/<int:pk>/', ServiceDetailAPIView.as_view(), name='api_service_detail'),
    path('service-types/', ServiceTypeListCreateAPIView.as_view(), name='api_service_type_list_create'),
    path('service-types/<int:pk>/', ServiceTypeDetailAPIView.as_view(), name='api_service_type_detail'),

    # Swagger docs 
    re_path(r'^swagger/service/$', schema_view.with_ui('swagger', cache_timeout=0), name='app-swagger-ui'),
]



