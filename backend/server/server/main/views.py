import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from testing_pyshark import scan


def index(request):
    return render(request, 'main/index.html')



def testdb(request):
    return HttpResponse('dffsgwrg')


def min1(request):
    return HttpResponse('Страница для проверки функций')


def getmap(request):
    scan()
    with open('main/static/main/js/data1.json') as f:
        result = json.load(f)
        return JsonResponse(result)
