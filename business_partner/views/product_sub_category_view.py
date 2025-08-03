from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductSubCategorySerializer
from services import services  # Import your service manager

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductSubCategoryListCreateAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="List all Product Sub-Categories",
    operation_description="Retrieve a list of all available product sub-categories.",
    responses={200: openapi.Response(description="List of product sub-categories")}
    )
    def get(self, request):
        sub_categories = services.product_sub_category_service.get_all_sub_categories()
        serializer = ProductSubCategorySerializer(sub_categories, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Create a Product Sub-Category",
    operation_description="Create a new product sub-category with name, category and other details.",
    request_body=ProductSubCategorySerializer,
    responses={201: openapi.Response(description="Sub-category created successfully")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def post(self, request):
        sub_category = services.product_sub_category_service.create_sub_category(request.serializer.validated_data)
        return Res.success("S-20002", ProductSubCategorySerializer(sub_category).data, status.HTTP_201_CREATED)

class ProductSubCategoryDetailAPIView(APIView):
    @swagger_auto_schema(
    operation_summary="Retrieve a Product Sub-Category",
    operation_description="Get details of a specific product sub-category using its ID.",
    responses={200: openapi.Response(description="Product sub-category details")}
    )
    def get(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSubCategorySerializer(sub_category)
        return Res.success("S-20001", serializer.data)
    

    @swagger_auto_schema(
        operation_summary="Update a Product Sub-Category",
        operation_description="Fully update a product sub-category with the provided ID.",
        request_body=ProductSubCategorySerializer,
        responses={200: openapi.Response(description="Sub-category updated successfully")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def put(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated = services.product_sub_category_service.update_sub_category(sub_category, request.serializer.validated_data)
        return Res.success("S-20001", ProductSubCategorySerializer(updated).data)


    @swagger_auto_schema(
    operation_summary="Partially Update a Product Sub-Category",
    operation_description="Partially update the fields of an existing product sub-category.",
    request_body=ProductSubCategorySerializer,
    responses={200: openapi.Response(description="Sub-category partially updated")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def patch(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        
        updated = services.product_sub_category_service.update_sub_category(sub_category, request.serializer.validated_data)
        return Res.success("S-20001", ProductSubCategorySerializer(updated).data)


    @swagger_auto_schema(
    operation_summary="Soft Delete a Product Sub-Category",
    operation_description="Perform a Soft Delete a product sub-category by setting is_active=False..",
    responses={204: openapi.Response(description="Sub-category deleted successfully")}
    )
    def delete(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_sub_category_service.delete_sub_category(sub_category)
        return Res.success("S-20003", {"message": "Sub-category deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
