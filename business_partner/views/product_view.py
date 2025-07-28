from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductSerializer
from services import services

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductListCreateAPIView(APIView):
    def get(self, request):
        print(f"Requested path: {request.path}")
        products = services.product_service.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    @validate_serializer(ProductSerializer)
    def post(self, request):
        product = services.product_service.create_product(request.serializer.validated_data)
        return Res.success("S-20002", ProductSerializer(product).data, status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    @validate_serializer(ProductSerializer)
    def put(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_product = services.product_service.update_product(product, request.serializer.validated_data)
        return Res.success("S-20001", ProductSerializer(updated_product).data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Greeting Response")}
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
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    def delete(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_service.delete_product(product)
        return Res.success("S-20003", {"message": "Product deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
    

