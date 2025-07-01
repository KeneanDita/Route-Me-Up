from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    x = 1
    y = 5
    return render(request, 'index.html',)
