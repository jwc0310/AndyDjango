"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views, testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('hello2/', views.hello3),
    path('andy/', views.andy),
    url(r'^$', views.hello2),
    path('testdb/', testdb.query),
    path('testdb/query/', testdb.query),
    path('testdb/add/', testdb.add),
    path('testdb/delete/', testdb.delete),
    path('testdb/update/', testdb.update),

    url(r'^search_form/$', search.search_form),
    url(r'^search/$', search.search),

    url(r'^search-post/$', search2.search_post),

    url(r'^search-post2/$', search2.search_post2),
]
