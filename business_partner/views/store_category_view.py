from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import StoreCategorySerializer
from services import store_category_service

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StoreCategoryListCreateView(APIView):
    def get(self, request):
        categories = store_category_service.StoreCategoryService().list_store_categories()
        serializer = StoreCategorySerializer(categories, many=True)
        return Res.success("S-30001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=StoreCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )    
    @validate_serializer(StoreCategorySerializer)
    def post(self, request):
        # category = store_category_service.StoreCategoryService().create_store_category(request.serializer.validated_data, user=request.user) # If the frontend is ready then use this line 
        category = store_category_service.StoreCategoryService().create_store_category(request.serializer.validated_data)
        return Res.success("S-30002", StoreCategorySerializer(category).data, status.HTTP_201_CREATED)  



class StoreCategoryDetailView(APIView):
    def get(self, request, pk):
        category = store_category_service.StoreCategoryService().get_store_category(pk)
        if not category:
            return Res.error(data={"message": "Store category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreCategorySerializer(category)
        return Res.success("S-30003", serializer.data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=StoreCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )    
    @validate_serializer(StoreCategorySerializer)
    def put(self, request, pk):
        category = store_category_service.StoreCategoryService().get_store_category(pk)
        if not category:
            return Res.error(data={"message": "Store category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        # updated_category = store_category_service.StoreCategoryService().update_store_category(category, request.serializer.validated_data, user=request.user) # If the frontend is ready then use this line 
        updated_category = store_category_service.StoreCategoryService().update_store_category(category, request.serializer.validated_data) 
        return Res.success("S-30004", StoreCategorySerializer(updated_category).data)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=StoreCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )    
    @validate_serializer(StoreCategorySerializer)
    def patch(self, request, pk):
        category = store_category_service.StoreCategoryService().get_store_category(pk)
        if not category:
            return Res.error(data={"message": "Store category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreCategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            # updated_category = store_category_service.StoreCategoryService().update_store_category(category, serializer.validated_data, user=request.user)  #If the frontend is ready then use this line
            updated_category = store_category_service.StoreCategoryService().update_store_category(category, request.serializer.validated_data)
            return Res.success("S-30006", StoreCategorySerializer(updated_category).data)
        return Res.error(data={"message": serializer.errors}, http_status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
    operation_summary="Say Hello",
    operation_description="Returns a greeting message using the provided name",
    request_body=StoreCategorySerializer,
    responses={200: openapi.Response(description="Greeting Response")}
    )
    def delete(self, request, pk):
        category = store_category_service.StoreCategoryService().get_store_category(pk)
        if not category:
            return Res.error(data={"message": "Store category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        store_category_service.StoreCategoryService().delete_store_category(category)
        return Res.success("S-30005", {"message": "Store category deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
