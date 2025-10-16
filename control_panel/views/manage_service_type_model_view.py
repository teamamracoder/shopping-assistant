# views.py
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from ..models import ServiceTypeModel
from ..forms import ServiceTypeForm
from services import ServiceTypeModelService
from utils.common_utils import get_user_id

service_helper = ServiceTypeModelService()
from constants import Role
from decorators.validator import role_required

# READ ALL
class ManageServiceTypeListView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request):
        services = service_helper.get_all_ServiceTypeModels()  # Call service method
        form = ServiceTypeForm()
        return render(request, 'admin/manage_service_type_model.html', {
            'services': services,
            'form': form
        })

## create view ##
class ManageServiceTypeCreateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self,request):
        services = ServiceTypeModel.objects.all()
        form = ServiceTypeForm()
        return render(request, 'admin/manage_service_type_model.html', {'services': services, 'form': form})

    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request):
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            service_instance = form.save(commit=False)

            # Set created_by and updated_by
            service_instance.created_by = get_user_id(request)
            service_instance.updated_by = get_user_id(request)

            try:
                service_instance.save()
                messages.success(request, "Service Type added successfully!")
            except Exception as e:
                messages.error(request, f"Error saving Service Type: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return redirect('manage_service_type_model_list')


    # def post(self, request):
    #     print("POST request received.")
    #     form = ServiceTypeForm(request.POST)
    #     if form.is_valid():
    #         print("Form is valid")
    #         service = ServiceTypeModelService()
    #         service.create_service_type(form, request.user)
    #     else:
    #         print("Form errors:", form.errors)
    #     return redirect('manage_service_type_model_list')


## update view ##
class ManageServiceTypeUpdateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request, pk):
        service_instance = service_helper.get_service_type_by_id(pk)
        if not service_instance:
            messages.error(request, "Service Type not found.")
            return redirect('manage_service_type_model_list')

        form = ServiceTypeForm(instance=service_instance)
        return render(request, 'admin/manage_service_type_model.html', {'form': form, 'service': service_instance})

    def post(self, request, pk):
        service_instance = service_helper.get_service_type_by_id(pk)
        if not service_instance:
            messages.error(request, "Service Type not found.")
            return redirect('manage_service_type_model_list')

        old_created_by = service_instance.created_by  # ✅ Preserve created_by
        form = ServiceTypeForm(request.POST, instance=service_instance)

        if form.is_valid():
            service_instance = form.save(commit=False)

            # Preserve created_by
            service_instance.created_by = old_created_by
            # Update updated_by
            service_instance.updated_by = get_user_id(request)

            try:
                service_instance.save()
                messages.success(request, "Service Type updated successfully!")
            except Exception as e:
                messages.error(request, f"Error updating Service Type: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return redirect('manage_service_type_model_list')


    # def post(self, request, pk):
    #     service_instance = service_helper.get_service_type_by_id(pk)
    #     form = ServiceTypeForm(request.POST, instance=service_instance)
    #     if form.is_valid():
    #         service = ServiceTypeModelService()
    #         service.update_service_type(form)
    #     return redirect('manage_service_type_model_list')


# DELETE
class ManageServiceTypeDeleteView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        service_ins = service_helper.get_service_type_by_id(pk)
        service_helper.delete_service_type(service_ins)
        messages.success(request, "Service Type deleted successfully!")
        return redirect('manage_service_type_model_list')    
    # def post(self, request, pk):
    #     service_ins = service_helper.get_service_type_by_id(pk)
    #     service_helper.delete_service_type(service_ins)
    #     return redirect('manage_service_type_model_create')

 #TOGGLE VIEW
class ManageToggleServiceTypeActiveView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        service_type = service_helper.get_service_type_by_id(pk)
        updated_service = service_helper.toggle_active_status(service_type)
        status = "activated" if updated_service.is_active else "deactivated"
        messages.success(request, f"Service Type '{updated_service.service_name}' has been {status}.")
        return redirect('manage_service_type_model_list')    
    # def post(self, request, pk):
    #     service_type = service_helper.get_service_type_by_id(pk)
    #     updated_service = service_helper.toggle_active_status(service_type)
    #     status = "activated" if updated_service.is_active else "deactivated"
    #     messages.success(request, f"Service Type '{updated_service}' has been {status}.")
    #     return redirect('manage_service_type_model_list')