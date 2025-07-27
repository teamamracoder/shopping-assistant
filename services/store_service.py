from control_panel.models import StoreModel
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework import status
from django.db import transaction
from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import StoreModel

class storeModelService:
    def get_all_stores(self):
        """
        Fetch all stores from the database.
        :return: QuerySet of all StoreModel instances.
        """
        return StoreModel.objects.all()

    def get_store_by_id(self, pk):
        """
        Fetch a store by its primary key (ID).
        :param pk: Primary key (ID) of the store.
        :return: StoreModel instance if found, None otherwise.
        """
        try:
            return StoreModel.objects.get(pk=pk)
        except StoreModel.DoesNotExist:
            return None

    def create_store(self, validated_data):
        """
        Create a new store with validated data.
        :param validated_data: Dictionary containing store data.
        :return: Newly created StoreModel instance.
        :raises ValidationError: If creation fails due to integrity issues.
        """
        try:
            return StoreModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("store creation failed due to integrity constraints.")

    def update_store(self, store, validated_data):
        """
        Update an existing store with new validated data.
        :param store: StoreModel instance to update.
        :param validated_data: Dictionary containing new data.
        :return: Updated StoreModel instance.
        :raises ValidationError: If update fails due to integrity issues.
        """
        try:
            # store.owner = validated_data.get('name', store.owner)
            store.store_name = validated_data.get('store_code', store.store_name)
            store.registration_no = validated_data.get('registration_no', store.registration_no)
            store.gst_no = validated_data.get('gst_no', store.gst_no)
            store.store_category = validated_data.get('discount_per', store.store_category)
            store.contact_no = validated_data.get('quantity', store.contact_no)
            store.alternate_contact_no = validated_data.get('maf_date', store.alternate_contact_no)
            store.email = validated_data.get('exp_date', store.email)
            store.alternate_email = validated_data.get('category', store.alternate_email)
            store.open_time = validated_data.get('sub_category', store.open_time)
            store.close_time = validated_data.get('others_category', store.close_time)
            store.address = validated_data.get('is_active', store.address)
            store.location = validated_data.get('is_active', store.location)
            store.street_or_road = validated_data.get('is_active', store.street_or_road)
            store.village_or_city = validated_data.get('is_active', store.village_or_city)
            store.district = validated_data.get('is_active', store.district)
            store.state = validated_data.get('is_active', store.state)
            store.pin_code = validated_data.get('is_active', store.pin_code)
            store.store_image_urls = validated_data.get('image_urls', store.store_image_urls)
            store.is_active = validated_data.get('is_active', store.is_active)
            store.updated_by = validated_data.get('updated_by', store.updated_by)

            store.save()
            return store
        except IntegrityError:
            raise ValidationError("store update failed due to integrity issues.")

    def delete_store(self, store):
        """
        Delete a store.
        :param store: StoreModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            store.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting store: {str(e)}")





# class StoreService:

#     def list_stores(self):
#         return StoreModel.objects.filter(is_active=True)

#     def create_store(self, validated_data, user = None):
#         return StoreModel.objects.create(**validated_data, created_by = user)

#     def get_store(self, pk):
#         try:
#             return StoreModel.objects.get(pk=pk, is_active=True)
#         except StoreModel.DoesNotExist:
#             return None

#     def update_store(self, store, validated_data, user = None):
#         for attr, value in validated_data.items():
#             setattr(store, attr, value)
#         store.updated_by = user    
#         store.save()
#         return store

#     def delete_store(self, store):
#         store.is_active = False
#         store.save()
#         return True
