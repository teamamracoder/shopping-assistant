from django.db import models

class ServiceType(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    
    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_service_type_users_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_service_type_users_id')

    class Meta:
        db_table = 'service_type'    

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"
