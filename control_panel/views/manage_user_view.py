from urllib import request
from django.http import Http404, JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ValidationError
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
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from ..models import UserModel
from django.utils.http import urlencode
from services import UserService


service = UserService()

#List (READ ALL)
class ManageUserListView(View):
     def get(self, request):
        users = service.get_all_users()  # call the service function

        form = ManageUserForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        choices_role = [{type.value: type.name} for type in Role]

        return render(request, "admin/manage_all_user.html", {'users': users,'form': form,
                'choices_gender': choices_gender,
                'choices_role': choices_role
            }
        )
     

# CREATE VIEW (not working properly)
class ManageUserCreateView(View):
    def get(self, request):
        users = service.get_all_users()
        form = ManageUserForm()
        choices_gender = [{type.value : type.name} for type in Gender]
        choices_role = [{type.value : type.name} for type in Role]
        return render(request, "admin/manage_all_user.html", {'users': users, 'form': form, 'choices_gender': choices_gender, 'choices_role' : choices_role })

    def post(self, request):
        form = ManageUserForm(request.POST)
        source_page = request.POST.get("source_page", "user")
        choices_gender = [{type.value: type.name} for type in Gender]
        choices_role = [{type.value: type.name} for type in Role]

        if form.is_valid():
            try:
                roles_raw = form.cleaned_data.get('roles')
                if not roles_raw:
                    raise ValueError("No roles selected")

                roles = [int(r) for r in roles_raw] if isinstance(roles_raw, list) else [int(roles_raw)]
                print("Roles being saved:", roles)

                validated_data = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'dob': form.cleaned_data['dob'],
                    'gender': form.cleaned_data['gender'],
                    'phone': form.cleaned_data['phone'],
                    'address': form.cleaned_data['address'],
                    'location': form.cleaned_data['location'],
                    'city': form.cleaned_data['city'],
                    'district': form.cleaned_data['district'],
                    'state': form.cleaned_data['state'],
                    'pincode': form.cleaned_data['pincode'],
                    'roles': roles,
                    'country': form.cleaned_data['country'],
                }

                service.create_user(validated_data)  #call service function
                messages.success(request, 'User created successfully.')               
               
                if(request.POST.get("seller")):
                    form = ManageUserForm()
                    users = UserModel.objects.filter(roles__contains=[Role.SELLER.value])
                    return render(request, "admin/partner_list.html", {
                    'users': users,
                    'form': form,
                    'choices_gender': choices_gender,
                    'choices_role': choices_role
                })

            except Exception as e:
                import traceback
                traceback.print_exc()
                messages.error(request, f"Error: {str(e)}")
        else:
            print("Form errors:", form.errors)

        # Return appropriate list view
        if source_page == "consumer":
            users = UserModel.objects.filter(roles__contains=[Role.END_USER.value])
            return render(request, "admin/consumer_list.html", {
                'users': users,
                'form': form,
                'choices_gender': choices_gender,
                'choices_role': choices_role
            })
        elif source_page == "service_provider":
            users = UserModel.objects.filter(roles__contains=[Role.SERVICE_PROVIDER.value])
            return render(request, "admin/service_provider_list.html", {"users": users, "form": form})
        else:
            users = UserModel.objects.all()
            return render(request, "admin/manage_all_user.html", {
                'users': users,
                'form': form,
                'choices_gender': choices_gender,
                'choices_role': choices_role
            })
        
        
# #DELETE VIEW
# class ManageUserDeleteView(View):
#     def post(self, request, user_id):
#         try:
#             print("+++++++++++++ ID = ",user_id)
#             service.user_delete(user_id)  #call the service method
#             messages.success(request, "User deleted successfully.")
#         except ValidationError as e:
#             messages.error(request, f"Error deleting user: {str(e)}")
#         return redirect("manage_user_list")
class ManageUserDeleteView(View):
    def post(self, request, user_id):
        try:
            print("+++++++++++++ ID = ", user_id)
            service.user_delete(user_id)  # call the service method
            messages.success(request, "User deleted successfully.")
        except ValidationError as e:
            messages.error(request, f"Error deleting user: {str(e)}")

        # Get the previous page URL (fallback to user list if missing)
        referer = request.META.get("HTTP_REFERER", reverse("manage_user_list"))
        return redirect(referer)
    

# class ManageUserUpdateView(UpdateView):
class ManageUserUpdateView(UpdateView):
    model = UserModel
    form_class = ManageUserForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('manage_user_list')  # fallback

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context
    
    def form_valid(self, form):
        try:
            validated_data = form.cleaned_data
            service.update_user(self.object, validated_data)  #use service layer
            messages.success(self.request, "User updated successfully.")
        except ValidationError as ve:
            form.add_error(None, ve.message)  # attach error to the form
            return self.form_invalid(form)
        except Exception as e:
            form.add_error(None, f"Unexpected error: {str(e)}")
            return self.form_invalid(form)
        return super().form_valid(form)


# TOGGLE VIEW
class ManageToggleUserActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        # user = get_object_or_404(UserModel, pk=pk)
        user = service.get_user_by_id(pk=pk)
        try:
            updated_user = service.toggle_user_active(user)
            status = "activated" if updated_user.is_active else "deactivated"
            messages.success(request, f"User '{updated_user.first_name}' has been {status}.")
        except ValidationError as e:
            messages.error(request, str(e))

        next_url = request.GET.get('next')
        return redirect(next_url) if next_url else redirect('manage_user_list')


class ConsumerListView(View):
    def get(self, request):
        consumers = service.get_users_by_role(Role.END_USER.value)
        context = UserService.common_user_context(consumers)
        return render(request, "admin/consumer_list.html", context)


# view for Partner
class ManagePartnerListView(View):
    def get(self, request):
        partners = service.get_users_by_role(Role.SELLER.value)
        context = UserService.common_user_context(partners)
        return render(request, "admin/partner_list.html", context)
    
## Service_Provider ##    
class ServiceProviderListView(View):
    def get(self, request):
        # This is correct now (passing [1] instead of just 1)
        service_provider = UserModel.objects.filter(roles__contains=[Role.SERVICE_PROVIDER.value])

        form = ManageUserForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        choices_role = [{type.value: type.name} for type in Role]

        return render(request, "admin/service_provider_list.html", {
            'users': service_provider,
            'form': form,
            'choices_gender': choices_gender,
            'choices_role': choices_role
        })