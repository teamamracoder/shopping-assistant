from control_panel.models import StoreCategoryModel

class StoreCategoryService:
    def list_store_categories(self):
        return StoreCategoryModel.objects.filter(is_active=True)

    def create_store_category(self, validated_data, user = None):
        return StoreCategoryModel.objects.create(**validated_data, created_by=user)

    def get_store_category(self, pk):
        try:
            return StoreCategoryModel.objects.get(pk=pk, is_active=True)
        except StoreCategoryModel.DoesNotExist:
            return None

    def update_store_category(self, store_category, validated_data, user = None):
        for attr, value in validated_data.items():
            setattr(store_category, attr, value)
        store_category.updated_by = user 
        store_category.save()
        return store_category

    def delete_store_category(self, store_category):
        store_category.is_active = False
        store_category.save()
        return True