from functools import wraps

from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect
from constants.enums import Role
from utils.common_utils import print_log
from utils.response_utils import Res
from rest_framework import status

def validate_serializer(serializer_class, status_code: str = 'E-10001'):
    """
    Decorator to validate the serializer on the incoming request data.
    If invalid, it returns an error response. If valid, it adds the
    validated serializer to the request object.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            serializer = serializer_class(data=request.data)
            if not serializer.is_valid():
                print_log(serializer.errors)
                return Res.error(
                    status_code=status_code,
                    http_status=status.HTTP_400_BAD_REQUEST,
                    data=serializer.errors  # Pass field-level errors as 'data'
                )

            # Attach the validated serializer to the request object
            request.serializer = serializer
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator


def partial_serializer(serializer_class, partial=False):
    def decorator(view_func):
        def _wrapped_view(self, request, *args, **kwargs):
            serializer = serializer_class(data=request.data, partial=partial)
            if not serializer.is_valid():
                return Res.error(data=serializer.errors, http_status=status.HTTP_400_BAD_REQUEST)
            request.serializer = serializer
            return view_func(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(*args, **kwargs):
            if hasattr(args[0], 'request'):
                request = args[0].request
            elif hasattr(args[0], 'session'):
                request = args[0]
            else:
                request = args[1]

            user = request.session.get('auth', {}).get('user')
            user_roles = user.get('roles', []) if user else []
            if not any(role in roles for role in user_roles):
                print("Access denied")
                return redirect("login_page")
            return view_func(*args, **kwargs)
        return _wrapped_view
    return decorator