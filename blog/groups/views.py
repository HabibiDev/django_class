from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Person


def index(request):
    name_of_group = request.GET['group_name']
    person_qs = Person.objects.filter(group__name = name_of_group).values()
    response = JsonResponse(list(person_qs), safe=False)
    return response