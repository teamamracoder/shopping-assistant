# services/service_booking_service.py
from control_panel.models.service_booking_model import ServiceBookingModel

class ServiceBookingModelService:
    def get_all_bookings(self):
        return ServiceBookingModel.objects.all()
    
    def get_booking_by_id(self, pk):
        try:
            return ServiceBookingModel.objects.get(pk=pk)
        except ServiceBookingModel.DoesNotExist:
            return None
    
    def create_booking(self, validated_data):
        return ServiceBookingModel.objects.create(**validated_data)

    def update_booking(self, instance, validated_data):
        """
        Update booking instance with validated data.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    def delete_booking(self, instance):
        instance.delete()

    def toggle_active_status(self, instance):
        """
        Toggle the is_active status of the booking instance.
        """
        instance.is_active = not instance.is_active
        instance.save()

    def get_booking_by_id(self, pk):
        try:
            return ServiceBookingModel.objects.get(pk=pk)
        except ServiceBookingModel.DoesNotExist:
            return None


