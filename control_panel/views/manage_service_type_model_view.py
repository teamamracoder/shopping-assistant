# views.py
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceTypeModel
from ..forms import ServiceTypeForm

# READ ALL
class ManageServiceTypeListView(View):
    def get(self, request):
        services = ServiceTypeModel.objects.all()
        form = ServiceTypeForm()
        return render(request, 'admin/manage_service_type_model.html', {'services': services,'form': form  })

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
            instance = form.save(commit=False)
            instance.created_by = request.user if request.user.is_authenticated else None
            instance.updated_by = request.user if request.user.is_authenticated else None
            instance.save()
        else:
            print("Form errors:", form.errors)
        return redirect('manage_service_type_model_list')


# UPDATE
class ManageServiceTypeUpdateView(View):
    def post(self, request, pk):
        service = get_object_or_404(ServiceTypeModel, pk=pk)
        form = ServiceTypeForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
        return redirect('manage_service_type_model_list')


# DELETE
class ManageServiceTypeDeleteView(View):
    def post(self, request, pk):
        service = get_object_or_404(ServiceTypeModel, id=pk)
        service.delete()
        return redirect('manage_service_type_model_create')
    
    
 #TOGGLE VIEW   
class ManageToggleServiceTypeActiveView(View):
    def post(self,request, pk):
        service_type = get_object_or_404(ServiceTypeModel,id=pk)
        service_type.is_active = not service_type.is_active
        service_type.save()

        status = "activated" if service_type.is_active else "deactivated"
        messages.success(request, f"User '{service_type.is_active}' has been {status}.")
        
        return redirect('manage_service_type_model_list')

