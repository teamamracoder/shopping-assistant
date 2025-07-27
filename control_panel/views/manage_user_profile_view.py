from django.shortcuts import render
from django.views import View
from django.contrib import messages
from ..forms.manage_user_profile_form import ManageUserProfileForm
from constants.enums import Gender
from ..models import UserModel


class ManageUserProfileView(View):
    template_name = 'admin/manage_user_profile.html'
    
    def get_user_instance(self):
        """Get user with id=1 (must exist)"""
        user = UserModel.objects.get(id=1)
        return user
    
    def get(self, request):
        """Display user profile form with user data from database"""
        user = self.get_user_instance()
        form = ManageUserProfileForm(instance=user)
        
        context = {
            'form': form,
            'user_data': user,
            'page_title': 'User Profile',
            'breadcrumb': 'Profile'
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request):
        """Handle profile update form submission"""
        user = self.get_user_instance()
        form = ManageUserProfileForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            form = ManageUserProfileForm(instance=user)
        else:
            messages.error(request, 'Please correct the errors below.')
        
        context = {
            'form': form,
            'user_data': user,
            'page_title': 'User Profile',
            'breadcrumb': 'Profile'
        }
        
        return render(request, self.template_name, context)