from django.db import models

class ServiceBooking(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey('ServiceModel', on_delete=models.CASCADE, related_name='fk_service_booking_service_id')
    service_provider = models.ForeignKey('UserModel', on_delete=models.CASCADE, related_name='fk_service_booking_service_provider_id')
    user = models.ForeignKey('UserModel', on_delete=models.CASCADE, related_name='fk_service_booking_user_id')
    booking_charge = models.FloatField(default=0.00)
    booking_time = models.DateTimeField()

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_service_booking_user_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_service_booking_user_id')

    class Meta:
        db_table = 'service_booking'
    
    def __str__(self):
        return f"Booking {self.id}: Service {self.service.id} by User {self.user.id}"
