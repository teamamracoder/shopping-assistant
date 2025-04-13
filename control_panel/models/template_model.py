from django.db import models
from django.contrib.postgres.fields import ArrayField

class TemplateModel(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    payload = models.JSONField(blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    placeholders = ArrayField(
        models.JSONField(),
        blank=True,
        null=True
    )
    image_urls = ArrayField(
        models.URLField(max_length=500),
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey('UserModel', on_delete=models.CASCADE,blank=True,null=True, 
        related_name='fk_create_templates_user_id'
    )
    updated_by = models.ForeignKey('UserModel',on_delete=models.CASCADE,blank=True,null=True, 
        related_name='fk_update_templates_user_id'
    )

    class Meta:
        db_table = 'templates'

    def __str__(self):
        return f"Template ID: {self.id}, Subject: {self.subject}, Active: {self.is_active}"
