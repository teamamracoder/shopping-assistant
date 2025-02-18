import logging
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

logger = logging.getLogger(__name__)

class ErrorHandlerMiddleware(MiddlewareMixin):
    """
    Middleware to handle exceptions globally and return error responses in JSON format.
    """

    def process_exception(self, request, exception):
        # Log the exception details for debugging
        logger.error(f"Unhandled Exception: {str(exception)}", exc_info=True)

        # Define a standard error response
        response_data = {
            "status": "error",
            "status_code": "E-10001"
        }

        # Optionally, include debug information in development mode
        if settings.DEBUG:
            response_data["error"] = str(exception)

        # Return a JSON response with a 500 status code
        return JsonResponse(response_data, status=500)
