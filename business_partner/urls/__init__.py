from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "You are accessing business partner"})),
    path("", include("business_partner.urls.demo_urls")),
    path("", include("business_partner.urls.user_urls")),
    path("", include("business_partner.urls.store_urls")),
    path("", include("business_partner.urls.store_category_urls")),
    path("", include("business_partner.urls.service_urls")),
    path("", include("business_partner.urls.service_booking_urls")),
    path("", include("business_partner.urls.product_urls")),
    path("", include("business_partner.urls.product_category_urls")),
    path("", include("business_partner.urls.product_sub_category_urls")),
]
