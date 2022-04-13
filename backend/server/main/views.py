from django.shortcuts import render
from django.http import HttpResponse
import testing_pyshark


def index(request):
    return render(request, 'main/index.html')


def testdb(request):
    return HttpResponse('dffsgwrg')


def min(request):
    check_point = 0
    testing_pyshark.scan(check_point)
    if check_point == 1:
        return HttpResponse('Майнинг')
    else:
        return HttpResponse('Всё тихо')
