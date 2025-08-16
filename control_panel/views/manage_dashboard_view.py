from django.shortcuts import render
from django.views import View
# from django.contrib.auth.models import UserModel  # or your custom user model
from control_panel.models import StoreModel, ProductsModel, ServiceModel, UserModel  # import your actual models
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.decorators import jwt_required, role_required
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class ManageDashboardView(View):
    @jwt_required
    def get(self, request):
        return Response({"message": f"Welcome {request.user.email}, you are authenticated!"})
    
    def get(self, request):
        context = {
            'total_users': UserModel.objects.count(),
            'total_stores': StoreModel.objects.count(),
            'total_products': ProductsModel.objects.count(),
            'total_services': ServiceModel.objects.count(),
        }
        return render(request, "admin/dashboard.html", context)
