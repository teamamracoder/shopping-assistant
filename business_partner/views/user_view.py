from rest_framework.views import APIView
from rest_framework import status

from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import UserSerializer
from services import services

class UserListCreateAPIView(APIView):
    def get(self, request):
        users = services.user_service.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Res.success("S-10001", serializer.data)

    @validate_serializer(UserSerializer)
    def post(self, request):
        user = services.user_service.create_user(request.serializer.validated_data)
        return Res.success("S-10002", UserSerializer(user).data, status.HTTP_201_CREATED)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = services.user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Res.success("S-10001", serializer.data)

    @validate_serializer(UserSerializer)
    def put(self, request, pk):
        user = services.user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_user = services.user_service.update_user(user, request.serializer.validated_data)
        return Res.success("S-10001", UserSerializer(updated_user).data)

    def delete(self, request, pk):
        user = services.user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.user_service.delete_user(user)
        return Res.success("S-10003", {"message": "User deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)