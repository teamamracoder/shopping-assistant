from rest_framework import serializers
from control_panel.models import EmailTrackModel
from control_panel.models import UserModel,TemplateModel


class EmailTrackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    template = serializers.PrimaryKeyRelatedField(queryset=TemplateModel.objects.all())
    msg_subject = serializers.CharField(max_length=255)
    msg_body = serializers.CharField()
    receiver = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    sender = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())
    sent_at = serializers.DateTimeField(read_only=True)

    is_active = serializers.BooleanField(default=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), required=False, allow_null=True)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), required=False, allow_null=True)

    def create(self, validated_data):
        return EmailTrackModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.template = validated_data.get('template', instance.template)
        instance.msg_subject = validated_data.get('msg_subject', instance.msg_subject)
        instance.msg_body = validated_data.get('msg_body', instance.msg_body)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.sender = validated_data.get('sender', instance.sender)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.updated_by = validated_data.get('updated_by', instance.updated_by)

        instance.save()
        return instance
