from django.db import models
from control_panel.models.user_model import UserModel
from constants.enums import RELATIONSHIP_TYPE

class CustomerProvider(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='fk_customer_users_user_id')
    provider = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='fk_provider_users_user_id')
    relationship_type = models.IntegerField(
        choices=[(type.value, type.name) for type in RELATIONSHIP_TYPE],    
        blank=False, null=False
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customer_providers'
        unique_together = ('customer', 'provider', 'relationship_type')  # Prevent duplicate links
        
    def __str__(self):
        return f"Customer: {self.customer.id}, Provider: {self.provider.id}, Type: {self.relationship_type}"    
