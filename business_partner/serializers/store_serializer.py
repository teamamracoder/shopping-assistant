from rest_framework import serializers
from control_panel.models import StoreModel

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')