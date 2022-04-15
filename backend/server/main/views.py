from django.shortcuts import render
from django.http import HttpResponse
from testing_pyshark import scan


def index(request):
    return render(request, 'main/index.html')


def testdb(request):
    return HttpResponse('dffsgwrg')


def min1(request):
    point, iphnik = scan()
    if point == 1:
        return HttpResponse('Майнинг' + iphnik)
    else:
        return HttpResponse('Всё тихо')
