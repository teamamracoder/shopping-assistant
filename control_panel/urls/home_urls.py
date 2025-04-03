from django.urls import path

from control_panel.views import IndexView,AdminView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', AdminView.as_view(), name='admin' ),
]