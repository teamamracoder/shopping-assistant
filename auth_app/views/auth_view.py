from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
import random
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from utils.response_utils import Res
from auth_app.serializers.auth_serializer import SendOtpSerializer, SignupSerializer, VerifyOtpSerializer, VerifyOTPResponseSerializer, SendOTPResponseSerializer, UserAuthSerializer
from constants.enums import Role
from decorators.validator import validate_serializer
from services import services
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from utils.response_utils import Res 

class SendOTPView(APIView):

    @swagger_auto_schema(
        operation_summary="send otp",
        operation_description="Enter email and send otp",
        request_body=SendOtpSerializer,
        responses={200: openapi.Response('Success', schema=SendOTPResponseSerializer)}
    )
    @validate_serializer(SendOtpSerializer)
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Res.error('Email is required', status=status.HTTP_400_BAD_REQUEST)
        
        # Generate 6-digit OTP
        otp = str(random.randint(100000, 999999))
        
        # Store OTP in cache (expires in 5 minutes)
        cache.set(f'otp_{email}', otp, timeout=300)
        
        # In production: Send OTP via email here
        print(f"OTP for {email}: {otp}")  # For development only

        is_existing_user = services.user_service.is_exist(email)
        
        return Res.success('OTP sent successfully', {"existing_user": is_existing_user})


class VerifyOTPView(APIView):
    
    @swagger_auto_schema(
        operation_summary="verify otp",
        operation_description="Enter email and otp to verify",
        request_body=VerifyOtpSerializer,
        responses={200: openapi.Response('Success', schema=VerifyOTPResponseSerializer)}
    )
    @validate_serializer(VerifyOtpSerializer)
    def post(self, request):
        email = request.serializer.validated_data.get('email')
        otp_attempt = request.serializer.validated_data.get('otp')
        
        if not email or not otp_attempt:
            return Response.error('Email and OTP are required', status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve OTP from cache
        cached_otp = cache.get(f'otp_{email}')
        
        if not cached_otp:
            return Res.error('OTP expired or not generated', status=status.HTTP_400_BAD_REQUEST)
        
        if cached_otp != otp_attempt:
            return Res.error('Invalid OTP', status.HTTP_400_BAD_REQUEST)
        
        # Get user by email
        user = services.user_service.get_user_by_email(email=email)
        is_new_user=False

        # Create user if does not exist
        if not user:
            is_new_user=True
            user = services.user_service.create_user(validated_data={
                "first_name": request.serializer.validated_data.get("first_name"),
                "last_name": request.serializer.validated_data.get("last_name"),
                "email": request.serializer.validated_data.get("email"),
                "roles": [Role.END_USER.value]
            })

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        cache.delete(f'otp_{email}')  # Clear OTP after successful verification
        
        # return Res.success(
        #     'Successsfully registered' if is_new_user else 'Login successfull',
        #     {
        #         'access_token': str(refresh.access_token),
        #         'refresh_token': str(refresh),
        #         'user': UserAuthSerializer(services.user_service.get_by_field(email=email)).data
        #     }
        # )

        # Prepare response data
        response_data = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user': UserAuthSerializer(services.user_service.get_by_field(email=email)).data
        }

        message = 'Successfully registered' if is_new_user else 'Login successful'


        # 🔐 Store auth info in session
        request.session['auth'] = {
            'access_token': response_data['access_token'],
            'refresh_token': response_data['refresh_token'],
            'user': response_data['user']
        }
        request.session.modified = True  # Optional, ensures session is saved


        # 🔍 Log to console
        # print(f"[VerifyOTPView] {message} - Response: {response_data}")

        return Res.success(message, response_data)

# Login View #
class Login_Page(View):
    def get(self, request):
        return render(request, 'login_page.html')
    
# Signup View #
class SignupView(View):
    """GET request -> return HTML page"""
    def get(self, request):
        return render(request, "signup_page.html")


class SignupApiView(APIView):
    """POST request -> create user via API"""
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApiView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"message": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Only works if blacklist app is enabled
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)