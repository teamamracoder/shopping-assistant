from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from services.user_service import user_service
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q


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
    

    def update_user(self, request, pk, partial=False):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)

        serializer = UserUpdateSerializer(
            instance=user,
            data=request.data,
            partial=partial,
            context={'request': request}
        )
        
        serializer.is_valid(raise_exception=True)
        updated_user = serializer.save()
        return Res.success("S-10001", UserSerializer(updated_user).data)

    def put(self, request, pk):
        return self.update_user(request, pk, partial=False)

    def patch(self, request, pk):
        return self.update_user(request, pk, partial=True)

    # def delete(self, request, pk):
    #     user = user_service.get_user_by_id(pk)
    #     if not user:
    #         return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
    #     user_service.delete_user(user)
    #     return Res.success("S-10003", {"message": "User deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
    def delete(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(
                data={"message": "User not found"},
                http_status=status.HTTP_404_NOT_FOUND
            )
        user_service.user_delete(pk)  
        return Res.success(
            "S-10003",
            {"message": "User deleted successfully"},
            http_status=status.HTTP_200_OK
        )

class MyCustomerListAPIView(APIView):
    def get(self, request):
        # Hardcoded user for now (replace with request.user if using auth)
        user = user_service.get_user_by_id(5)
        if not user.is_seller:
            return Res.error(
                data={"message": "You must be a seller to view customers"},
                http_status=status.HTTP_403_FORBIDDEN
            )

        # Get all customers linked to the seller
        customers = user_service.get_my_customers(user)

        # --- Query string parameters ---
        search = request.query_params.get('search', '')   # search by name
        sort = request.query_params.get('sort', 'id')     # field to sort by
        page = int(request.query_params.get('page', 1))   # default page 1
        page_size = int(request.query_params.get('page_size', 5))  # default 5

        # --- Search ---
        if search:
            customers = customers.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(email__icontains=search)
            )

        # --- Sorting ---
        if sort.lstrip('-') in ['id', 'first_name', 'last_name', 'email', 'created_at']:
            customers = customers.order_by(sort)

        # --- Pagination ---
        paginator = Paginator(customers, page_size)
        try:
            paged_customers = paginator.page(page)
        except EmptyPage:
            paged_customers = []

        serializer = UserSerializer(paged_customers, many=True)
        return Res.success("S-10001", {
            "results": serializer.data,
            "total": paginator.count,
            "page": page,
            "pages": paginator.num_pages
        })
