from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ServiceType

class ServiceTypeService:
    def get_all_servicetypes(self):
        """
        Fetch all service types from the database.
        :return: Queryset of all ServiceType instances.
        """
        return ServiceType.objects.all()

    def get_user_by_id(self,pk):
        """
        Fetch a service type by its primary key (ID).
        :param pk: Primary key (ID) of the service type.
        :return: ServiceType instance if found, None otherwise.
        """
        try:
            return ServiceType.objects.get(pk=pk)
        except ServiceType.DoesNotExist:
            return None

    def update_service_type(self, service_type, validated_data):
        """
        Update an existing service type with new validated data.
        :param service_type: ServiceType instance to be updated.
        :param validated_data: A dictionary of data to update the service type with.
        :return: Updated ServiceType instance.
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
        :param service_type: ServiceType instance to be deleted.
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
        :param service_type: ServiceType instance to be activated.
        :return: Activated ServiceType instance.
        """
        service_type.is_active = True
        service_type.save()
        return service_type

    def deactivate_service_type(self, service_type):
        """
        Deactivate a service type.
        :param service_type: ServiceType instance to be deactivated.
        :return: Deactivated ServiceType instance.
        """
        service_type.is_active = False
        service_type.save()
        return service_type