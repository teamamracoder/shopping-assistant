from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path

# Import schema_view for Swagger & Redoc documentation
from .swagger import schema_view  # Adjust the import path as needed

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Welcome"})),
    path("admin/", admin.site.urls),
    path("api/v1/shopping-assistant/", include("shopping_assistant.urls")),
    path("api/v1/business-partner/", include("business_partner.urls")),
    path("control-panel/", include("control_panel.urls")),



    # Swagger & Redoc URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
