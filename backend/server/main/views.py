from django.shortcuts import render
from django.http import HttpResponse
from testing_pyshark import scan


def index(request):
    scan()
    return render(request, 'main/index.html')



def testdb(request):
    return HttpResponse('dffsgwrg')


def min1(request):
    return HttpResponse('Страница для проверки функций')
