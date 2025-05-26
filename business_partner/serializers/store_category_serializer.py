from rest_framework import serializers
from control_panel.models import StoreCategoryModel

class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategoryModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by', 'updated_by']
