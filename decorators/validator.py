from functools import wraps

from django.http import HttpResponseForbidden, JsonResponse
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


# def store_auth_in_session(func):
#     @wraps(func)
#     def wrapper(view, request, *args, **kwargs):
#         response = func(view, request, *args, **kwargs)

#         # If response is a success and contains user data
#         if hasattr(response, 'data') and 'user' in response.data:
#             request.session['auth'] = {
#                 'access_token': response.data.get('access_token'),
#                 'refresh_token': response.data.get('refresh_token'),
#                 'user': response.data.get('user')
#             }
#             request.session.modified = True  # Mark session as modified
#             request.session.save()
#             # Optional: print for debug
#             print(f"[Session] Stored user in session: {request.session['auth']}")

#         return response

#     return wrapper


def role_required(*allowed_roles):
    """
    Decorator to restrict view access to users with specific roles.
    Usage:
        @role_required(Role.ADMIN, Role.SELLER)
    """
    allowed_values = [role.value for role in allowed_roles]

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.session.get('auth', {}).get('user')

            if not user:
                return HttpResponseForbidden("Unauthorized: No user in session.")

            if user.get('role') not in allowed_values:
                return HttpResponseForbidden("Access Denied: Insufficient permissions.")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator