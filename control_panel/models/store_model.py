from django.db import models
from django.contrib.postgres.fields import ArrayField
from control_panel.models import UserModel,StoreCategoryModel  # Assuming your UserModel is in control_panel.models

class StoreModel(models.Model):
    id = models.AutoField(primary_key=True)  # 1. Id
    owner = models.ForeignKey('UserModel', on_delete=models.CASCADE, related_name='fk_create_stores_user_id')
    store_name = models.CharField(max_length=255)  # 3. StoreName
    registration_no = models.CharField(max_length=255)  # 4. RegistrationNo
    gst_no = models.CharField(max_length=255)  # 5. GSTNo
    store_category = models.ForeignKey('StoreCategoryModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_store_categories_store_categorie_id')
    # contact_no = ArrayField(models.CharField(max_length=15), blank=True)  # 7. ContactNo (Array of strings)
    contact_no = models.CharField(max_length=15)
    alternate_contact_no =  models.CharField(max_length=15,blank=True,null=True)
    # email = ArrayField(models.EmailField(), blank=True)  # 8. Email (Array of strings)
    email = models.EmailField()
    alternate_email= models.EmailField(blank=True, null=True)
    open_time = models.DateTimeField()  # 9. OpenTime
    close_time = models.DateTimeField()  # 10. CloseTime
    address = models.TextField(blank=True, null=True)  # 11. Address
    location = models.CharField(max_length=255,blank=True, null=True)  # 12. Location
    street_or_road = models.CharField(max_length=255,blank=True, null=True)  # 13. Street/Road
    village_or_city = models.CharField(max_length=255,blank=True, null=True)  # 14. Village/City
    district = models.CharField(max_length=255,blank=True, null=True)  # 15. District
    state = models.CharField(max_length=255,blank=True, null=True)  # 16. State
    pin_code = models.IntegerField(blank=True, null=True)
    store_image_urls = ArrayField(models.URLField(max_length=255), blank=True,null=True)  # 18. StoreImage_urls (Array of strings)

    is_active = models.BooleanField(db_default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_stores_users_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_stores_users_id')

    class Meta:
        db_table = 'stores'
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    def __str__(self):
        return f"{self.store_name} - {self.owner.first_name} {self.owner.last_name}"

