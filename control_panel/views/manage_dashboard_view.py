from django.shortcuts import render
from django.views import View
# from django.contrib.auth.models import UserModel  # or your custom user model
from control_panel.models import StoreModel, ProductsModel, ServiceModel, UserModel  # import your actual models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from constants import Role
from decorators.validator import role_required


class ManageDashboardView(View):
    @role_required(Role.ADMIN, Role.SERVICE_PROVIDER)
    def get(self, request):
        user_session = request.session.get('auth')
        print('dash res',user_session)
        context = {
            'total_users': UserModel.objects.count(),
            'total_stores': StoreModel.objects.count(),
            'total_products': ProductsModel.objects.count(),
            'total_services': ServiceModel.objects.count(),
        }
        return render(request, "admin/dashboard.html", context)
