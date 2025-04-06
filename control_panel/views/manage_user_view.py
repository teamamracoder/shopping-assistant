from django.http import Http404, JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, render
from constants import Gender
from services import services  
from ..forms import ManageUserForm
from control_panel.models import UserModel
from django.shortcuts import render, redirect
from constants import Gender,Role
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import IntegrityError


#List
class ManageUserListView(View):
    def get(self, request):
        users = UserModel.objects.all()
        form = ManageUserForm()
        return render(request, 'admin/manage_all_user.html', {"users": users, "form": form})

# from django.shortcuts import render, redirect
# from django.views import View
# from django.db import IntegrityError
# from .forms import ManageUserForm
# from .models import UserModel, Gender, Role

class ManageUserCreateView(View):
    def get(self, request):
        users = UserModel.objects.all()
        form = ManageUserForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        return render(request, "admin/manage_all_user.html", {'form': form, 'choices_gender': choices_gender, 'users': users})

    def post(self, request):
        form = ManageUserForm(request.POST)
        if form.is_valid():
            try:
                user_data = UserModel.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    dob=form.cleaned_data['dob'],
                    gender=form.cleaned_data['gender'],
                    address=form.cleaned_data['address'],
                    location=form.cleaned_data['location'],
                    city=form.cleaned_data['city'],
                    district=form.cleaned_data['district'],
                    state=form.cleaned_data['state'],
                    pincode=form.cleaned_data['pincode'],
                    roles=[Role.END_USER.value],
                )
                return redirect("manage_user_list", {'user_data': user_data})
            except IntegrityError:
                form.add_error(None, 'A user with this email or contact already exists.')
        print(form.errors)        
        return render(request, "admin/manage_all_user.html", {'form': form})

# class ManageUserCreateView(View):
#     def get(self, request):
#         users = UserModel.objects.all()
#         form = ManageUserForm()
#         choices_gender = [(type.value, type.name) for type in Gender]
#         return render(request, "admin/manage_all_user.html", {'form': form, 'choices_gender': choices_gender, 'users': users})

#     def post(self, request):
#         form = ManageUserForm(request.POST)
#         if form.is_valid():
#             try:
#                 user_data = UserModel.objects.create(
#                     first_name=form.cleaned_data['first_name'],
#                     last_name=form.cleaned_data['last_name'],
#                     email=form.cleaned_data['email'],
#                     dob=form.cleaned_data['dob'],
#                     gender=form.cleaned_data['gender'],
#                     address=form.cleaned_data['address'],
#                     location=form.cleaned_data['location'],
#                     city=form.cleaned_data['city'],
#                     district=form.cleaned_data['district'],
#                     state=form.cleaned_data['state'],
#                     pincode=form.cleaned_data['pincode'],
#                     roles=[Role.END_USER.value],
#                 )
#                 return redirect("manage_user_list")
#             except IntegrityError:
#                 form.add_error(None, 'A user with this email or contact already exists.')
#         return render(request, "admin/manage_all_user.html", {'form': form})




# class ManageUserCreateView(View):
#     def get(self, request):
#         users = UserModel.objects.all()  # Fetch all users
#         form = ManageUserForm()
#         choices_gender = [{type.value: type.name} for type in Gender]
#         return render(request, "admin/manage_all_user.html", {'form': form,'choices_gender': choices_gender,'users':users})

#     def post(self, request):
#         form = ManageUserForm(request.POST)
#         if form.is_valid():
#             user_data = UserModel.objects.create(
#                 first_name = form.cleaned_data['first_name'],
#                 last_name  = form.cleaned_data['last_name'],
#                 email      = form.cleaned_data['email'],
#                 dob        = form.cleaned_data['dob'],
#                 gender     = form.cleaned_data['gender'],
#                 address    = form.cleaned_data['address'],
#                 location   = form.cleaned_data['location'],
#                 city       = form.cleaned_data['city'],
#                 district   = form.cleaned_data['district'],
#                 state      = form.cleaned_data['state'],
#                 pincode    = form.cleaned_data['pincode'],
#                 roles      = [Role.END_USER.value],
#             )
#             return redirect("manage_user_list",{'user_data': user_data})
#         return render(request, "admin/manage_all_user.html", {'form': form})


class ManageUserDeleteView(View):
    def post(self,request,user_id):
        user = UserModel.objects.get(id=user_id)
        user.delete()  # Delete user
        return redirect("manage_user_list")  # Redirect to list after deletion


#Update
class ManageUserUpdateView(UpdateView):
    model = UserModel
    form_class = ManageUserForm
    success_url = reverse_lazy('manage_user_list')  # Redirect to user list after success

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # You can override this to customize if necessary
        return super().get(request, *args, **kwargs)

