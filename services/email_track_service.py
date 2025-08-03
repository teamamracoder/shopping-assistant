from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import EmailTrackModel


class EmailTrackService:
    def get_all_emails(self):
        """
        Fetch all email records.
        :return: QuerySet of all EmailTrackModel instances.
        """
        return EmailTrackModel.objects.all()

    # def get_email_by_id(self, pk):
    def get_email_track_by_id(self, pk):
        """
        Fetch an email by its primary key.
        :param pk: Primary key (ID) of the email.
        :return: EmailTrackModel instance if found, None otherwise.
        """
        try:
            return EmailTrackModel.objects.get(pk=pk)
        except EmailTrackModel.DoesNotExist:
            return None

    def create_email(self, validated_data):
        """
        Create a new email tracking entry.
        :param validated_data: Dict containing valid email data.
        :return: Newly created EmailTrackModel instance.
        :raises ValidationError: If creation fails due to integrity issues.
        """
        try:
            return EmailTrackModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("Email creation failed due to integrity constraints.")

    def update_email(self, email, validated_data):
        """
        Update an existing email entry.
        :param email: EmailTrackModel instance to update.
        :param validated_data: Dict with new data.
        :return: Updated EmailTrackModel instance.
        :raises ValidationError: If update fails.
        """
        try:
            email.template = validated_data.get('template', email.template)
            email.msg_subject = validated_data.get('msg_subject', email.msg_subject)
            email.msg_body = validated_data.get('msg_body', email.msg_body)
            email.receiver = validated_data.get('receiver', email.receiver)
            email.sender = validated_data.get('sender', email.sender)
            email.is_active = validated_data.get('is_active', email.is_active)
            email.updated_by = validated_data.get('updated_by', email.updated_by)

            email.save()
            return email
        except IntegrityError:
            raise ValidationError("Email update failed due to integrity issues.")

    def delete_email(self, email):
        """
        Delete an email entry.
        :param email: EmailTrackModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            email.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting email: {str(e)}")
