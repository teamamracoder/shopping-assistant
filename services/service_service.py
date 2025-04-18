from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ServiceModel

class ServiceService:
    def get_all_services(self):
        """
        Fetch all services from the database.
        :return: Queryset of all ServiceModel instances.
        """
        return ServiceModel.objects.all()

    def get_service_by_id(self, pk):
        """
        Fetch a service by its primary key (ID).
        :param pk: Primary key (ID) of the service.
        :return: ServiceModel instance if found, None otherwise.
        """
        try:
            return ServiceModel.objects.get(pk=pk)
        except ServiceModel.DoesNotExist:
            return None

    def update_service(self, service, validated_data):
        """
        Update an existing service with new validated data.
        :param service: ServiceModel instance to be updated.
        :param validated_data: A dictionary of data to update the service with.
        :return: Updated ServiceModel instance.
        :raises ValidationError: If the updated data fails validation.
        """
        try:
            service.service_type = validated_data.get('service_type', service.service_type)
            service.service_provider = validated_data.get('service_provider', service.service_provider)
            service.services_charge = validated_data.get('services_charge', service.services_charge)
            service.description = validated_data.get('description', service.description)
            
            service.save()
            return service
        except IntegrityError:
            raise ValidationError("Service update failed due to integrity issues.")

    def delete_service(self, service):
        """
        Delete a service.
        :param service: ServiceModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            service.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting service: {str(e)}")
