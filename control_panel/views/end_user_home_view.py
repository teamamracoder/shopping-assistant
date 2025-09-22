from urllib import request
from django.http import Http404, JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ValidationError
from services import services  
from ..forms import ManageUserForm
from control_panel.models import UserModel
from django.shortcuts import render, redirect
from constants import Gender,Role
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from ..models import UserModel
from django.utils.http import urlencode
from services import UserService
from decorators.validator import role_required
from django.utils.decorators import method_decorator


service = UserService()

#List (READ ALL)
class EndUserHome(View):
    @role_required(Role.END_USER.value)
    def get(self, request):
        return render(request,'enduser/end_user_home.html')