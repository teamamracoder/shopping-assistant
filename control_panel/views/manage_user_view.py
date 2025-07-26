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

# ---------------------------
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import UserModel
from ..forms import ManageUserForm
from django.contrib import messages


#List (READ ALL)
class ManageUserListView(View):
    def get(self, request):
        users = services.manage_user_service.get_all_users()

        # Initialize an empty form for user creation or management
        form = ManageUserForm()

        # Generate gender choices from the Gender enum (as a list of dictionaries)
        choices_gender = [{type.value : type.name} for type in Gender]

        # Generate role choices from the Role enum (as a list of dictionaries)
        choices_role = [{type.value : type.name} for type in Role]

        # Render the 'manage_all_user.html' template with the user list, form, and choice data
        return render(request, "admin/manage_all_user.html", {
            'users': users,
            'form': form,
            'choices_gender': choices_gender,
            'choices_role': choices_role
        })


# CREATE VIEW (not working properly)
class ManageUserCreateView(View):
    def get(self, request):
        users = services.manage_user_service.get_all_users()
        form = ManageUserForm()
        choices_gender = [{type.value : type.name} for type in Gender]
        choices_role = [{type.value : type.name} for type in Role]
        return render(request, "admin/manage_all_user.html", {'users': users, 'form': form, 'choices_gender': choices_gender, 'choices_role' : choices_role })

    def post(self, request):
        # Initialize the form with POST data from the request
        form = ManageUserForm(request.POST) 
        # Fetch all users to be displayed on the template
        users = services.manage_user_service.get_all_users()
        # Prepare gender choices for rendering in the form (as list of dictionaries)
        choices_gender = [{type.value: type.name} for type in Gender]
        # Prepare role choices for rendering in the form (as list of dictionaries)
        choices_role = [{type.value: type.name} for type in Role]

        # Validate the submitted form data
        if form.is_valid():
            # Extract cleaned form data into a dictionary for user creation
            user_data = {
                'first_name' : form.cleaned_data['first_name'],
                'last_name'  : form.cleaned_data['last_name'],
                'email'      : form.cleaned_data['email'],
                'dob'        : form.cleaned_data['dob'],
                'gender'     : form.cleaned_data['gender'],
                'phone'      : form.cleaned_data['phone'],
                'address'    : form.cleaned_data['address'],
                'country'    :  form.cleaned_data['country'],
                'location'   : form.cleaned_data['location'],
                'city'       : form.cleaned_data['city'],
                'district'   : form.cleaned_data['district'],
                'state'      : form.cleaned_data['state'],
                'pincode'    : form.cleaned_data['pincode'],
                'roles'      : form.cleaned_data['roles'],
            }
            # Call the service to create a new user with the form data
            services.manage_user_service.manage_create_user(**user_data)
            # Display a success message to the admin
            messages.success(request, 'User created successfully.')
            # Reset the form after successful submission
            form = ManageUserForm()  # reset the form
        else:
            # Print form errors for checking purposes
            print("Form errors:", form.errors)

        # Render the template with users list, form, and gender/role choices
        return render(request, "admin/manage_all_user.html", {
            'users': users,
            'form': form,
            'choices_gender': choices_gender,
            'choices_role': choices_role
        })

#DELETE VIEW
class ManageUserDeleteView(View):
    # View method to handle POST request for deleting a user
    def post(self, request, user_id):
        # Call the service method to delete the specified user
        services.manage_user_service.manage_user_delete(user_id)
        
        # Redirect to the user management list page after deletion
        return redirect("manage_user_list")
    

class ManageUserUpdateView(UpdateView):
    model = UserModel
    form_class = ManageUserForm
    success_url = reverse_lazy('manage_user_list')  # Redirect to user list after success

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        # You can override this to customize if necessary
        return super().get(request, *args, **kwargs)

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