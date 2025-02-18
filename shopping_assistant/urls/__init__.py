from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "You are accessing shopping assistant"})),
    path("", include("shopping_assistant.urls.demo_urls")),
]
