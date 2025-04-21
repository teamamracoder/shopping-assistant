from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceModel,ServiceTypeModel,UserModel
from ..forms .manage_service_model_form  import *
from django.views import View
from django.contrib import messages


# LIST VIEW (READ ALL)
class ManageServiceModelListView(View):
    def get(self, request):
        services_model_data = ServiceModel.objects.all()
        form = ServiceModelForm()
        services_with_names = []
        for service in services_model_data:
            service_type_name  = ServiceTypeModel.objects.filter(id = service.service_type_id).first()
            service_provider_name = UserModel.objects.filter(id=service.service_provider_id,is_service_provider=True).first()
            services_with_names.append({
                'service_type_name': service_type_name.service_name if service_type_name else 'N/A',
                'service_provider_name': service_provider_name.first_name if service_provider_name else 'N/A'
            })
        return render(request, 'admin/manage_service_model.html', {'services_model_data': services_model_data,'form': form,'services_with_names': services_with_names})


# CREATE VIEW
class ManageServiceModelCreateView(View):
    def get(self, request):
        form = ServiceModelForm()
        return render(request, 'admin/manage_service_model.html', {'form': form})
    
    def post(self, request):
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            # service.created_by = request.user # this will required while login or sign up feature will developed
            # service.updated_by = request.user # this will required while login or sign up feature will developed
            service.save()
            form.save()
            return redirect('manage_service_list')
        return render(request, 'admin/manage_service_model.html', {'form': form})


# UPDATE VIEW
class ManageServiceModelUpdateView(View):
    def get(self, request, pk):
        service = get_object_or_404(ServiceModel, pk=pk)
        form = ServiceModelForm(instance=service)
        return render(request, 'admin/manage_service_model.html', {'form': form, 'service': service})

    def post(self, request, pk):
        service = get_object_or_404(ServiceModel, pk=pk)
        form = ServiceModelForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.updated_by = request.user
            service.save()
            return redirect('manage_service_list')
        return render(request, 'admin/manage_service_model.html', {'form': form, 'service': service})


# DELETE VIEW
class ManageServiceModelDeleteView(View):
    def get(self, request, pk):
        service = get_object_or_404(ServiceModel, pk=pk)
        return render(request, 'admin/manage_service_model.html', {'service': service})
    
    def post(self, request, pk):
        service = get_object_or_404(ServiceModel, pk=pk)
        service.delete()
        return redirect('manage_service_list')
    
    
#TOGGLE VIEW
class ManageToggleServiceModelActiveView(View): 
    def post(self, request, pk):
        service = get_object_or_404(ServiceModel, pk=pk)
        service.is_active = not service.is_active 
        service.save()
        status = "activated" if service.is_active else "deactivated"
        messages.success(request, f"ServiceModel '{service.is_active}' has been {status}.")
        
        return redirect('manage_service_list')