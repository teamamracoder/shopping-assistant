from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductCategorySerializer
from services import services

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductCategoryListCreateAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="List all product categories",
    operation_description="Fetch and return a list of all available product categories.",
    responses={200: openapi.Response(description="List of product categories")}
    )    
    def get(self, request):
        categories = services.product_category_service.get_all_categories()
        serializer = ProductCategorySerializer(categories, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new product category",
        operation_description="Creates a new product category using the provided name and description.",
        request_body=ProductCategorySerializer,
        responses={201: openapi.Response(description="Created product category")}
    )
    @validate_serializer(ProductCategorySerializer)
    def post(self, request):
        category = services.product_category_service.create_category(request.serializer.validated_data)
        return Res.success("S-20002", ProductCategorySerializer(category).data, status.HTTP_201_CREATED)

class ProductCategoryDetailAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="Retrieve a product category by ID",
    operation_description="Returns the details of a product category identified by its ID.",
    responses={200: openapi.Response(description="Product category detail"), 404: "Category not found"}
    )
    def get(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductCategorySerializer(category)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(ProductCategorySerializer)
    @swagger_auto_schema(
        operation_summary="Update a product category completely",
        operation_description="Updates the entire product category data identified by its ID using PUT method.",
        request_body=ProductCategorySerializer,
        responses={200: openapi.Response(description="Updated product category"), 404: "Category not found"}
    )
    def put(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_category = services.product_category_service.update_category(category, request.serializer.validated_data)
        return Res.success("S-20001", ProductCategorySerializer(updated_category).data)
    
    @swagger_auto_schema(
        operation_summary="Partially Update a product category",
        operation_description="Partially update the fields of an existing product sub-category.",
        request_body=ProductCategorySerializer,
        responses={200: openapi.Response(description="Category soft deleted"), 404: "Category not found"}
    )
    def patch(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)

        # Perform soft delete
        services.product_category_service.delete_category(category)
        return Res.success("S-20003", {"message": "Category soft deleted (is_active=False)"})


    @swagger_auto_schema(
        operation_summary="Soft Delete a Product Category",
        operation_description="Performs a soft delete on the category by setting is_active=False.",
        request_body=ProductCategorySerializer,
        responses={204: openapi.Response(description="Category deleted successfully"), 404: "Category not found"}
    )
    def delete(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_category_service.delete_category(category)
        return Res.success("S-20003", {"message": "Category deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
