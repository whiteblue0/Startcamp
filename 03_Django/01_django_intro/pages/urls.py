from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
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
]