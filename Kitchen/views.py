
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return HttpResponse('PAGE 1')


def about(request):
    return HttpResponse('PAGE 2')
