from django.db import models

class EmailTrackModel(models.Model):
    id = models.AutoField(primary_key=True)
    template = models.ForeignKey(
        'TemplateModel', 
        on_delete=models.CASCADE, 
        related_name='fk_email_tracks_template_id'
    )
    msg_subject = models.CharField(max_length=255)
    msg_body = models.TextField()
    receiver = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        related_name='fk_received_email_user_id'
    )
    sender = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        related_name='fk_sent_email_user_id'
    )
    sent_at = models.DateTimeField(auto_now_add=True)


    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_by = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='fk_create_email_track_user_id'
    )
    updated_by = models.ForeignKey(
        'UserModel', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='fk_update_email_track_users_id'
    )




    class Meta:
        db_table = 'email_track'

    def __str__(self):
        return f"Email ID: {self.id}, Subject: {self.msg_subject}, Sent at: {self.sent_at}"
