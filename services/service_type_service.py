from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ServiceTypeModel
from django.db import transaction

class ServiceTypeModelService:

    def get_all_ServiceTypeModels(self):
        return ServiceTypeModel.objects.all()
    
    def create_service_type(self, form, user):
        """
        Create and save a ServiceTypeModel instance with audit fields.
        """
        instance = form.save(commit=False)
        if user and user.is_authenticated:
            instance.created_by = user
            instance.updated_by = user
        else:
            instance.created_by = None
            instance.updated_by = None
        instance.save()
        return instance
    
    def get_service_type_by_id(self,pk):
        try:
            return ServiceTypeModel.objects.get(id=pk)
        except ServiceTypeModel.DoesNotExist:
            return None

    def update_service_type(self, form):
        form.save()
        """
        Update an existing service type with new validated data.
        :param service_type: ServiceTypeModel instance to be updated.
        :param validated_data: A dictionary of data to update the service type with.
        :return: Updated ServiceTypeModel instance.
        :raises ValidationError: If the updated data fails validation.
        """
        
    def delete_service_type(self, service_type):
        """
        Delete a service type.
        :param service_type: ServiceTypeModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            service_type.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting service type: {str(e)}")
    
    def toggle_active_status(self, service_type):
        """
        Activate a service type.
        :param service_type: ServiceTypeModel instance to be activated.
        :return: Activated ServiceTypeModel instance.
        """
        service_type.is_active = not service_type.is_active
        service_type.save()
        return service_type
        
    def deactivate_service_type(self, service_type):
        """
        Deactivate a service type.
        :param service_type: ServiceTypeModel instance to be deactivated.
        :return: Deactivated ServiceTypeModel instance.
        """
        service_type.is_active = False
        service_type.save()
        return service_type
    

# API Section for service_type table
class ServiceTypeModelAPI:
    def get_all_the_service_type(self):
        return ServiceTypeModel.objects.all()

    def get_service_type_by_id(self,pk):
        try:
            return ServiceTypeModel.objects.get(id=pk)
        except ServiceTypeModel.DoesNotExist:
            return None

    @transaction.atomic
    def create_the_service_type(self,data):
        service_type = ServiceTypeModel(**data)
        service_type.save()
        return service_type

    @transaction.atomic
    def update_the_service_type_by_id(self,service_type, data):
        for key, value in data.items():
            setattr(service_type, key, value)
        service_type.save()
        return service_type

    @transaction.atomic
    def delete_the_service_type_by_id(self, pk):
        try:
            service = ServiceTypeModel.objects.get(id=pk)
            service.delete()
            return service
        except ServiceTypeModel.DoesNotExist:
            return None
