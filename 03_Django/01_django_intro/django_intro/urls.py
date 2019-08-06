"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/',views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lottos/', views.lottos),
    path('ispal/<word>/', views.ispal),
    path('isbirth/', views.isbirth),
    path('student/<str:>', views.student),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('Circle/<int:r>/', views.Circle),
    path('mult/<int:num1>/<int:num2>', views.mult),
    path('introduce_2/<str:name>/<int:age>/', views.introduce_2),
    path('hello/<str:name>/<int:age>/', views.hello),
    path('images/', views.images),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
