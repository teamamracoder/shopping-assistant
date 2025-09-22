from django.shortcuts import redirect, render
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
from django.utils.decorators import method_decorator
from utils.common_utils import get_user_id

class ManageDashboardView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value, Role.END_USER.value)
    def get(self, request):
        user_roles = request.session.get('auth', {}).get('user', {}).get('roles', [])        
        if Role.END_USER.value in user_roles and len(user_roles) == 1:
            return redirect('end_user_home')
        
        context = {
            'total_users': UserModel.objects.count(),
            'total_stores': StoreModel.objects.count(),
            'total_products': ProductsModel.objects.count(),
            'total_services': ServiceModel.objects.count(),
        }
        return render(request, "admin/dashboard.html", context)
