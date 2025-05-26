from django.db import models


class ProductSubCategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('ProductCategoryModel', on_delete=models.CASCADE,related_name='fk_product_sub_categories_id')  # FK to Category model
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_product_sub_categories_user_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_product_sub_categories_user_id')

    class Meta:
        db_table = 'product_sub_category'    
    def __str__(self):
        return self.name