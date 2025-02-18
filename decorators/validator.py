from functools import wraps
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
                return Res.error(status_code, http_status=status.HTTP_400_BAD_REQUEST)
            
            # Attach the validated serializer to the request object
            request.serializer = serializer
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
