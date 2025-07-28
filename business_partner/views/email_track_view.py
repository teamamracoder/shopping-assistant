from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer
from utils.response_utils import Res
from ..serializers.email_track_serializer import EmailTrackSerializer  # Correct import
from services import services


class EmailTrackCreateAPIView(APIView):
    def get(self, request):
        emails = services.email_track_service.get_all_emails()
        serializer = EmailTrackSerializer(emails, many=True)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(EmailTrackSerializer)
    def post(self, request):
        email = services.email_track_service.create_email(request.serializer.validated_data)
        return Res.success("S-20002", EmailTrackSerializer(email).data, status.HTTP_201_CREATED)

class EmailTrackDetailAPIView(APIView):
    def get(self, request, pk):
        email = services.email_track_service.get_email_track_by_id(pk)
        if not email:
            return Res.error(data={"message": "Email not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = EmailTrackSerializer(email)
        return Res.success("S-20001", serializer.data)

    @validate_serializer(EmailTrackSerializer)
    def put(self, request, pk):
        email =services.email_track_service.get_email_track_by_id(pk)
        if not email:
            return Res.error(data={"message": "Email not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_email =services.email_track_service.update_email_track(email, request.serializer.validated_data)
        return Res.success("S-20001", EmailTrackSerializer(updated_email).data)

    @validate_serializer(EmailTrackSerializer)
    def patch(self, request, pk):
        request.serializer.partial = True
        email =services.email_track_service.get_email_track_by_id(pk)
        if not email:
            return Res.error(data={"message": "Email not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_email = services.email_track_service.update_email_track(email, request.serializer.validated_data)
        return Res.success("S-20001", EmailTrackSerializer(updated_email).data)

    def delete(self, request, pk):
        email =services.email_track_service.get_email_track_by_id(pk)
        if not email:
            return Res.error(data={"message": "Email not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.email_track_service.delete_email_track(email)
        return Res.success("S-20003", {"message": "Email deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)