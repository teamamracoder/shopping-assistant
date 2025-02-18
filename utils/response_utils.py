from rest_framework.response import Response
from rest_framework import status

class Res:
    @staticmethod
    def error(status_code: str = 'E-10001', http_status = status.HTTP_200_OK, data = None):
        res_data = {
            'status': 'error',
            'status_code': status_code
        } if data is None else {
            'status': 'error',
            'status_code': status_code,
            "data": data
        }
        return Response(data=res_data, status=http_status)

    @staticmethod
    def success(status_code: str, data: any = None, http_status = status.HTTP_200_OK):
        res_data = {
            'status': 'success',
            'status_code': status_code
        } if data is None else {
            'status': 'success',
            'status_code': status_code,
            "data": data
        }
        return Response(data=res_data, status=http_status)