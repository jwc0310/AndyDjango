
from django.http import HttpResponse
from django.shortcuts import render

def andy(request):
    context     = {}
    context['hello'] = 'hello world'
    return render(request, 'andy.html', context)


def hello(request):
    return HttpResponse("hello world")


def hello2(request):
    return HttpResponse("hello world2")