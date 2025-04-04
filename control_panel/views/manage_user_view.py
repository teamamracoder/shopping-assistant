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



class ManageUserCreateView(View):
    def get(self, request):
        users = UserModel.objects.all()  # Fetch all users
        form = ManageUserForm()
        choices_gender = [{type.value: type.name} for type in Gender]
        return render(request, "admin/manage_all_user.html", {'form': form,'choices_gender': choices_gender,'users':users})

    def post(self, request):
        form = ManageUserForm(request.POST)
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
    

# class ManageUserUpdateView(View):
#     def get(self, request, user_id):
#         user_id = 11
#         try:
#             user = UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             raise Http404("User not found")

#         data = {
#             "id": user.id,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "email": user.email,
#             "dob": user.dob.isoformat() if user.dob else "",
#             "gender": user.gender,
#             "contact": user.contact,
#             "address": user.address,
#             "location": user.location,
#             "city": user.city,
#             "district": user.district,
#             "state": user.state,
#             "pincode": user.pincode,
#         }
#         return JsonResponse(data)


    def post(self, request, user_id):
        user = get_object_or_404(UserModel, id=11)
        form = ManageUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("manage_users")  # Redirect to user list page
        return render(request, "admin/manage_all_user.html", {"form": form, "user_id": user.id})


class ManageUserDeleteView(View):
    def post(self,request,user_id):
        user = UserModel.objects.get(id=user_id)
        user.delete()  # Delete user
        return redirect("manage_user_list")  # Redirect to list after deletion
    






# Update user with POST data
@method_decorator(csrf_exempt, name='dispatch')
class ManageUserUpdateView(View):
    def post(self, request, pk):
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        form = ManageUserForm(request.POST)
        if form.is_valid():
            for field, value in form.cleaned_data.items():
                setattr(user, field, value)
            user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail', 'errors': form.errors})