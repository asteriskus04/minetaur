from django.shortcuts import render
from django.http import HttpResponse
from testdb import users

def index(request):
    return render(request, 'main/index.html')


def testdb(request):
    return HttpResponse(users)
