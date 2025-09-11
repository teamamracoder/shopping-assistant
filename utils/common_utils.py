from django.conf import settings

from control_panel.models.user_model import UserModel


def print_log(*args):
    if settings.DEBUG:
        print(args)

def get_user_id(request):
        user_id=request.session.get('auth', {}).get('user', {}).get('id')
        return UserModel.objects.get(pk=user_id)
