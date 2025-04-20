from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ProductsModel

class ProductModelService:
    def get_all_products():
        return ProductsModel.objects.all()

    def get_product_by_id(product_id):
        return ProductsModel.objects.filter(id=product_id).first()

    def create_product(validated_data):
        return ProductsModel.objects.create(**validated_data)

    def update_product(instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete_product(instance):
        instance.delete()
