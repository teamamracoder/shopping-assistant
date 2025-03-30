from django.shortcuts import render
from django.views import View

class ManageUserView(View):
    def get(self, request):
        return render(request, "admin/manage_all_user.html")
