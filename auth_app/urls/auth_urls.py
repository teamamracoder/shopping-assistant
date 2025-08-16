from django.urls import path
from auth_app.views import *
from auth_app.views.auth_view import SendOTPView, VerifyOTPView, Login_Page, Signup_Page


urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path('login-page/', Login_Page.as_view(), name='login_page'),    
    path('signup-page/', Signup_Page.as_view(), name='signup_page'),

]