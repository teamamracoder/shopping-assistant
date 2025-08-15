from django.urls import path
from ..views import StoreListCreateView, StoreDetailView

urlpatterns = [
    path('stores/', StoreListCreateView.as_view(), name='store_list_create'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store_detail'),
]