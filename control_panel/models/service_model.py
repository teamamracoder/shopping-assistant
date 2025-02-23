from django.db import models

class ServiceModel(models.Model):
    id = models.AutoField(primary_key=True)
    # service_name = models.CharField(max_length=100)

    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE,related_name='fk_create_services_service_type_id')

    service_provider = models.ForeignKey('UserModel', on_delete=models.CASCADE,related_name='fk_create_services_service_provider_id')

    services_charge = models.FloatField(default=0.00)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_services_users_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_services_users_id')

    class Meta:
        db_table = 'services'

    def __str__(self):
        return f"Service {self.id}: {self.description[:50]}"
