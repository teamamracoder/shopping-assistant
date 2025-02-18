from rest_framework.views import APIView

from utils.response_utils import Res

class DemoView(APIView):
    
    def get(self, request):
        return Res.success('S-10000', 'Welcome to shopping_assistant app demo api')