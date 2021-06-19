from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)


def search_post2(request):

    name = request.path
    print("search_post2 " + name)

    name2 = request.method
    print("search_post2 " + name2)

    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)