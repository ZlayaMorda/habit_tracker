from django.shortcuts import render
from django.http import HttpResponse


def habits_list(request):
    return HttpResponse("Habits list")
