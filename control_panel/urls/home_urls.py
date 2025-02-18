from django.urls import path

from control_panel.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]