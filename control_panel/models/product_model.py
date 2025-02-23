from django.db import models
from django.contrib.postgres.fields import ArrayField

class ProductsModel(models.Model):
    id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
        'CategoryModel', 
        on_delete=models.CASCADE, 
        related_name='products_category_id'
    )
    sub_category = models.ForeignKey(
        'SubCategoryModel_sub_category_id', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='products_sub_category_id'
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

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}"
