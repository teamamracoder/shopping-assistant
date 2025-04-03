from django.shortcuts import render
from django.views import View

class ManageDashboardView(View):

    def get(self, request):
        return render(request, "admin/dashboard.html")