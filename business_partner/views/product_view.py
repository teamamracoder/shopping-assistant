from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import ProductSerializer
from services import services

class ProductListCreateAPIView(APIView):
    def get(self, request):
        print(f"Requested path: {request.path}")
        products = services.product_service.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Res.success("S-20001", serializer.data)

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

    @validate_serializer(ProductSerializer)
    def put(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_product = services.product_service.update_product(product, request.serializer.validated_data)
        return Res.success("S-20001", ProductSerializer(updated_product).data)

    @validate_serializer(ProductSerializer)  
    def patch(self, request, pk):
        request.serializer.partial = True 
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_product = services.product_service.update_product(product, request.serializer.validated_data)
        return Res.success("S-20001", ProductSerializer(updated_product).data)

    
    def delete(self, request, pk):
        product = services.product_service.get_product_by_id(pk)
        if not product:
            return Res.error(data={"message": "Product not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.product_service.delete_product(product)
        return Res.success("S-20003", {"message": "Product deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
