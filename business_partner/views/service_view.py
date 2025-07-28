from rest_framework.views import APIView
from rest_framework import status
from decorators import validate_serializer, partial_serializer
from utils.response_utils import Res
from ..serializers import ServiceTypeModelSerializer, ServiceSerializer
from services import services
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ServiceListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="List all services",
        responses={200: ServiceSerializer(many=True)}
    )
    def get(self, request):
        services_list = services.service_api.get_the_all_service()
        serializer = ServiceSerializer(services_list, many=True)
        return Res.success("S-22001", serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new service",
        request_body=ServiceSerializer,
        responses={201: ServiceSerializer}
    )
    @validate_serializer(ServiceSerializer)
    def post(self, request):
        new_service = services.service_api.create_the_service(request.serializer.validated_data)
        return Res.success("S-22002", ServiceSerializer(new_service).data, status.HTTP_201_CREATED)


class ServiceDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="Retrieve service by ID",
        responses={200: ServiceSerializer, 404: "Service not found"}
    )
    def get(self, request, pk):
        service = services.service_api.get_the_service_by_id(pk)
        if not service:
            return Res.error(data={"message": "Service not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service)
        return Res.success("S-22001", serializer.data)

    @swagger_auto_schema(
        operation_summary="Update full service by ID",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer, 404: "Service not found"}
    )
    @validate_serializer(ServiceSerializer)
    def put(self, request, pk):
        service = services.service_api.get_the_service_by_id(pk)
        if not service:
            return Res.error(data={"message": "Service not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_service = services.service_api.update_the_service_by_id(service, request.serializer.validated_data)
        return Res.success("S-22001", ServiceSerializer(updated_service).data)

    @swagger_auto_schema(
        operation_summary="Partially update service by ID",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer, 404: "Service not found"}
    )
    @partial_serializer(ServiceSerializer, partial=True)
    def patch(self, request, pk):
        service = services.service_api.get_the_service_by_id(pk)
        if not service:
            return Res.error(data={"message": "Service not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_service = services.service_api.update_the_service_by_id(service, request.serializer.validated_data)
        return Res.success("S-22001", ServiceSerializer(updated_service).data)

    @swagger_auto_schema(
        operation_summary="Delete service by ID",
        responses={204: openapi.Response(description="No Content"), 404: "Service not found"}
    )
    def delete(self, request, pk):
        service = services.service_api.get_the_service_by_id(pk)
        if not service:
            return Res.error(data={"message": "Service not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.service_api.delete_the_service_by_id(pk)
        return Res.success("S-22003", {"message": "Service deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)


class ServiceTypeListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="List all service types",
        responses={200: ServiceTypeModelSerializer(many=True)}
    )
    def get(self, request):
        service_types = services.service_type_api.get_all_the_service_type()
        serializer = ServiceTypeModelSerializer(service_types, many=True)
        return Res.success("S-21001", serializer.data)

    @swagger_auto_schema(
        operation_summary="Create new service type",
        request_body=ServiceTypeModelSerializer,
        responses={201: ServiceTypeModelSerializer}
    )
    @validate_serializer(ServiceTypeModelSerializer)
    def post(self, request):
        new_service_type = ServiceTypeModelSerializer().create(request.serializer.validated_data)
        return Res.success("S-21002", ServiceTypeModelSerializer(new_service_type).data, status.HTTP_201_CREATED)


class ServiceTypeDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="Retrieve service type by ID",
        responses={200: ServiceTypeModelSerializer, 404: "Service Type not found"}
    )
    def get(self, request, pk):
        service_type = services.service_type_api.get_service_type_by_id(pk)
        if not service_type:
            return Res.error(data={"message": "Service Type not found"}, http_status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceTypeModelSerializer(service_type)
        return Res.success("S-21001", serializer.data)

    @swagger_auto_schema(
        operation_summary="Update full service type by ID",
        request_body=ServiceTypeModelSerializer,
        responses={200: ServiceTypeModelSerializer, 404: "Service Type not found"}
    )
    @validate_serializer(ServiceTypeModelSerializer)
    def put(self, request, pk):
        service_type = services.service_type_api.get_service_type_by_id(pk)
        if not service_type:
            return Res.error(data={"message": "Service Type not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_service_type = services.service_type_api.update_the_service_type_by_id(service_type, request.serializer.validated_data)
        return Res.success("S-21001", ServiceTypeModelSerializer(updated_service_type).data)

    @swagger_auto_schema(
        operation_summary="Partially update service type by ID",
        request_body=ServiceTypeModelSerializer,
        responses={200: ServiceTypeModelSerializer, 404: "Service Type not found"}
    )
    @partial_serializer(ServiceTypeModelSerializer, partial=True)
    def patch(self, request, pk):
        service_type = services.service_type_api.get_service_type_by_id(pk)
        if not service_type:
            return Res.error(data={"message": "Service Type not found"}, http_status=status.HTTP_404_NOT_FOUND)
        updated_service_type = services.service_type_api.update_the_service_type_by_id(service_type, request.serializer.validated_data)
        return Res.success("S-21001", ServiceTypeModelSerializer(updated_service_type).data)

    @swagger_auto_schema(
        operation_summary="Delete service type by ID",
        responses={204: openapi.Response(description="No Content"), 404: "Service Type not found"}
    )
    def delete(self, request, pk):
        service_type = services.service_type_api.get_service_type_by_id(pk)
        if not service_type:
            return Res.error(data={"message": "Service Type not found"}, http_status=status.HTTP_404_NOT_FOUND)
        services.service_type_api.delete_the_service_type_by_id(pk)
        return Res.success("S-21003", {"message": "Service Type deleted successfully"}, http_status=status.HTTP_204_NO_CONTENT)
