from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductSerializer
from services import services

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductListCreateAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="List all Products",
    operation_description="Retrieve a list of all available products.",
    responses={200: openapi.Response(description="List of products")}
    )
    
    def get(self, request):
        print(f"Requested path: {request.path}")
        products = services.product_service.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Create a Product",
    operation_description="Add a new product with details like name, price, and category.",
    request_body=ProductSerializer,
    responses={201: openapi.Response(description="Product created successfully")}
    )
    @validate_serializer(ProductSerializer)
    def post(self, request):
        product = services.product_service.create_product(request.serializer.validated_data)
        return Res.success("S-20002", ProductSerializer(product).data, status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="Retrieve a Product",
    operation_description="Fetch details of a specific product by ID.",
    responses={200: openapi.Response(description="Product details")}
    )
    def get(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Update a Product",
    operation_description="Fully update an existing product's information using its ID.",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Product updated successfully")}
    )
    @validate_serializer(ProductSerializer)
    def put(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_product = services.product_service.update_product(product, request.serializer.validated_data)
        return Res.success("S-20001", ProductSerializer(updated_product).data)

    @swagger_auto_schema(
    operation_summary="Partially Update a Product",
    operation_description="Partially update fields of a product like name or price using its ID.",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Product partially updated")}
    )   
    def patch(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            updated_product = services.product_service.update_product(product, serializer.validated_data)
            return Res.success("S-20004", ProductSerializer(updated_product).data)
        return Res.error(data=serializer.errors, http_status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
    operation_summary="Soft Delete a Product",
    operation_description="Performs a soft delete on the Product by setting is_active=False.",
    responses={204: openapi.Response(description="Product deleted successfully")}
)
    def delete(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_service.delete_product(product)
        return Res.success("S-20003", {"message": "Product deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
    

