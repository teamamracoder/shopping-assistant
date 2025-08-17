from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from functools import wraps

def jwt_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        jwt_auth = JWTAuthentication()
        try:
            user_auth_tuple = jwt_auth.authenticate(request)
            if user_auth_tuple is None:
                raise AuthenticationFailed("Invalid or missing token")
            request.user, request.auth = user_auth_tuple
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
        return func(self, request, *args, **kwargs)
    return wrapper


def role_required(roles: list):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            jwt_auth = JWTAuthentication()
            try:
                user_auth_tuple = jwt_auth.authenticate(request)
                if user_auth_tuple is None:
                    raise AuthenticationFailed("Invalid or missing token")
                request.user, request.auth = user_auth_tuple

                if request.user.role not in roles:
                    return Response({'message': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

            except AuthenticationFailed as e:
                return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
