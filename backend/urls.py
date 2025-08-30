from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from drf_spectacular.views import(
    SpectacularAPIView, 
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Welcome"})),
    path("admin/", admin.site.urls),
    path("api/v1/shopping-assistant/", include("shopping_assistant.urls")),
    path("api/v1/business-partner/", include("business_partner.urls")),
    path("control-panel/", include("control_panel.urls")),
    
    # Swagger + schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
