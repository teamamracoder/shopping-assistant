from django.conf import settings


def print_log(*args):
    if settings.DEBUG:
        print(args)