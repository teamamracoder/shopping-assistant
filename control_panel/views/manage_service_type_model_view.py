# views.py
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceTypeModel
from ..forms import ServiceTypeForm
from services import ServiceTypeModelService
service_helper = ServiceTypeModelService()

# READ ALL
class ManageServiceTypeListView(View):
    def get(self, request):
        services = service_helper.get_all_ServiceTypeModels()  # Call service method
        form = ServiceTypeForm()
        return render(request, 'admin/manage_service_type_model.html', {
            'services': services,
            'form': form
        })

# CREATE
class ManageServiceTypeCreateView(View):
    def get(self,request):
        services = ServiceTypeModel.objects.all()
        form = ServiceTypeForm()
        return render(request, 'admin/manage_service_type_model.html', {'services': services,'form': form  })
    
    def post(self, request):
        print("POST request received.")
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            service = ServiceTypeModelService()
            service.create_service_type(form, request.user)
        else:
            print("Form errors:", form.errors)
        return redirect('manage_service_type_model_list')

# UPDATE
class ManageServiceTypeUpdateView(View):
    def post(self, request, pk):
        service_instance = service_helper.get_service_type_by_id(pk)
        form = ServiceTypeForm(request.POST, instance=service_instance)
        if form.is_valid():
            service = ServiceTypeModelService()
            service.update_service_type(form)
        return redirect('manage_service_type_model_list')

# DELETE
class ManageServiceTypeDeleteView(View):
    def post(self, request, pk):
        service_ins = service_helper.get_service_type_by_id(pk)
        service_helper.delete_service_type(service_ins)
        return redirect('manage_service_type_model_create')
    
 #TOGGLE VIEW   
class ManageToggleServiceTypeActiveView(View):
    def post(self, request, pk):
        service_type = service_helper.get_service_type_by_id(pk)
        updated_service = service_helper.toggle_active_status(service_type)
        status = "activated" if updated_service.is_active else "deactivated"
        messages.success(request, f"Service Type '{updated_service}' has been {status}.")
        return redirect('manage_service_type_model_list')