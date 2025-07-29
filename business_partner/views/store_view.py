from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from decorators.validator import validate_serializer
from services import store_service
from utils.response_utils import Res
from ..serializers import StoreSerializer
# from services.store_service import storeModelService
from services.store_service import storeModelService


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StoreListCreateView(APIView):
    @swagger_auto_schema(
    operation_summary="Get All Stores",
    operation_description="Retrieve a list of all stores currently stored in the system.",
    responses={200: openapi.Response(description="List of stores")}
    )
    def get(self, request):
        stores = store_service.storeModelService().list_stores()
        serializer = StoreSerializer(stores, many=True)
        return Res.success("S-20001", serializer.data)

    @swagger_auto_schema(
    operation_summary="Create a New Store",
    operation_description="Create and save a new store using the data provided in the request body.",
    request_body=StoreSerializer,
    responses={201: openapi.Response(description="Store created successfully")}
    )
    @validate_serializer(StoreSerializer)
    def post(self, request):
        # store = store_service.storeModelService().create_store(request.serializer.validated_data, user=request.user)   # If the frontend is ready then use this line 
        store = store_service.storeModelService().create_store(request.serializer.validated_data) 
        return Res.success("S-20002", StoreSerializer(store).data, status.HTTP_201_CREATED)


class StoreDetailView(APIView):
    @swagger_auto_schema(
    operation_summary="Get a Store by ID",
    operation_description="Retrieve a single store by providing its ID in the URL path.",
    responses={200: openapi.Response(description="Store details"), 404: openapi.Response(description="Store not found")}
    )
    def get(self, request, pk):
        store = store_service.storeModelService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store)
        return Res.success("S-20003", serializer.data)

    @swagger_auto_schema(
        operation_summary="Update Entire Store",
        operation_description="Update the entire store object with new data by providing all fields.",
        request_body=StoreSerializer,
        responses={200: openapi.Response(description="Store updated successfully"), 404: openapi.Response(description="Store not found")}
    )
    @validate_serializer(StoreSerializer)
    def put(self, request, pk):
        store = store_service.storeModelService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        # updated_store = store_service.storeModelService().update_store(store, request.serializer.validated_data, user=request.user) # If the frontend is ready then use this line 
        updated_store = store_service.storeModelService().update_store(store, request.serializer.validated_data) 
        return Res.success("S-20004", StoreSerializer(updated_store).data)
    
    @swagger_auto_schema(
    operation_summary="Partially Update Store",
    operation_description="Update specific fields of the store object. Only provided fields will be updated.",
    request_body=StoreSerializer,
    responses={200: openapi.Response(description="Store partially updated"), 404: openapi.Response(description="Store not found")}
    )
    @validate_serializer(StoreSerializer)
    def patch(self, request, pk):
        store = store_service.storeModelService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
            # updated_store = store_service.storeModelService().update_store(store, serializer.validated_data, user=request.user)  # If the frontend is ready then use this line
            updated_store = store_service.storeModelService().update_store(store, request.serializer.validated_data)
            return Res.success("S-20006", StoreSerializer(updated_store).data)
        return Res.error(data={"message": serializer.errors}, http_status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
    operation_summary="Soft Delete a Store",
    operation_description="Performs a soft delete on the Store by setting is_active=False.",
    responses={204: openapi.Response(description="Store deleted successfully"), 404: openapi.Response(description="Store not found")}
    )
    def delete(self, request, pk):
        store = store_service.storeModelService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        store_service.storeModelService().delete_store(store)
        return Res.success("S-20005", {"message": "Store deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)