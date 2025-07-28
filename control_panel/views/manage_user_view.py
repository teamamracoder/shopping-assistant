from urllib import request
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
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from ..models import UserModel
from django.utils.http import urlencode

#List (READ ALL)
class ManageUserListView(View):
    def get(self, request):
        users = UserModel.objects.all()
        form = ManageUserForm()
        choices_gender = [{type.value : type.name} for type in Gender]
        choices_role = [{type.value : type.name} for type in Role]
        return render(request, "admin/manage_all_user.html", {'users': users, 'form': form, 'choices_gender': choices_gender, 'choices_role' : choices_role   })

# CREATE VIEW (not working properly)
class ManageUserCreateView(View):
    def get(self, request):
        users = UserModel.objects.all()
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

                # Normalize to list of ints
                roles = [int(r) for r in roles_raw] if isinstance(roles_raw, list) else [int(roles_raw)]

                print("Roles being saved:", roles)

                UserModel.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    dob=form.cleaned_data['dob'],
                    gender=form.cleaned_data['gender'],
                    phone=form.cleaned_data['phone'],
                    address=form.cleaned_data['address'],
                    location=form.cleaned_data['location'],
                    city=form.cleaned_data['city'],
                    district=form.cleaned_data['district'],
                    state=form.cleaned_data['state'],
                    pincode=form.cleaned_data['pincode'],
                    roles=roles,
                )

                messages.success(request, 'User created successfully.')
                form = ManageUserForm()  # reset

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
        else:
            users = UserModel.objects.all()
            return render(request, "admin/manage_all_user.html", {
                'users': users,
                'form': form,
                'choices_gender': choices_gender,
                'choices_role': choices_role
            })

    # def post(self, request):
    #     form = ManageUserForm(request.POST)
    #     users = UserModel.objects.all()
    #     choices_gender = [{type.value: type.name} for type in Gender]
    #     choices_role = [{type.value: type.name} for type in Role]

    #     if form.is_valid():
    #         user_data = UserModel.objects.create(
    #         first_name=form.cleaned_data['first_name'],
    #         last_name=form.cleaned_data['last_name'],
    #         email=form.cleaned_data['email'],
    #         dob=form.cleaned_data['dob'],
    #         gender=form.cleaned_data['gender'],
    #         phone=form.cleaned_data['phone'],
    #         address=form.cleaned_data['address'],
    #         location=form.cleaned_data['location'],
    #         city=form.cleaned_data['city'],
    #         district=form.cleaned_data['district'],
    #         state=form.cleaned_data['state'],
    #         pincode=form.cleaned_data['pincode'],
    #         roles=form.cleaned_data['roles']
    #         )
    #         messages.success(request, 'User created successfully.')
    #         form = ManageUserForm()  # reset the form
    #     else:
    #         print("Form errors:", form.errors)

    #     return render(request, "admin/manage_all_user.html", {
    #         'users': users,
    #         'form': form,
    #         'choices_gender': choices_gender,
    #         'choices_role': choices_role
    #     })

#DELETE VIEW
class ManageUserDeleteView(View):
    # View method to handle POST request for deleting a user
    def post(self, request, user_id):
        # Call the service method to delete the specified user
        services.user_service.manage_user_delete(user_id)
        
        # Redirect to the user management list page after deletion
        return redirect("manage_user_list")
    

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


# TOGGLE VIEW
class ManageToggleUserActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        user = get_object_or_404(UserModel, pk=pk)
        user.is_active = not user.is_active
        user.save()
        status = "activated" if user.is_active else "deactivated"
        messages.success(request, f"User '{user.first_name}' has been {status}.")
        print(status)
        return redirect('manage_user_list')
    

## Consumer ##
class ConsumerListView(View):
    def get(self, request):
        # This is correct now (passing [1] instead of just 1)
        consumers = UserModel.objects.filter(roles__contains=[Role.END_USER.value])

        form = ManageUserForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        choices_role = [{type.value: type.name} for type in Role]

        return render(request, "admin/consumer_list.html", {
            'users': consumers,
            'form': form,
            'choices_gender': choices_gender,
            'choices_role': choices_role
        })