from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404, render
from constants import Gender
from services import services  
from ..forms import ManageUserCreateForm,ManageUserUpdateForm
from control_panel.models import UserModel
from django.shortcuts import render, redirect
from constants import Gender,Role



class ManageUserCreateView(View):
    def get(self, request):
        users = UserModel.objects.all()  # Fetch all users
        form = ManageUserCreateForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        return render(request, "admin/manage_all_user.html", {'form': form,'choices_gender': choices_gender,'users':users})

    def post(self, request):
        form = ManageUserCreateForm(request.POST)
        if form.is_valid():
            user_data = UserModel.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name  = form.cleaned_data['last_name'],
                email      = form.cleaned_data['email'],
                dob        = form.cleaned_data['dob'],
                gender     = form.cleaned_data['gender'],
                address    = form.cleaned_data['address'],
                location   = form.cleaned_data['location'],
                city       = form.cleaned_data['city'],
                district   = form.cleaned_data['district'],
                state      = form.cleaned_data['state'],
                pincode    = form.cleaned_data['pincode'],
                roles      = [Role.END_USER.value],
            )
            return redirect("manage_user_list")
        return render(request, "admin/manage_all_user.html", {'form': form})

class ManageUserListView(View):
    def get(self, request):
        users = UserModel.objects.all() 
        return render(request, "admin/manage_all_user.html", {"users": users})
    

class ManageUserUpdateView(View):
    def get(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)  # Ensure user exists
        form = ManageUserUpdateForm(instance=user)
        return render(request, "admin/manage_user_update.html", {"form": form, "user": user})

    def post(self, request, user_id):
        user = get_object_or_404(UserModel, id=user_id)
        form = ManageUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("manage_users")  # Redirect to user list page
        return render(request, "admin/manage_user_update.html", {"form": form, "user": user})


# class ManageUserUpdateView(View):
#     def get(self, request, user_id):
#         user = UserModel.objects.get(id=user_id)
#         form = ManageUserUpdateForm(initial={
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'dob': user.dob,
#             'gender': user.gender,
#             'phone': user.phone,  
#             'address': user.address,
#             'location': user.location,
#             'city': user.city,
#             'district': user.district,
#             'state': user.state,
#             'pincode': user.pincode,
#         })
#         return render(request, "admin/manage_all_user.html", {'form': form, 'user': user})

#     def post(self, request, user_id):
#         user = UserModel.objects.get(id=user_id)
#         form = ManageUserUpdateForm(request.POST)
#         if form.is_valid():
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.dob = form.cleaned_data['dob']
#             user.gender = form.cleaned_data['gender']
#             user.phone = form.cleaned_data['phone']  
#             user.address = form.cleaned_data['address']
#             user.location = form.cleaned_data['location']
#             user.city = form.cleaned_data['city']
#             user.district = form.cleaned_data['district']
#             user.state = form.cleaned_data['state']
#             user.pincode = form.cleaned_data['pincode']
#             user.save()
#             return JsonResponse({"message": "User updated successfully"}, status=200)

#         return JsonResponse({"error": "Invalid data", "errors": form.errors}, status=400)





# class ManageUserUpdateView(View):
#     def get(self, request, user_id):
#         user = UserModel.objects.get(id=user_id)
#         form = ManageUserUpdateForm(initial={
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'email': user.email,
#             'dob': user.dob,
#             'gender': user.gender,
#             'contact': user.phone,
#             'address': user.address,
#             'location': user.location,
#             'city': user.city,
#             'district': user.district,
#             'state': user.state,
#             'pincode': user.pincode,
#         })
#         return render(request, "admin/manage_user_update.html", {'form': form, 'user': user})

#     def post(self, request, user_id):
#         user = UserModel.objects.get(id=user_id)
#         form = ManageUserUpdateForm(request.POST)
#         if form.is_valid():
#             user.first_name = form.cleaned_data['first_name']
#             user.last_name = form.cleaned_data['last_name']
#             user.email = form.cleaned_data['email']
#             user.dob = form.cleaned_data['dob']
#             user.gender = form.cleaned_data['gender']
#             user.phone = form.cleaned_data['contact']
#             user.address = form.cleaned_data['address']
#             user.location = form.cleaned_data['location']
#             user.city = form.cleaned_data['city']
#             user.district = form.cleaned_data['district']
#             user.state = form.cleaned_data['state']
#             user.pincode = form.cleaned_data['pincode']
#             user.save()
#             return redirect("manage_user_list")  # Redirect after successful update
#         return render(request, "admin/manage_user_update.html", {'form': form, 'user': user})

    # def get(self, request, user_id):
    #     user = get_object_or_404(UserModel, id=user_id)  # Assuming you have a User model
    #     form = ManageUserUpdateForm(initial={
    #         'first_name': user.first_name,
    #         'last_name': user.last_name,
    #         'email': user.email
    #     })
    #     return render(request, 'adminuser/user/update.html', {"form": form, "user_id": user.id})
    
    # def post(self, request, user_id):
    #     user = get_object_or_404(UserModel, id=user_id)
    #     # Update user fields
    #     user.first_name = request.POST.get("first_name", user.first_name)
    #     user.last_name = request.POST.get("last_name", user.last_name)
    #     user.email = request.POST.get("email", user.email)
    #     user.dob = request.POST.get("dob", user.dob)
    #     user.gender = request.POST.get("gender", user.gender)
    #     user.contact = request.POST.get("contact", user.contact)
    #     user.address = request.POST.get("address", user.address)
    #     user.location = request.POST.get("location", user.location)
    #     user.city = request.POST.get("city", user.city)
    #     user.district = request.POST.get("district", user.district)
    #     user.state = request.POST.get("state", user.state)
    #     user.pincode = request.POST.get("pincode", user.pincode)
    #     user.save()
    #     return JsonResponse({"message": "User updated successfully"}, status=200)
#-----------------------------------------------------------------------------
# def manage_get_user(user_id):
#     # Fetch the user object by ID or return a 404 error if not found
#     return get_object_or_404(User, id=user_id)
#-----------------------------------------------------------------------------

class ManageUserDeleteView(View):
    def post(self,request,user_id):
        user = UserModel.objects.get(id=user_id)
        user.delete()  # Delete user
        return redirect("manage_user_list")  # Redirect to list after deletion