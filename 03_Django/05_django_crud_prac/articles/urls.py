from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/new.html', views.new, name='new'),
    path('articles/create.html', views.create, name='create'),
    
]
