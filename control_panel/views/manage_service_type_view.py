from django.shortcuts import render
from django.views import View
from ..forms .manage_store_form import *
from ..forms .manage_store_category_form import *
from ..forms .manage_service_type_form import *
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from ..models import UserModel,ServiceTypeModel,StoreCategoryModel
from services import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponseForbidden



class ManageServiceTypeView(View):
    def get(self, request):
        form = ServiceTypeForm()
        service_type_list = ServiceTypeModel.objects.all()
        # Split email strings into lists
       
        # return render(request, "admin/manage_store.html", {"form": form, "store_list": store_list})
        return render(request, "admin/manage_service_type.html", {"form": form, "service_type_list": service_type_list})
    
class ManageCreateServiceTypeView(View):
    def post(self, request, *args, **kwargs):
        form = ServiceTypeForm(request.POST)

        if form.is_valid():
            service_type = form.save(commit=False)
            user_instance = get_object_or_404(UserModel, id=1) 
            service_type.created_by = user_instance
            service_type.updated_by = user_instance
            service_type.save()
            messages.success(request, "Service type created successfully!")
            return redirect('manage_service_type_list')
        else:
            messages.error(request, "Error creating service type.")
            return render(request, 'manage_service_type_list', {'form': form})

