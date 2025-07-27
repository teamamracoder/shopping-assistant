from django.db import models

class StoreCategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        'UserModel', on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='fk_create_store_categories_user_id')
    updated_by = models.ForeignKey(
        'UserModel', on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='fk_update_store_categories_user_id'
    )

    class Meta:
        db_table = 'store_categories'

    def __str__(self):
        return self.name
