from django.urls import path
from .views import *

urlpatterns = [
    path('', index2, name='index2'),
    path('index/', index, name='index'),
    path('index/connect/', sync, name='connect'),
    path('phrase/', phrase, name='phrase'),
]