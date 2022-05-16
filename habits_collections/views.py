from django.http import HttpResponse
from django.shortcuts import render


def page_name(request):
    return HttpResponse('habits collections page')
