from django.db import models

class ProductCategoryModel(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented integer ID
    name = models.CharField(max_length=255)  # Category name
    description = models.TextField(blank=True, null=True)  # Optional description

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        'UserModel', on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name='fk_create_product_categories_user_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_product_categories_user_id')
    
    class Meta:
        db_table = 'product_categories'
    def __str__(self):
        return self.name
