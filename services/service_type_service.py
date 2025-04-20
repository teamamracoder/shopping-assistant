from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ServiceTypeModel
from django.db import transaction
class ServiceTypeModelService:
    def get_all_ServiceTypeModels(self):
        """
        Fetch all service types from the database.
        :return: Queryset of all ServiceTypeModel instances.
        """
        return ServiceTypeModel.objects.all()

    def get_user_by_id(self,pk):
        """
        Fetch a service type by its primary key (ID).
        :param pk: Primary key (ID) of the service type.
        :return: ServiceTypeModel instance if found, None otherwise.
        """
        try:
            return ServiceTypeModel.objects.get(pk=pk)
        except ServiceTypeModel.DoesNotExist:
            return None

    def update_service_type(self, service_type, validated_data):
        """
        Update an existing service type with new validated data.
        :param service_type: ServiceTypeModel instance to be updated.
        :param validated_data: A dictionary of data to update the service type with.
        :return: Updated ServiceTypeModel instance.
        :raises ValidationError: If the updated data fails validation.
        """
        try:
            service_type.service_name = validated_data.get('service_name', service_type.service_name)
            service_type.is_active = validated_data.get('is_active', service_type.is_active)
            service_type.created_by = validated_data.get('created_by', service_type.created_by)
            service_type.updated_by = validated_data.get('updated_by', service_type.updated_by)

            service_type.save()
            return service_type
        except IntegrityError:
            raise ValidationError("Service type update failed due to integrity issues.") 

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
    
    def activate_service_type(self, service_type):
        """
        Activate a service type.
        :param service_type: ServiceTypeModel instance to be activated.
        :return: Activated ServiceTypeModel instance.
        """
        service_type.is_active = True
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
