from django.shortcuts import render
from django.views import View
# from django.contrib.auth.models import UserModel  # or your custom user model
from control_panel.models import StoreModel, ProductsModel, ServiceModel, UserModel  # import your actual models

class ManageDashboardView(View):
    def get(self, request):
        context = {
            'total_users': UserModel.objects.count(),
            'total_stores': StoreModel.objects.count(),
            'total_products': ProductsModel.objects.count(),
            'total_services': ServiceModel.objects.count(),
        }
        return render(request, "admin/dashboard.html", context)
