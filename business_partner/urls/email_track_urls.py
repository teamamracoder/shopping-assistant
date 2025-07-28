from django.urls import path
from ..views.email_track_view import *

urlpatterns = [
    path('email-track/', EmailTrackCreateAPIView.as_view(), name='email_track_create'),
    path('email-track/<int:pk>/',EmailTrackDetailAPIView.as_view(), name='email-track-detail'),
    
]
