from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('testdb', views.testdb),
    path('infomining', views.min1),
    path('api/getmap', views.getmap)

]
