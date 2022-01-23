
from django.shortcuts import render

def index(request) :
    print('rootWEB index ~ ')
    return render(request , 'map_main.html')

