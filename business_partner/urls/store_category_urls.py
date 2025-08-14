from django.urls import path
from ..views import StoreCategoryListCreateView, StoreCategoryDetailView


urlpatterns = [
    path('store/categories/', StoreCategoryListCreateView.as_view()),
    path('store/categories/<int:pk>/', StoreCategoryDetailView.as_view()),
]



