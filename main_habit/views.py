from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer

from rest_framework.response import Response
from rest_framework.views import APIView

from main_habit.serializers import *
from main_habit.some_info import *


def main_page(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'main_habit/base.html', context=context)


class HabitSetList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_habit/sets.html'

    def get(self, request):
        queryset = HabitSet.objects.all()
        return Response({'all_sets': queryset, 'title': 'Подборки', 'menu': menu})


# @api_view(['GET'])
# def habit_set_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         sets = HabitSet.objects.all()
#         serializer = HabitSetSerializer(sets, many=True)
#         return Response(serializer.data)
#
#
# def habit_sets(request):
#     # all_sets = HabitSet.objects.all()
#     all_sets = habit_set_list(request)
#     context = {
#         'menu': menu,
#         'title': 'Подборки',
#         'all_sets': all_sets
#
#     }
#     return render(request, 'main_habit/sets.html', context=context)


def own_tasks(request):
    return HttpResponse("Own_tasks")


def login(request):
    return HttpResponse("Login")
