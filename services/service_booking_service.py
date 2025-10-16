# services/service_booking_service.py
from control_panel.models.service_booking_model import ServiceBookingModel
from django.utils import timezone

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

    # def update_booking(self, instance, validated_data):
    #     """
    #     Update booking instance with validated data.
    #     """
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance
    
    def update_booking(self, instance, validated_data, user_id):
        """
        Update booking instance safely without losing created_by or created_at.
        """
        # Preserve original values
        old_created_by = instance.created_by
        old_created_at = instance.created_at

        # Update allowed fields only
        for attr, value in validated_data.items():
            # যদি created_by বা created_at থাকে, সেগুলো skip করবো
            if attr not in ['created_by', 'created_at']:
                setattr(instance, attr, value)

        # Preserve original audit fields
        if not instance.created_by:
            instance.created_by = user_id
        if not instance.created_by:
            instance.created_by = old_created_by
        if not instance.created_at:
            instance.created_at = old_created_at

        # Update updater info
        instance.updated_by = user_id
        instance.updated_at = timezone.now()

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

    def toggle_active_status(self, instance):
        """
        Toggle the 'is_active' status and return the updated instance.
        """
        if instance is None:
            return None  # safety guard

        instance.is_active = not instance.is_active
        instance.save()
        return instance  # ✅ return the updated booking


