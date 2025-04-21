from django.urls import path
from ..views.service_booking_view import *

urlpatterns = [
    path('service-bookings/', ServiceBookingListCreateAPIView.as_view(), name='service_booking_list_create'),
    path('service-bookings/<int:pk>/', ServiceBookingDetailAPIView.as_view(), name='service_booking_detail'),
]
