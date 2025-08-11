from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Shopping Assistant API",
      default_version='v1',
      description="API documentation Shopping Assistant",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
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
    path("auth/", include("auth_app.urls")),

    # Swagger & Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
]
