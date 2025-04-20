from django.db import models
from constants.enums import Role,Gender
from django.contrib.postgres.fields import ArrayField

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.IntegerField(
        choices=[(gender.value, gender.name) for gender in Gender],
        blank=True,
        null=True
    )
    dob = models.DateField(blank=True,null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    is_seller = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)
    designation = models.CharField(max_length=100, blank=True, null=True)
    roles = ArrayField(
        models.IntegerField(
            choices=[(type.value, type.name) for type in Role],
            default=Role.END_USER.value,
            blank=True
        ),
        blank=True
    )
    bio = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_create_users_user_id')
    updated_by = models.ForeignKey('UserModel', on_delete=models.CASCADE, blank=True, null=True, related_name='fk_update_users_user_id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    class Meta:
        db_table = 'users'
         
    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"