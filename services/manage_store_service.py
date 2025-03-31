from urllib import request
from django.shortcuts import get_object_or_404
from django.db.models import Q
from control_panel.models import *


def get_store_list():
    return user_model.objects.all()