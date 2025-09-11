from django.urls import path
from auth_app.views import *
from auth_app.views.auth_view import LogoutApiView, SendOTPView, VerifyOTPView, Login_Page,  SignupApiView, SignupView, UnauthorizedView

urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('login-page/', Login_Page.as_view(), name='login_page'),    

    # signup (GET -> page, POST -> API)
    path('signup/', SignupView.as_view(), name='signup_page'),
    path('signup-api/', SignupApiView.as_view(), name='signup_api'),
    path('logout/', LogoutApiView.as_view(), name='logout_api'),

    path('unauthorized/', UnauthorizedView.as_view(), name='unauthorized_page'),


]