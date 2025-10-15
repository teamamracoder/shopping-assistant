from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceModel,ServiceTypeModel,UserModel
from ..forms .manage_service_model_form  import *
from django.views import View
from django.contrib import messages
from services import ServiceService
from utils.common_utils import get_user_id

service_helper = ServiceService()
from decorators.validator import role_required
from constants import Role

# LIST VIEW (READ ALL)
class ManageServiceModelListView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request):
        form = ServiceModelForm()
        services_ins = service_helper.get_all_services()

        return render(request, 'admin/manage_service_model.html', {
            'form': form,
            'services_model_data': services_ins,
        })


# CREATE VIEW
class ManageServiceModelCreateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request):
        form = ServiceModelForm()
        return render(request, 'admin/manage_service_model.html', {'form': form})
    
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request):
        print("[DEBUG] Current user:", get_user_id(request))
        form = ServiceModelForm(request.POST)
        if form.is_valid():
            service_instance = form.save(commit=False)  # get model instance without saving

            # Assign created_by and updated_by
            user_id = get_user_id(request)
            service_instance.created_by = user_id
            service_instance.updated_by = user_id

            try:
                service_instance.save()
                messages.success(request, "Service added successfully!", extra_tags="service")
                return redirect('manage_service_list')
            except Exception as e:
                form.add_error(None, f"Error saving service: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, 'admin/manage_service_model.html', {'form': form})


# UPDATE VIEW
class ManageServiceModelUpdateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request, pk):
        service = service_helper.get_service_by_id(pk=pk)
        form = ServiceModelForm(instance=service)
        return render(request, 'admin/manage_service_model.html', {'form': form, 'service': service})
    
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        service_instance = service_helper.get_service_by_id(pk=pk)
        if not service_instance:
            messages.error(request, "Service not found.")
            return redirect('manage_service_list')

        form = ServiceModelForm(request.POST, instance=service_instance)
        if form.is_valid():
            service_instance = form.save(commit=False)

            # Assign updated_by
            service_instance.updated_by = get_user_id(request)

            try:
                service_instance.save()
                messages.success(request, "Service updated successfully!", extra_tags="service")
                return redirect('manage_service_list')
            except Exception as e:
                form.add_error(None, f"Error updating service: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, 'admin/manage_service_model.html', {'form': form, 'service': service_instance})


# DELETE VIEW
class ManageServiceModelDeleteView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request, pk):
        service = service_helper.get_service_by_id(pk=pk)
        return render(request, 'admin/manage_service_model.html', {'service': service})
    
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        service = service_helper.get_service_by_id(pk=pk)
        service_helper.delete_service(service)
        messages.success(request, "Service deleted successfully!", extra_tags="service")
        return redirect('manage_service_list')
    
#TOGGLE VIEW
class ManageToggleServiceModelActiveView(View): 
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        service_ins = service_helper.get_service_by_id(pk=pk)
        updated_service = service_helper.toggle_active_status(service_ins)
        status = "activated" if updated_service.is_active else "deactivated"
        messages.success(request, f"Service '{updated_service.service_type}' has been {status}.", extra_tags="service")
        return redirect('manage_service_list')
    