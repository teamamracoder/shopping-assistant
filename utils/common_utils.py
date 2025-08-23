from django.conf import settings


def print_log(*args):
    if settings.DEBUG:
        print(args)

def get_user_id(request):
        return request.session.get('auth', {}).get('user', {}).get('id')