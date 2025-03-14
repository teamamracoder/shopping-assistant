from django.urls import include, path

urlpatterns = [
    # path("", include("control_panel.urls.demo_urls")),
    path("", include("control_panel.urls.home_urls")),
]
