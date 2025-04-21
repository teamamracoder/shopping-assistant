from control_panel.models import StoreModel
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


class StoreService:

    def list_stores(self):
        return StoreModel.objects.filter(is_active=True)

    def create_store(self, validated_data, user = None):
        return StoreModel.objects.create(**validated_data, created_by = user)

    def get_store(self, pk):
        try:
            return StoreModel.objects.get(pk=pk, is_active=True)
        except StoreModel.DoesNotExist:
            return None

    def update_store(self, store, validated_data, user = None):
        for attr, value in validated_data.items():
            setattr(store, attr, value)
        store.updated_by = user    
        store.save()
        return store

    def delete_store(self, store):
        store.is_active = False
        store.save()
        return True
