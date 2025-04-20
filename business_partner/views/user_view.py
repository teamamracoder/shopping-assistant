from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from services.user_service import user_service


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = user_service.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Res.success("S-10001", serializer.data)

    @validate_serializer(UserCreateSerializer)
    def post(self, request):
                # Check if the user is already Existing and active
        if user_service.user_exists(request.serializer.validated_data['email']):
            user = user_service.get_user_by_email(request.serializer.validated_data['email'])
            user = user_service.activate_user(user)
            return Res.success("S-10001", UserSerializer(user).data, status.HTTP_200_OK)
        
        # Create a new user if the email doesn't exist
        user = user_service.create_user(request.serializer.validated_data)
        return Res.success("S-10002", UserSerializer(user).data, status.HTTP_201_CREATED)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Res.success("S-10001", serializer.data)

    @validate_serializer(UserUpdateSerializer)
    def put(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_user = user_service.update_user(user, request.serializer.validated_data)
        return Res.success("S-10001", UserSerializer(updated_user).data)
    
    @validate_serializer(UserUpdateSerializer)
    def patch(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        
        # Using `partial=True` to allow partial updates
        updated_user = user_service.update_user(user, request.serializer.validated_data)
        return Res.success("S-10001", UserSerializer(updated_user).data)

    def delete(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        user_service.delete_user(user)
        return Res.success("S-10003", {"message": "User deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)