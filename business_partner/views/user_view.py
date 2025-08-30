from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from services.user_service import user_service
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter


class UserListCreateAPIView(APIView):
    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="List Users",
        description="Retrieve all users",
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        users = user_service.get_all_users()
        serializer = UserSerializer(users, many=True)
        return Res.success("S-10001", serializer.data)
    
    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="Create User",
        description="Create a new user with username, email, etc.",
        request=UserCreateSerializer,
        responses={201: UserSerializer},
    )
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
    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="Retrieve a user by ID",
        description="Fetch detailed information of a specific user using their ID.",
        responses={
            200: OpenApiResponse(UserSerializer, description="User retrieved successfully"),
            404: OpenApiResponse(description="User not found"),
        }
    )
    def get(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Res.success("S-10001", serializer.data)
    

    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="Update a user (full update)",
        description="Update all fields of an existing user. Overwrites the entire user data.",
        request=UserUpdateSerializer,
        responses={
            200: OpenApiResponse(UserSerializer, description="User updated successfully"),
            404: OpenApiResponse(description="User not found"),
        }
    )
    def put(self, request, pk):
        return self.update_user(request, pk, partial=False)

    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="Partially update a user",
        description="Update only specific fields of a user without overwriting everything.",
        request=UserUpdateSerializer,
        responses={
            200: OpenApiResponse(UserSerializer, description="User partially updated"),
            404: OpenApiResponse(description="User not found"),
        }
    )
    def patch(self, request, pk):
        return self.update_user(request, pk, partial=True)

    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="Delete a user",
        description="Permanently delete a user account by ID.",
        responses={
            204: OpenApiResponse(description="User deleted successfully"),
            404: OpenApiResponse(description="User not found"),
        }
    )
    def delete(self, request, pk):
        user = user_service.get_user_by_id(pk)
        if not user:
            return Res.error(data={"message": "User not found"}, http_status=status.HTTP_404_NOT_FOUND)
        user_service.delete_user(user)
        return Res.success("S-10003", {"message": "User deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
    
    
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



class MyCustomerListAPIView(APIView):
    @extend_schema(
        tags=["Users"], # Add this line to categorize under "Users"
        summary="List customers of the logged-in seller",
        description=(
            "Retrieve a paginated list of all customers linked to the authenticated seller. "
            "Supports search, sorting, and pagination via query parameters."
        ),
        parameters=[
            OpenApiParameter("search", str, description="Search by first name, last name, or email", required=False),
            OpenApiParameter("sort", str, description="Sort by: id, first_name, last_name, email, created_at", required=False),
            OpenApiParameter("page", int, description="Page number (default: 1)", required=False),
            OpenApiParameter("page_size", int, description="Number of results per page (default: 5)", required=False),
        ],
        responses={
            200: OpenApiResponse(response=UserSerializer(many=True), description="List of customers"),
            403: OpenApiResponse(description="Only sellers can view customers"),
        }
    )
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
