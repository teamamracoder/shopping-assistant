from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from decorators.validator import validate_serializer
from services import store_service
from utils.response_utils import Res
from ..serializers import StoreSerializer
from services.store_service import StoreService


class StoreListCreateView(APIView):
    def get(self, request):
        stores = store_service.StoreService().list_stores()
        serializer = StoreSerializer(stores, many=True)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(StoreSerializer)
    def post(self, request):
        # store = store_service.StoreService().create_store(request.serializer.validated_data, user=request.user)   # If the frontend is ready then use this line 
        store = store_service.StoreService().create_store(request.serializer.validated_data) 
        return Res.success("S-20002", StoreSerializer(store).data, status.HTTP_201_CREATED)


class StoreDetailView(APIView):
    def get(self, request, pk):
        store = store_service.StoreService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store)
        return Res.success("S-20003", serializer.data)


    @validate_serializer(StoreSerializer)
    def put(self, request, pk):
        store = store_service.StoreService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        # updated_store = store_service.StoreService().update_store(store, request.serializer.validated_data, user=request.user) # If the frontend is ready then use this line 
        updated_store = store_service.StoreService().update_store(store, request.serializer.validated_data) 
        return Res.success("S-20004", StoreSerializer(updated_store).data)
    

    @validate_serializer(StoreSerializer)
    def patch(self, request, pk):
        store = store_service.StoreService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(store, data=request.data, partial=True)
        if serializer.is_valid():
            # updated_store = store_service.StoreService().update_store(store, serializer.validated_data, user=request.user)  # If the frontend is ready then use this line
            updated_store = store_service.StoreService().update_store(store, request.serializer.validated_data)
            return Res.success("S-20006", StoreSerializer(updated_store).data)
        return Res.error(data={"message": serializer.errors}, http_status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        store = store_service.StoreService().get_store(pk)
        if not store:
            return Res.error(data={"message": "Store not found"}, http_status=status.HTTP_404_NOT_FOUND)
        store_service.StoreService().delete_store(store)
        return Res.success("S-20005", {"message": "Store deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)