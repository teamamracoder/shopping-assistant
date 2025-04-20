from django.db import IntegrityError
from django.forms import ValidationError
from control_panel.models import ProductsModel

class ProductModelService:
    def get_all_products(self):
        """
        Fetch all products from the database.
        :return: QuerySet of all ProductsModel instances.
        """
        return ProductsModel.objects.all()

    def get_product_by_id(self, pk):
        """
        Fetch a product by its primary key (ID).
        :param pk: Primary key (ID) of the product.
        :return: ProductsModel instance if found, None otherwise.
        """
        try:
            return ProductsModel.objects.get(pk=pk)
        except ProductsModel.DoesNotExist:
            return None

    def create_product(self, validated_data):
        """
        Create a new product with validated data.
        :param validated_data: Dictionary containing product data.
        :return: Newly created ProductsModel instance.
        :raises ValidationError: If creation fails due to integrity issues.
        """
        try:
            return ProductsModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("Product creation failed due to integrity constraints.")

    def update_product(self, product, validated_data):
        """
        Update an existing product with new validated data.
        :param product: ProductsModel instance to update.
        :param validated_data: Dictionary containing new data.
        :return: Updated ProductsModel instance.
        :raises ValidationError: If update fails due to integrity issues.
        """
        try:
            product.name = validated_data.get('name', product.name)
            product.product_code = validated_data.get('product_code', product.product_code)
            product.description = validated_data.get('description', product.description)
            product.price = validated_data.get('price', product.price)
            product.discount_per = validated_data.get('discount_per', product.discount_per)
            product.quantity = validated_data.get('quantity', product.quantity)
            product.maf_date = validated_data.get('maf_date', product.maf_date)
            product.exp_date = validated_data.get('exp_date', product.exp_date)
            product.image_urls = validated_data.get('image_urls', product.image_urls)
            product.category = validated_data.get('category', product.category)
            product.sub_category = validated_data.get('sub_category', product.sub_category)
            product.others_category = validated_data.get('others_category', product.others_category)
            product.is_active = validated_data.get('is_active', product.is_active)
            product.updated_by = validated_data.get('updated_by', product.updated_by)

            product.save()
            return product
        except IntegrityError:
            raise ValidationError("Product update failed due to integrity issues.")

    def delete_product(self, product):
        """
        Delete a product.
        :param product: ProductsModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            product.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting product: {str(e)}")

