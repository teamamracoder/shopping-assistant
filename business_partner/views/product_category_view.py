from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductCategorySerializer
from services import services

class ProductCategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = services.product_category_service.get_all_categories()
        serializer = ProductCategorySerializer(categories, many=True)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(ProductCategorySerializer)
    def post(self, request):
        category = services.product_category_service.create_category(request.serializer.validated_data)
        return Res.success("S-20002", ProductCategorySerializer(category).data, status.HTTP_201_CREATED)

class ProductCategoryDetailAPIView(APIView):
    def get(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ProductCategorySerializer(category)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(ProductCategorySerializer)
    def put(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_category = services.product_category_service.update_category(category, request.serializer.validated_data)
        return Res.success("S-20001", ProductCategorySerializer(updated_category).data)
    
    @validate_serializer(ProductCategorySerializer)
    def patch(self, request, pk):
        request.serializer.partial = True
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_category = services.product_category_service.update_category(
            category, request.serializer.validated_data)
        return Res.success("S-20001", ProductCategorySerializer(updated_category).data)

    def delete(self, request, pk):
        category = services.product_category_service.get_category_by_id(pk)
        if not category:
            return Res.error(data={"message": "Category not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_category_service.delete_category(category)
        return Res.success("S-20003", {"message": "Category deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
