from django.shortcuts import render
from django.http import HttpResponse
from testing_pyshark import check_point

def index(request):
    return render(request, 'main/index.html')


def testdb(request):
    return HttpResponse('dffsgwrg')

def min(request):
    if check_point == 1:
        return HttpResponse('Майнинг')
    else:
        return HttpResponse('Всё тихо')

