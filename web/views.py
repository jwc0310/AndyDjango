
from django.http import HttpResponse
from django.shortcuts import render, redirect


def andy(request):

    context     = {}

    context['hello'] = 'hello world'
    return render(request, 'andy.html', context)


def hello(request):
    name = request.GET.get("name")

    return HttpResponse('姓名： {}'.format(name))


def hello3(request):
    return redirect('/hello/')


def hello_post(request):
    name = request.POST.get("name")
    print('name: ' + name)
    return HttpResponse('姓名： {}'.format(name))


def hello2(request):
    return HttpResponse("hello world2")