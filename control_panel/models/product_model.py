from django.db import models
from django.contrib.postgres.fields import ArrayField

class ProductsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100, unique=True,blank=True, null=True)  # Optional product code
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    discount_per = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    quantity = models.IntegerField(default=0)
    maf_date = models.DateTimeField(blank=True, null=True)
    exp_date = models.DateTimeField(blank=True, null=True)
    image_urls = ArrayField(
        models.URLField(max_length=500),
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        'ProductCategoryModel', 
        on_delete=models.CASCADE, 
        related_name='fk_products_categories_id'
    )
    sub_category = models.ForeignKey(
        'ProductSubCategoryModel', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='fk_products_sub_categories_id'
    )
    others_category = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='fk_create_products_user_id'
    )
    updated_by = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='fk_update_products_user_id'
    )

    class Meta:
        db_table = 'products'

    def _str_(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}"