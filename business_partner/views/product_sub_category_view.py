from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductSubCategorySerializer
from services import services  # Import your service manager

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductSubCategoryListCreateAPIView(APIView):
    def get(self, request):
        sub_categories = services.product_sub_category_service.get_all_sub_categories()
        serializer = ProductSubCategorySerializer(sub_categories, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSubCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def post(self, request):
        sub_category = services.product_sub_category_service.create_sub_category(request.serializer.validated_data)
        return Res.success("S-20002", ProductSubCategorySerializer(sub_category).data, status.HTTP_201_CREATED)

class ProductSubCategoryDetailAPIView(APIView):
    def get(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSubCategorySerializer(sub_category)
        return Res.success("S-20001", serializer.data)
    

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSubCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def put(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated = services.product_sub_category_service.update_sub_category(sub_category, request.serializer.validated_data)
        return Res.success("S-20001", ProductSubCategorySerializer(updated).data)


    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSubCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    @validate_serializer(ProductSubCategorySerializer)
    def patch(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        
        updated = services.product_sub_category_service.update_sub_category(sub_category, request.serializer.validated_data)
        return Res.success("S-20001", ProductSubCategorySerializer(updated).data)


    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=ProductSubCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    def delete(self, request, pk):
        sub_category = services.product_sub_category_service.get_sub_category_by_id(pk)
        if not sub_category:
            return Res.error(data={"message": "Sub-category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_sub_category_service.delete_sub_category(sub_category)
        return Res.success("S-20003", {"message": "Sub-category deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
