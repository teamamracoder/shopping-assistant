from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ServiceBooking

class ServiceBookingService:
    def get_all_bookings(self):
        """
        Fetch all service bookings from the database.
        :return: Queryset of all ServiceBooking instances.
        """
        return ServiceBooking.objects.all()

    def get_booking_by_id(self, pk):
        """
        Fetch a service booking by its primary key (ID).
        :param pk: Primary key (ID) of the service booking.
        :return: ServiceBooking instance if found, None otherwise.
        """
        try:
            return ServiceBooking.objects.get(pk=pk)
        except ServiceBooking.DoesNotExist:
            return None

    def update_booking(self, booking, validated_data):
        """
        Update an existing service booking with new validated data.
        :param booking: ServiceBooking instance to be updated.
        :param validated_data: A dictionary of data to update the booking with.
        :return: Updated ServiceBooking instance.
        :raises ValidationError: If the updated data fails validation.
        """
        try:
            booking.service = validated_data.get('service', booking.service)
            booking.service_provider = validated_data.get('service_provider', booking.service_provider)
            booking.user = validated_data.get('user', booking.user)
            booking.booking_charge = validated_data.get('booking_charge', booking.booking_charge)
            booking.booking_time = validated_data.get('booking_time', booking.booking_time)
            
            booking.save()
            return booking
        except IntegrityError:
            raise ValidationError("Service booking update failed due to integrity issues.")

    def delete_booking(self, booking):
        """
        Delete a service booking.
        :param booking: ServiceBooking instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            booking.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting service booking: {str(e)}")
