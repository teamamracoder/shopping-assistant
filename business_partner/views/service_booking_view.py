from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers.service_booking_serializer import ServiceBookingModelSerializer
from services import services
from rest_framework.response import Response

class ServiceBookingListCreateAPIView(APIView):
    def get(self, request):
        print(f"Requested path: {request.path}")
        bookings = services.service_booking_service.get_all_bookings()
        serializer = ServiceBookingModelSerializer(bookings, many=True)
        return Res.success("S-30001", serializer.data)

    @validate_serializer(ServiceBookingModelSerializer)
    def post(self, request):
        booking = services.service_booking_service.create_booking(request.serializer.validated_data)
        return Res.success("S-30002", ServiceBookingModelSerializer(booking).data, status.HTTP_201_CREATED)


class ServiceBookingDetailAPIView(APIView):
    def get(self, request, pk):
        booking = services.service_booking_service.get_booking_by_id(pk)
        if not booking:
            return Res.error(data={"message": "Booking not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceBookingModelSerializer(booking)
        return Res.success("S-30001", serializer.data)

    @validate_serializer(ServiceBookingModelSerializer)
    def put(self, request, pk):
        booking = services.service_booking_service.get_booking_by_id(pk)
        if not booking:
            return Res.error(data={"message": "Booking not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_booking = services.service_booking_service.update_booking(booking, request.serializer.validated_data)
        return Res.success("S-30001", ServiceBookingModelSerializer(updated_booking).data)
    
    @validate_serializer(ServiceBookingModelSerializer)
    def patch(self, request, pk):
        """
        Partially update an existing service booking.
        :param request: The incoming request containing partial data.
        :param pk: The primary key (ID) of the service booking.
        :return: The updated service booking instance.
        """
        booking = services.service_booking_service.get_booking_by_id(pk)
        if not booking:
            return Res.error(data={"message": "Booking not found"}, http_status=status.HTTP_404_NOT_FOUND)
        
        # The update service is called here with the validated data (which might not have all fields)
        updated_booking = services.service_booking_service.update_booking(booking, request.serializer.validated_data)
        
        return Res.success("S-30001", ServiceBookingModelSerializer(updated_booking).data)

    def delete(self, request, pk):
        booking = services.service_booking_service.get_booking_by_id(pk)
        if not booking:
            return Res.error(data={"message": "Booking not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.service_booking_service.delete_booking(booking)
        return Res.success("S-30003", {"message": "Booking deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)