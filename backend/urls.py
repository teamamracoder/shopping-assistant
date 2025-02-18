from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Welcome"})),
    path("admin/", admin.site.urls),
    path("api/v1/shopping-assistant", include("shopping_assistant.urls")),
    path("api/v1/business-partner", include("business_partner.urls")),
    path("control-panel", include("control_panel.urls")),
]
