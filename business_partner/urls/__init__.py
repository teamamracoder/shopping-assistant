from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "You are accessing business partner"})),
    path("", include("business_partner.urls.demo_urls")),
    path("", include("business_partner.urls.user_urls")),
    path("", include("business_partner.urls.store_urls")),
    path("", include("business_partner.urls.store_category_urls")),
]
