from django.urls import path
from ..views import *

urlpatterns = [
    path('demo/', DemoView.as_view(), name='demo'),
]