from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path

# Import schema_view for Swagger & Redoc documentation
from .swagger import schema_view  # Adjust the import path as needed
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Hello API",
      default_version='v1',
      description="A simple DRF API to greet users",
      contact=openapi.Contact(email="hello@example.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Welcome"})),
    path("admin/", admin.site.urls),
    path("api/v1/shopping-assistant/", include("shopping_assistant.urls")),
    path("api/v1/business-partner/", include("business_partner.urls")),
    path("control-panel/", include("control_panel.urls")),



    # Swagger & Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
