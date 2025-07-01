from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return render(request, 'index.html', {
        'Greeting': 'Hello World',
        'message': 'Welcome to the Django Playground!'
    })
